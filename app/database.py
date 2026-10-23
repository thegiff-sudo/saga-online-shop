import sqlite3
import json
import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Detect Vercel serverless environment (writable /tmp)
if os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME"):
    DB_PATH = Path("/tmp/saga_store.db")
    orig_db = BASE_DIR / "saga_store.db"
    if not DB_PATH.exists() and orig_db.exists():
        shutil.copy(orig_db, DB_PATH)
else:
    DB_PATH = BASE_DIR / "saga_store.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # Products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        slug TEXT NOT NULL,
        category TEXT NOT NULL,
        deodap_sku TEXT NOT NULL,
        wholesale_price REAL NOT NULL,
        selling_price REAL NOT NULL,
        mrp REAL NOT NULL,
        stock INTEGER NOT NULL DEFAULT 50,
        rating REAL NOT NULL DEFAULT 4.7,
        review_count INTEGER NOT NULL DEFAULT 120,
        badge TEXT DEFAULT '',
        description TEXT NOT NULL,
        features_json TEXT NOT NULL DEFAULT '[]',
        image_url TEXT NOT NULL,
        gallery_json TEXT NOT NULL DEFAULT '[]',
        is_trending INTEGER NOT NULL DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Categories table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        slug TEXT NOT NULL UNIQUE,
        icon TEXT NOT NULL,
        image_url TEXT NOT NULL
    )
    """)

    # Orders table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id TEXT PRIMARY KEY,
        customer_name TEXT NOT NULL,
        customer_phone TEXT NOT NULL,
        customer_email TEXT,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        pincode TEXT NOT NULL,
        payment_method TEXT NOT NULL,
        payment_status TEXT NOT NULL DEFAULT 'Pending',
        subtotal REAL NOT NULL,
        discount REAL NOT NULL DEFAULT 0,
        shipping_fee REAL NOT NULL DEFAULT 0,
        total_amount REAL NOT NULL,
        total_wholesale_cost REAL NOT NULL DEFAULT 0,
        total_margin REAL NOT NULL DEFAULT 0,
        status TEXT NOT NULL DEFAULT 'Confirmed',
        items_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deodap_sync_status TEXT NOT NULL DEFAULT 'Ready to Dispatch',
        tracking_number TEXT DEFAULT ''
    )
    """)

    # Coupons table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS coupons (
        code TEXT PRIMARY KEY,
        discount_type TEXT NOT NULL,
        value REAL NOT NULL,
        min_order_value REAL NOT NULL DEFAULT 0,
        is_active INTEGER NOT NULL DEFAULT 1
    )
    """)

    conn.commit()
    conn.close()
