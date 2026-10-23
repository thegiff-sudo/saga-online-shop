# SAGA ONLINE SHOP - Dropshipping E-Commerce Webapp

A modern, mobile-friendly dropshipping e-commerce web application with full backend functionality from product discovery through order placement, margin tracking, and direct WhatsApp integration.

## 🚀 Live Preview Links
- **Desktop / Local Browser:** [http://localhost:8000](http://localhost:8000)
- **Mobile / Local Wi-Fi Network:** [http://192.168.1.12:8000](http://192.168.1.12:8000)
- **Interactive API Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌟 Key Features

1. **Brand Identity & Uploaded Logo:**
   - Branded as **SAGA ONLINE SHOP** using the uploaded logo image.
   - Integrated into the header, favicon, receipt generator, and footer.

2. **DeoDap Dropshipping Business Model:**
   - Products are modeled on real **DeoDap** best-sellers and viral Instagram Reels gadgets across 5 categories:
     - Smart Kitchen & Appliances
     - Home & Organizers
     - Viral Tech Gadgets & Mobile Accessories
     - Beauty & Personal Care
     - Fitness & Car Accessories
   - Direct margin markup added to each product (e.g. DeoDap Wholesale ₹119 ➔ SAGA Selling ₹349 ➔ ₹230 Profit Margin).
   - DeoDap sourcing is hidden from regular customers, presenting SAGA as the direct brand.

3. **Merchant Dropship Mode (Owner Feature):**
   - Click the **"Merchant View: Dropship Margin"** toggle in the header to reveal:
     - DeoDap wholesale base cost vs SAGA selling price on every product card.
     - Net profit and margin percentage per product.
     - **"Profit Center"** modal tracking Gross Sales, DeoDap COGS, Total Net Profit, and 1-Click DeoDap Dispatch sync.

4. **Complete E-Commerce Flow Till Order Placement:**
   - Real-time catalog filtering, search, and sorting.
   - Interactive Product Quick-View modal with image gallery, specs, and Indian pincode delivery checker.
   - Slide-out Cart Drawer with item quantities, free shipping progress bar, and coupon codes (`SAGA10`, `WELCOME50`).
   - Express Checkout with customer shipping address (Full Name, Phone, Address, City, State, Pincode).
   - Payment Methods: **Cash on Delivery (COD)** and **Instant UPI / QR Payment**.
   - Order Confirmation screen generating a unique Order ID (`#SAGA-XXXXX`), invoice summary, and printable receipt.
   - Real-time Order Tracking lookup (`#SAGA-XXXXX`).

5. **WhatsApp Integration (+91 9922163722):**
   - Floating WhatsApp button with pulsing animation on all screens.
   - Header & Footer direct chat links.
   - Product page "Chat on WhatsApp about this item".
   - Post-order 1-click **"Send Order to WhatsApp"** button pre-formatting the complete order summary directly to `9922163722`.

---

## 🛠️ Tech Stack
- **Backend:** Python 3.12, FastAPI, Uvicorn, SQLite3, Pydantic
- **Frontend:** Responsive HTML5, Tailwind CSS, FontAwesome 6, Plus Jakarta Sans typography
- **Server:** Running as a daemon on `0.0.0.0:8000`
