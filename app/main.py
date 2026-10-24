import os
import json
import random
import datetime
from pathlib import Path
from fastapi import FastAPI, HTTPException, Query, Request, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

from .database import get_db, init_db
from .seed_data import seed_database
from .models import OrderCreateRequest, CouponRequest, PincodeRequest, StatusUpdateRequest

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

app = FastAPI(
    title="SAGA ONLINE SHOP API",
    description="Drop-shipping E-commerce webapp demo with DeoDap direct fulfillment and margin tracking",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.on_event("startup")
def startup_event():
    init_db()
    # Check if products exist; if not, seed
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM products")
    count = cursor.fetchone()[0]
    conn.close()
    if count == 0:
        seed_database()

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    index_file = TEMPLATES_DIR / "index.html"
    if not index_file.exists():
        raise HTTPException(status_code=404, detail="Index template not found")
    with open(index_file, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/api/categories")
def get_categories():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    rows = cursor.fetchall()
    
    categories = []
    for r in rows:
        slug = r["slug"]
        if slug == "all":
            cursor.execute("SELECT COUNT(*) FROM products")
        else:
            cursor.execute("SELECT COUNT(*) FROM products WHERE category = ?", (slug,))
        prod_count = cursor.fetchone()[0]
        categories.append({
            "id": r["id"],
            "name": r["name"],
            "slug": r["slug"],
            "icon": r["icon"],
            "image_url": r["image_url"],
            "count": prod_count
        })
    conn.close()
    return categories

@app.get("/api/products")
def get_products(
    category: str = Query("all"),
    search: str = Query(""),
    sort: str = Query("popular"),
    trending_only: bool = Query(False)
):
    conn = get_db()
    cursor = conn.cursor()

    query = "SELECT * FROM products WHERE 1=1"
    params = []

    if category and category != "all":
        query += " AND category = ?"
        params.append(category)

    if search.strip():
        query += " AND (title LIKE ? OR description LIKE ? OR deodap_sku LIKE ?)"
        term = f"%{search.strip()}%"
        params.extend([term, term, term])

    if trending_only:
        query += " AND is_trending = 1"

    if sort == "price_low":
        query += " ORDER BY selling_price ASC"
    elif sort == "price_high":
        query += " ORDER BY selling_price DESC"
    elif sort == "margin_high":
        query += " ORDER BY (selling_price - wholesale_price) DESC"
    elif sort == "rating":
        query += " ORDER BY rating DESC, review_count DESC"
    else:  # popular / default
        query += " ORDER BY is_trending DESC, rating DESC, review_count DESC"

    cursor.execute(query, params)
    rows = cursor.fetchall()

    products = []
    for r in rows:
        margin = round(r["selling_price"] - r["wholesale_price"], 2)
        margin_percent = round((margin / r["selling_price"]) * 100, 1) if r["selling_price"] > 0 else 0
        discount_percent = round(((r["mrp"] - r["selling_price"]) / r["mrp"]) * 100) if r["mrp"] > 0 else 0

        products.append({
            "id": r["id"],
            "title": r["title"],
            "slug": r["slug"],
            "category": r["category"],
            "deodap_sku": r["deodap_sku"],
            "wholesale_price": r["wholesale_price"],
            "selling_price": r["selling_price"],
            "mrp": r["mrp"],
            "margin": margin,
            "margin_percent": margin_percent,
            "discount_percent": discount_percent,
            "stock": r["stock"],
            "rating": r["rating"],
            "review_count": r["review_count"],
            "badge": r["badge"],
            "description": r["description"],
            "features": json.loads(r["features_json"]),
            "image_url": r["image_url"],
            "gallery": json.loads(r["gallery_json"]),
            "is_trending": bool(r["is_trending"])
        })

    conn.close()
    return products

@app.get("/api/products/{product_id}")
def get_product_detail(product_id: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ? OR slug = ?", (product_id, product_id))
    r = cursor.fetchone()
    if not r:
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")

    margin = round(r["selling_price"] - r["wholesale_price"], 2)
    margin_percent = round((margin / r["selling_price"]) * 100, 1) if r["selling_price"] > 0 else 0
    discount_percent = round(((r["mrp"] - r["selling_price"]) / r["mrp"]) * 100) if r["mrp"] > 0 else 0

    product = {
        "id": r["id"],
        "title": r["title"],
        "slug": r["slug"],
        "category": r["category"],
        "deodap_sku": r["deodap_sku"],
        "wholesale_price": r["wholesale_price"],
        "selling_price": r["selling_price"],
        "mrp": r["mrp"],
        "margin": margin,
        "margin_percent": margin_percent,
        "discount_percent": discount_percent,
        "stock": r["stock"],
        "rating": r["rating"],
        "review_count": r["review_count"],
        "badge": r["badge"],
        "description": r["description"],
        "features": json.loads(r["features_json"]),
        "image_url": r["image_url"],
        "gallery": json.loads(r["gallery_json"]),
        "is_trending": bool(r["is_trending"])
    }

    # Fetch 4 related products
    cursor.execute(
        "SELECT * FROM products WHERE category = ? AND id != ? LIMIT 4",
        (r["category"], r["id"])
    )
    related_rows = cursor.fetchall()
    related = []
    for rel in related_rows:
        related.append({
            "id": rel["id"],
            "title": rel["title"],
            "selling_price": rel["selling_price"],
            "mrp": rel["mrp"],
            "image_url": rel["image_url"],
            "rating": rel["rating"]
        })

    conn.close()
    return {"product": product, "related": related}

@app.post("/api/coupons/apply")
def apply_coupon(payload: CouponRequest):
    code = payload.code.strip().upper()
    subtotal = payload.subtotal

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM coupons WHERE code = ? AND is_active = 1", (code,))
    coupon = cursor.fetchone()
    conn.close()

    if not coupon:
        raise HTTPException(status_code=400, detail="Invalid coupon code. Try 'SAGA10' or 'WELCOME50'")

    if subtotal < coupon["min_order_value"]:
        raise HTTPException(
            status_code=400,
            detail=f"Minimum cart value of ₹{coupon['min_order_value']} required for coupon {code}"
        )

    if coupon["discount_type"] == "percent":
        discount = round((subtotal * coupon["value"]) / 100, 2)
    else:
        discount = round(min(coupon["value"], subtotal), 2)

    return {
        "valid": True,
        "code": code,
        "discount": discount,
        "message": f"Coupon {code} applied successfully! You saved ₹{discount}"
    }

@app.post("/api/pincode/check")
def check_pincode(payload: PincodeRequest):
    pin = payload.pincode.strip()
    if len(pin) != 6 or not pin.isdigit():
        return {
            "deliverable": False,
            "message": "Please enter a valid 6-digit Indian postal pincode"
        }

    # Realistic estimation
    delivery_date = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%A, %d %b")
    return {
        "deliverable": True,
        "pincode": pin,
        "estimated_delivery": delivery_date,
        "shipping_method": "DeoDap Express Air Surface",
        "cod_available": False,
        "message": f"Standard Delivery by {delivery_date}. 100% Express Air Shipping!"
    }

@app.post("/api/orders")
def create_order(payload: OrderCreateRequest):
    if not payload.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    conn = get_db()
    cursor = conn.cursor()

    subtotal = 0.0
    total_wholesale = 0.0
    order_items = []

    for item in payload.items:
        cursor.execute("SELECT * FROM products WHERE id = ?", (item.product_id,))
        prod = cursor.fetchone()
        if not prod:
            conn.close()
            raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")

        item_subtotal = prod["selling_price"] * item.quantity
        item_wholesale = prod["wholesale_price"] * item.quantity
        subtotal += item_subtotal
        total_wholesale += item_wholesale

        order_items.append({
            "product_id": prod["id"],
            "title": prod["title"],
            "image_url": prod["image_url"],
            "selling_price": prod["selling_price"],
            "wholesale_price": prod["wholesale_price"],
            "quantity": item.quantity,
            "deodap_sku": prod["deodap_sku"],
            "item_subtotal": item_subtotal
        })

    # Discount calculation
    discount = 0.0
    if payload.coupon_code:
        code = payload.coupon_code.strip().upper()
        cursor.execute("SELECT * FROM coupons WHERE code = ? AND is_active = 1", (code,))
        cp = cursor.fetchone()
        if cp and subtotal >= cp["min_order_value"]:
            if cp["discount_type"] == "percent":
                discount = round((subtotal * cp["value"]) / 100, 2)
            else:
                discount = round(min(cp["value"], subtotal), 2)

    # Shipping fee calculation (Free above ₹499)
    shipping_fee = 0.0 if (subtotal - discount) >= 499.0 else 49.0
    total_amount = round(max(0, subtotal - discount + shipping_fee), 2)
    total_margin = round(total_amount - total_wholesale - shipping_fee, 2)

    order_id = f"SAGA-{random.randint(10000, 99999)}"
    payment_status = "Paid (Prepaid Online / UPI)"
    tracking_number = f"DD-EXP-{random.randint(100000, 999999)}"

    cursor.execute("""
    INSERT INTO orders (
        id, customer_name, customer_phone, customer_email, address, city, state,
        pincode, payment_method, payment_status, subtotal, discount, shipping_fee,
        total_amount, total_wholesale_cost, total_margin, status, items_json,
        deodap_sync_status, tracking_number
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        order_id, payload.customer_name, payload.customer_phone, payload.customer_email,
        payload.address, payload.city, payload.state, payload.pincode,
        payload.payment_method, payment_status, subtotal, discount, shipping_fee,
        total_amount, total_wholesale, total_margin, "Confirmed",
        json.dumps(order_items), "Synced to DeoDap Warehouse", tracking_number
    ))

    conn.commit()
    conn.close()

    # Pre-crafted WhatsApp message
    wa_items = "\n".join([f"• {i['quantity']}x {i['title']} (₹{i['selling_price']})" for i in order_items])
    wa_text = (
        f"*Order Confirmed with SAGA ONLINE SHOP!*\n\n"
        f"📦 *Order ID:* #{order_id}\n"
        f"👤 *Customer:* {payload.customer_name}\n"
        f"📞 *Phone:* {payload.customer_phone}\n"
        f"📍 *Delivery to:* {payload.city}, {payload.pincode}\n"
        f"💳 *Payment Mode:* {payload.payment_method}\n"
        f"💰 *Total Amount:* ₹{total_amount}\n\n"
        f"*Items:*\n{wa_items}\n\n"
        f"Thank you for shopping with SAGA Online Shop! Your order has been dispatched via express shipping."
    )

    return {
        "success": True,
        "order_id": order_id,
        "customer_name": payload.customer_name,
        "customer_phone": payload.customer_phone,
        "address": f"{payload.address}, {payload.city}, {payload.state} - {payload.pincode}",
        "payment_method": payload.payment_method,
        "payment_status": payment_status,
        "subtotal": subtotal,
        "discount": discount,
        "shipping_fee": shipping_fee,
        "total_amount": total_amount,
        "total_wholesale_cost": total_wholesale,
        "total_margin": total_margin,
        "tracking_number": tracking_number,
        "items": order_items,
        "whatsapp_url": f"https://wa.me/919922163722?text={round_encode(wa_text)}",
        "created_at": datetime.datetime.now().strftime("%d %b %Y, %I:%M %p")
    }

def round_encode(text: str) -> str:
    import urllib.parse
    return urllib.parse.quote(text)

@app.get("/api/orders/{order_id}")
def get_order_by_id(order_id: str):
    conn = get_db()
    cursor = conn.cursor()
    clean_id = order_id.replace("#", "").strip()
    cursor.execute("SELECT * FROM orders WHERE id = ? OR id = ?", (clean_id, f"SAGA-{clean_id}"))
    order = cursor.fetchone()
    conn.close()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    items = json.loads(order["items_json"])
    return {
        "order_id": order["id"],
        "customer_name": order["customer_name"],
        "customer_phone": order["customer_phone"],
        "customer_email": order["customer_email"],
        "address": f"{order['address']}, {order['city']}, {order['state']} - {order['pincode']}",
        "payment_method": order["payment_method"],
        "payment_status": order["payment_status"],
        "subtotal": order["subtotal"],
        "discount": order["discount"],
        "shipping_fee": order["shipping_fee"],
        "total_amount": order["total_amount"],
        "total_wholesale_cost": order["total_wholesale_cost"],
        "total_margin": order["total_margin"],
        "status": order["status"],
        "deodap_sync_status": order["deodap_sync_status"],
        "tracking_number": order["tracking_number"],
        "created_at": order["created_at"],
        "items": items
    }

@app.get("/api/admin/orders")
def get_admin_orders():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders ORDER BY created_at DESC")
    rows = cursor.fetchall()

    orders = []
    for r in rows:
        items = json.loads(r["items_json"])
        orders.append({
            "order_id": r["id"],
            "customer_name": r["customer_name"],
            "customer_phone": r["customer_phone"],
            "city": r["city"],
            "pincode": r["pincode"],
            "payment_method": r["payment_method"],
            "payment_status": r["payment_status"],
            "subtotal": r["subtotal"],
            "discount": r["discount"],
            "shipping_fee": r["shipping_fee"],
            "total_amount": r["total_amount"],
            "total_wholesale_cost": r["total_wholesale_cost"],
            "total_margin": r["total_margin"],
            "margin_percentage": round((r["total_margin"] / r["total_amount"]) * 100, 1) if r["total_amount"] > 0 else 0,
            "status": r["status"],
            "deodap_sync_status": r["deodap_sync_status"],
            "tracking_number": r["tracking_number"],
            "created_at": r["created_at"],
            "items_count": len(items),
            "items": items
        })

    conn.close()
    return orders

@app.get("/api/admin/stats")
def get_admin_stats():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT 
        COUNT(*) as total_orders,
        COALESCE(SUM(total_amount), 0) as gross_revenue,
        COALESCE(SUM(total_wholesale_cost), 0) as total_cogs,
        COALESCE(SUM(total_margin), 0) as total_profit
    FROM orders
    """)
    stats_row = cursor.fetchone()

    total_orders = stats_row["total_orders"]
    gross_revenue = round(stats_row["gross_revenue"], 2)
    total_cogs = round(stats_row["total_cogs"], 2)
    total_profit = round(stats_row["total_profit"], 2)
    avg_order_value = round(gross_revenue / total_orders, 2) if total_orders > 0 else 0
    profit_margin_percent = round((total_profit / gross_revenue) * 100, 1) if gross_revenue > 0 else 0

    conn.close()
    return {
        "total_orders": total_orders,
        "gross_revenue": gross_revenue,
        "total_cogs": total_cogs,
        "total_profit": total_profit,
        "avg_order_value": avg_order_value,
        "profit_margin_percent": profit_margin_percent
    }

@app.post("/api/admin/orders/{order_id}/sync-deodap")
def sync_order_to_deodap(order_id: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
    order = cursor.fetchone()
    if not order:
        conn.close()
        raise HTTPException(status_code=404, detail="Order not found")

    new_tracking = order["tracking_number"] or f"DD-EXP-{random.randint(100000, 999999)}"
    cursor.execute("""
    UPDATE orders 
    SET deodap_sync_status = 'Dispatched by DeoDap',
        status = 'In Transit',
        tracking_number = ?
    WHERE id = ?
    """, (new_tracking, order_id))
    conn.commit()
    conn.close()

    return {
        "success": True,
        "order_id": order_id,
        "deodap_sync_status": "Dispatched by DeoDap",
        "status": "In Transit",
        "tracking_number": new_tracking,
        "message": f"Order {order_id} synced directly to DeoDap fulfillment center! Shipped via BlueDart/Delhivery."
    }

@app.post("/api/admin/upload-image")
async def upload_product_image(file: UploadFile = File(...)):
    """Upload product photos directly into the web application"""
    allowed_extensions = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Invalid image type. Allowed: jpg, jpeg, png, webp, gif")

    products_dir = STATIC_DIR / "images" / "products"
    products_dir.mkdir(parents=True, exist_ok=True)

    import uuid
    safe_name = f"prod_{uuid.uuid4().hex[:10]}{ext}"
    dest_path = products_dir / safe_name

    contents = await file.read()
    with open(dest_path, "wb") as f:
        f.write(contents)

    rel_url = f"/static/images/products/{safe_name}"
    return {
        "success": True,
        "filename": safe_name,
        "url": rel_url,
        "message": "Product image uploaded successfully!"
    }

@app.get("/api/admin/uploaded-images")
def list_uploaded_images():
    """List all uploaded product images"""
    products_dir = STATIC_DIR / "images" / "products"
    if not products_dir.exists():
        return []
    images = []
    for f in os.listdir(products_dir):
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
            images.append({
                "filename": f,
                "url": f"/static/images/products/{f}"
            })
    return images

@app.post("/api/admin/add-product")
async def add_new_product(
    title: str = Form(...),
    category: str = Form(...),
    wholesale_price: float = Form(...),
    selling_price: float = Form(...),
    mrp: float = Form(...),
    stock: int = Form(50),
    badge: str = Form("New Arrival ⭐"),
    description: str = Form(...),
    image_url: str = Form(...)
):
    """Add a new product with uploaded image directly to catalog"""
    conn = get_db()
    cursor = conn.cursor()
    import uuid
    prod_id = f"SAGA-NEW-{uuid.uuid4().hex[:6].upper()}"
    slug = title.lower().replace(" ", "-").replace("/", "-")[:50]

    cursor.execute("""
    INSERT INTO products (
        id, title, slug, category, deodap_sku, wholesale_price, selling_price,
        mrp, stock, rating, review_count, badge, description, features_json,
        image_url, gallery_json, is_trending
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        prod_id, title, slug, category, f"DD-NEW-{uuid.uuid4().hex[:6].upper()}",
        wholesale_price, selling_price, mrp, stock, 4.8, 15, badge, description,
        json.dumps(["Direct Sourced High Quality", "Fast Express Shipping"]),
        image_url, json.dumps([image_url]), 1
    ))
    conn.commit()
    conn.close()

    return {
        "success": True,
        "product_id": prod_id,
        "message": f"Product '{title}' added to store successfully!"
    }
