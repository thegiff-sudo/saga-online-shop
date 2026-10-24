import json
from .database import get_db

CATEGORIES = [
    {
        "id": "cat-all",
        "name": "All Products",
        "slug": "all",
        "icon": "fa-solid fa-border-all",
        "image_url": "/static/images/banners/showcase_3d_circular_podium.jpg"
    },
    {
        "id": "cat-desk-decor",
        "name": "Desk Decor & Divine",
        "slug": "desk-decor",
        "icon": "fa-solid fa-om",
        "image_url": "/static/images/products/shiva_3d_lamp_pooja.jpg"
    },
    {
        "id": "cat-bathroom",
        "name": "Bathroom Needs",
        "slug": "bathroom-needs",
        "icon": "fa-solid fa-bath",
        "image_url": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400&q=80"
    },
    {
        "id": "cat-home-needs",
        "name": "Home Needs & Daily",
        "slug": "home-needs",
        "icon": "fa-solid fa-house-chimney-window",
        "image_url": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=400&q=80"
    },
    {
        "id": "cat-kitchen",
        "name": "Smart Kitchen",
        "slug": "smart-kitchen",
        "icon": "fa-solid fa-kitchen-set",
        "image_url": "/static/images/products/portable_usb_blender_bottle.jpg"
    },
    {
        "id": "cat-apparel",
        "name": "Saga Apparel & Suits",
        "slug": "apparel-hoodies",
        "icon": "fa-solid fa-shirt",
        "image_url": "/static/images/products/saga_merino_wool_blazer_tag.jpg"
    },
    {
        "id": "cat-baby-kids",
        "name": "Baby & Kids",
        "slug": "baby-kids",
        "icon": "fa-solid fa-baby",
        "image_url": "/static/images/banners/banner_baby_home_diagonal.jpg"
    },
    {
        "id": "cat-car",
        "name": "Car Accessories",
        "slug": "car-accessories",
        "icon": "fa-solid fa-car-side",
        "image_url": "/static/images/banners/showcase_3d_circular_podium.jpg"
    },
    {
        "id": "cat-tech",
        "name": "Viral Gadgets & Tech",
        "slug": "viral-gadgets",
        "icon": "fa-solid fa-bolt",
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300&q=80"
    }
]

PRODUCTS = [
    # --- 1. USER UPLOADED 5 PRODUCTS ---
    {
        "id": "SAGA-DEC-001",
        "title": "Divine 3D Illusion Lord Shiva Ambient Night Lamp with Solid Beech Wood Base",
        "slug": "divine-3d-illusion-lord-shiva-lamp-wood-base",
        "category": "desk-decor",
        "deodap_sku": "DD-DECR-SHIV-3D1",
        "wholesale_price": 165.0,
        "selling_price": 499.0,
        "mrp": 1199.0,
        "stock": 120,
        "rating": 5.0,
        "review_count": 480,
        "badge": "Spiritual Bestseller 🕉️",
        "description": "Exquisitely etched circular acrylic plate illuminating a 3D hologram of Lord Shiva in deep meditation with Trishul and Damru. Emits a peaceful, soothing warm-golden aura resting on a solid natural beech wood base. Powered via USB cable for pooja rooms, office desks, and meditation corners.",
        "features": [
            "Laser-Etched Optical-Grade Acrylic with 3D Holographic Depth",
            "Natural Solid Beech Wood Base with Smooth Lacquered Finish",
            "Eye-Friendly Warm Golden Glow (Zero Glare)",
            "USB Powered - Connect to Phone Charger, Laptop or Power Bank",
            "Perfect for Pooja Mandir, Study Desk, Office & Devotional Gifting"
        ],
        "image_url": "/static/images/products/shiva_3d_lamp_pooja.jpg",
        "gallery": [
            "/static/images/products/shiva_3d_lamp_pooja.jpg",
            "/static/images/products/shiva_3d_lamp_desk.jpg"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-DEC-002",
        "title": "Lord Shiva Acrylic 3D Hologram Desk Lamp with USB Cable (Warm Glow Edition)",
        "slug": "lord-shiva-acrylic-3d-hologram-lamp-usb",
        "category": "desk-decor",
        "deodap_sku": "DD-DECR-SHIV-3D2",
        "wholesale_price": 165.0,
        "selling_price": 499.0,
        "mrp": 1199.0,
        "stock": 95,
        "rating": 4.9,
        "review_count": 315,
        "badge": "Divine Glow ✨",
        "description": "High-clarity optical grade laser-engraved Mahadev plate resting on an ergonomic wooden stand. Emits a soothing luminous warm glow perfect for nighttime reading, study desk motivation, and devotional gifting.",
        "features": [
            "High Clarity Circular 3D Holographic Display",
            "Solid Hardwood Stand with USB Power Interface",
            "Low Energy Consumption Long-Life LED Chips (50,000+ Hours)",
            "Calming Ambient Atmosphere for Desk or Bedroom",
            "Compact Dimensions: 17cm x 15cm"
        ],
        "image_url": "/static/images/products/shiva_3d_lamp_desk.jpg",
        "gallery": [
            "/static/images/products/shiva_3d_lamp_desk.jpg",
            "/static/images/products/shiva_3d_lamp_pooja.jpg"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-KTC-010",
        "title": "Portable USB Rechargeable Personal Smoothie & Protein Shaker Blender Bottle (500ml, Rose Gold)",
        "slug": "portable-usb-rechargeable-smoothie-blender-bottle-rosegold",
        "category": "smart-kitchen",
        "deodap_sku": "DD-KTC-BLND-PINK",
        "wholesale_price": 280.0,
        "selling_price": 699.0,
        "mrp": 1599.0,
        "stock": 140,
        "rating": 4.9,
        "review_count": 520,
        "badge": "Viral Blender 🍓",
        "description": "Powerful 6-blade 304 stainless steel personal blender bottle capable of crushing ice cubes, frozen berries, and protein shakes in 30 seconds. Features a leak-proof sipper lid with carry loop, measuring indicators, and USB-C fast charging.",
        "features": [
            "6 Ultra-Sharp 304 Stainless Steel Serrated Blades (22,000 RPM)",
            "BPA-Free Food-Grade PCTG Material with Clear Volume Markings",
            "Built-in 2400mAh Battery - Blends up to 15 Cups on Single USB Charge",
            "Magnetic Safety Induction Lock - Blades Won't Spin Unless Base is Locked",
            "Flip Top Drinking Spout with Silicone Finger Carry Strap"
        ],
        "image_url": "/static/images/products/portable_usb_blender_bottle.jpg",
        "gallery": [
            "/static/images/products/portable_usb_blender_bottle.jpg",
            "/static/images/products/portable_blender_lifestyle_model.jpg"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-KTC-011",
        "title": "4-Slot Cartoon Sailboat Ice Cream & Popsicle Mold with Drip-Guard Handles",
        "slug": "4-slot-cartoon-sailboat-popsicle-mold-drip-guard",
        "category": "home-needs",
        "deodap_sku": "DD-KTC-POPS-BOAT",
        "wholesale_price": 75.0,
        "selling_price": 249.0,
        "mrp": 599.0,
        "stock": 110,
        "rating": 4.8,
        "review_count": 210,
        "badge": "Kids Favourite 🍧",
        "description": "Fun sailboat-themed 4-compartment frozen treat maker. Features adorable animal character and helm handles with built-in drip guards to keep children's hands clean. Food-grade BPA-free silicone makes popping out frozen fruit pops effortless.",
        "features": [
            "100% Food-Grade BPA-Free Non-Toxic Material",
            "Integrated Drip Guards on Handles Prevent Sticky Fingers",
            "Easy Release Design - Run Warm Water for 3 Seconds to Release",
            "Make Fresh Fruit Puree, Yogurt Pops, Kulfi & Fruit Juice Ice Cream",
            "Dishwasher & Deep-Freezer Safe"
        ],
        "image_url": "/static/images/products/popsicle_icecream_mold_boat.jpg",
        "gallery": [
            "/static/images/products/popsicle_icecream_mold_boat.jpg"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-KTC-012",
        "title": "Fresh Juice To-Go Mini USB Electric Blender Cup with Silicone Hand Strap",
        "slug": "fresh-juice-to-go-mini-usb-electric-blender-cup",
        "category": "smart-kitchen",
        "deodap_sku": "DD-KTC-BLND-CUPO",
        "wholesale_price": 260.0,
        "selling_price": 649.0,
        "mrp": 1499.0,
        "stock": 85,
        "rating": 4.8,
        "review_count": 340,
        "badge": "Fitness Daily 🥤",
        "description": "Blend and drink directly from the bottle anywhere. Lightweight 450ml single-serve blender bottle ideal for office breakfast, gym pre-workout, and outdoor travel. One-touch power button with safety magnetic sensor lock.",
        "features": [
            "Direct-Drink Ergonomic Mouthpiece with Silicone Seal",
            "Single Button Operation - Double Click to Start",
            "Easy Self-Cleaning - Add Water & Soap, Press Button to Spin",
            "USB-C Universal Rechargeable (Works with Car Charger & Powerbank)",
            "Compact & Portable for Travel Bag"
        ],
        "image_url": "/static/images/products/portable_blender_lifestyle_model.jpg",
        "gallery": [
            "/static/images/products/portable_blender_lifestyle_model.jpg",
            "/static/images/products/portable_usb_blender_bottle.jpg"
        ],
        "is_trending": 1
    },

    # --- 2. BATHROOM NEEDS (DeoDap Direct Sourced) ---
    {
        "id": "SAGA-BATH-001",
        "title": "Wall-Mounted Automatic Toothpaste Dispenser with 4 Magnetic Mouthwash Cups",
        "slug": "wall-mounted-automatic-toothpaste-dispenser-magnetic-cups",
        "category": "bathroom-needs",
        "deodap_sku": "DD-BATH-DISP-4C",
        "wholesale_price": 165.0,
        "selling_price": 449.0,
        "mrp": 899.0,
        "stock": 75,
        "rating": 4.8,
        "review_count": 390,
        "badge": "Bathroom Upgrade 🚿",
        "description": "All-in-one family bathroom vanity organizer. Includes hands-free vacuum squeeze toothpaste dispenser, 4 inverted magnetic mouthwash cups that drain water rapidly to prevent bacteria, dustproof toothbrush slots, and top cosmetic storage tray.",
        "features": [
            "Automatic Hands-Free Squeeze Toothpaste Pump",
            "4 Inverted Magnetic Cups Drain Dust & Dry Instantly",
            "Enclosed Dustproof Rack Holds up to 5 Toothbrushes",
            "Top Storage Shelf for Shaving Cream, Face Wash & Perfumes",
            "Strong No-Drill Adhesive Strip Holds up to 6kg on Tiles"
        ],
        "image_url": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=600&q=80"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-BATH-002",
        "title": "Silicone Flex Flat Head Toilet Cleaning Brush with Quick-Drying Base",
        "slug": "silicone-flex-toilet-brush-quick-drying-base",
        "category": "bathroom-needs",
        "deodap_sku": "DD-BATH-BRSH-SIL",
        "wholesale_price": 85.0,
        "selling_price": 279.0,
        "mrp": 599.0,
        "stock": 130,
        "rating": 4.7,
        "review_count": 270,
        "badge": "Hygienic Clean 🧼",
        "description": "Bendable D-shaped TPR silicone bristle brush that reaches under rim dead corners easily without scratching toilet glaze. Hair and dirt rinse off immediately with water, and the hollow suspended holder evaporates water without dripping on the floor.",
        "features": [
            "Flexible TPR Silicone Head Bends to Clean Under-Rim Corners",
            "Non-Sticky Bristles - Hair & Debris Wash Off Instantly",
            "Wall-Mount or Floor-Standing Ventilated Holder",
            "Drip-Proof Base Prevents Stagnant Dirty Water Odors",
            "Rustproof Stainless Steel & Ergonomic Grip Handle"
        ],
        "image_url": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=600&q=80"
        ],
        "is_trending": 0
    },
    {
        "id": "SAGA-BATH-003",
        "title": "Super Absorbent Quick-Dry Diatomite Anti-Slip Bathroom Floor Mat",
        "slug": "super-absorbent-quick-dry-diatomite-bathroom-mat",
        "category": "bathroom-needs",
        "deodap_sku": "DD-BATH-MAT-DIAT",
        "wholesale_price": 110.0,
        "selling_price": 329.0,
        "mrp": 699.0,
        "stock": 160,
        "rating": 4.8,
        "review_count": 415,
        "badge": "Magic Dry ✨",
        "description": "Revolutionary 4-layer diatomaceous earth composite mat that sucks water off wet feet within 3 seconds and dries rapidly. Textured rubber bottom grips tile floors firmly to prevent slips and falls.",
        "features": [
            "Instant 3-Second Water Absorption Technology",
            "Natural Breathable Diatom Mud Core Prevents Mold & Odors",
            "Anti-Slip Heavy Duty Natural Rubber Gripper Backing",
            "Ultra-Thin Sleek Design Never Jams Under Bathroom Doors",
            "Easy Wipe Clean with Damp Sponge or Shower Rinse"
        ],
        "image_url": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=600&q=80"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-BATH-004",
        "title": "360° Rotating Turbo Propeller High-Pressure Shower Head with PP Cotton Filter",
        "slug": "turbo-propeller-high-pressure-shower-head-filter",
        "category": "bathroom-needs",
        "deodap_sku": "DD-BATH-SHWR-TRB",
        "wholesale_price": 145.0,
        "selling_price": 399.0,
        "mrp": 899.0,
        "stock": 90,
        "rating": 4.6,
        "review_count": 230,
        "badge": "Spa Pressure 🚿",
        "description": "Increases water pressure by up to 200% while cutting water consumption by 40% using an internal turbo fan. Features micro-nozzle stainless steel plate, one-touch on/off switch, and replaceable multi-layer PP filter cartridge to trap rust and chlorine.",
        "features": [
            "Hydro-Propeller Boosts Water Pressure by 200%",
            "Built-in Replaceable Micron PP Cotton Water Filter",
            "One-Key Instant Water Pause Button on Handle",
            "Universal G1/2 Thread Fits Any Standard Shower Hose",
            "360° Free Rotating Swivel Ball Joint"
        ],
        "image_url": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=600&q=80"
        ],
        "is_trending": 0
    },

    # --- 3. HOME NEEDS & DAILY ITEMS (DeoDap Direct Sourced) ---
    {
        "id": "SAGA-HOME-001",
        "title": "Wireless Electric Automatic Water Dispenser Pump for 20L Cans (USB Rechargeable)",
        "slug": "wireless-electric-water-dispenser-pump-20l",
        "category": "home-needs",
        "deodap_sku": "DD-HOME-WTR-PUMP",
        "wholesale_price": 129.0,
        "selling_price": 379.0,
        "mrp": 799.0,
        "stock": 180,
        "rating": 4.8,
        "review_count": 620,
        "badge": "Daily Essential 💧",
        "description": "Never lift heavy 20-litre water jars again! One-touch automatic suction pump dispenses clean drinking water effortlessly. Fits all standard 20L, 15L, and 10L water cans with food-grade silicone intake tube and 304 stainless steel spout.",
        "features": [
            "One-Touch Automatic Water Pumping with LED Indicator",
            "Food-Grade Odorless Silicone Suction Tube & 304 Steel Outlet",
            "Fast 1200mAh USB Rechargeable Battery - Pumps 6-8 Full 20L Jars per Charge",
            "Zero Installation - Place Right on Top of Standard Bottle Neck",
            "Compact, Portable for Home, Kitchen, Office & Camping"
        ],
        "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=600&q=80"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-HOME-002",
        "title": "Stainless Steel Wall-Mounted Self-Adhesive Mop & Broom Organizer Gripper (Pack of 3)",
        "slug": "stainless-steel-mop-broom-organizer-gripper-3pack",
        "category": "home-needs",
        "deodap_sku": "DD-HOME-MOP-CLP",
        "wholesale_price": 75.0,
        "selling_price": 229.0,
        "mrp": 499.0,
        "stock": 140,
        "rating": 4.7,
        "review_count": 280,
        "badge": "Neat & Tidy 🧹",
        "description": "Clears cluttered kitchen and balcony corners. Spring-loaded silicone rollers grip brooms, mops, wipers, umbrellas, and dusters securely without slipping. Heavy-duty 304 stainless steel backplate with ultra-strong trace-less adhesive.",
        "features": [
            "304 Rustproof Heavy-Duty Stainless Steel Backing",
            "Corrugated Silicone Anti-Slip Roller Grips Any Handle Diameter",
            "Holds up to 5kg Without Drilling or Nailing Walls",
            "Waterproof & Oil-Proof - Perfect for Bathrooms & Kitchens",
            "Pack of 3 Grippers"
        ],
        "image_url": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=600&q=80"
        ],
        "is_trending": 0
    },
    {
        "id": "SAGA-HOME-003",
        "title": "Rechargeable Fabric Shaver & Electric Lint Remover for Sweaters, Blankets & Sofas",
        "slug": "rechargeable-fabric-shaver-electric-lint-remover",
        "category": "home-needs",
        "deodap_sku": "DD-HOME-LINT-REM",
        "wholesale_price": 155.0,
        "selling_price": 429.0,
        "mrp": 899.0,
        "stock": 105,
        "rating": 4.8,
        "review_count": 340,
        "badge": "Like New Again ✨",
        "description": "Restores pilled woollen sweaters, coats, joggers, couches, and thermal blankets in seconds. 6-leaf stainless steel precision blades rotate at 8000 RPM behind a smooth bionic honeycomb mesh cover that protects fabrics from cuts.",
        "features": [
            "6-Blade High-Speed Rotary Cutter with Suction Fan",
            "Bionic Honeycomb Foil Net Protects Delicate Fabrics",
            "Large Detachable Transparent Fuzz Collection Container",
            "USB Rechargeable with Safety Lock When Mesh is Loose",
            "Ideal for Sweaters, Woollens, Sofas, Bedsheets & Curtains"
        ],
        "image_url": "https://images.unsplash.com/photo-1582735689369-4fe89db7114c?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1582735689369-4fe89db7114c?w=600&q=80"
        ],
        "is_trending": 1
    },

    # --- 4. MORE DESK DECOR (DeoDap Direct Sourced) ---
    {
        "id": "SAGA-DEC-003",
        "title": "Smoke Waterfall Ceramic Backflow Incense Cone Burner with 30 Scented Cones",
        "slug": "smoke-waterfall-ceramic-backflow-incense-burner",
        "category": "desk-decor",
        "deodap_sku": "DD-DECR-BCK-FLW",
        "wholesale_price": 125.0,
        "selling_price": 349.0,
        "mrp": 799.0,
        "stock": 90,
        "rating": 4.8,
        "review_count": 310,
        "badge": "Aromatherapy 🪔",
        "description": "Mesmerizing smoky cascade designed to purify air, relieve stress, and enhance meditation. Dense smoke cascades down rockery layers like a mystical mountain waterfall. Handcrafted glazed ceramic with 30 natural aromatic incense cones included.",
        "features": [
            "Handcrafted Glazed Ceramic Artwork with Mountain Rockery Tier",
            "Mesmerizing Downward Smoke Waterfall Visual Effect",
            "Includes 30 Free Assorted Natural Essential Oil Cones",
            "Relieves Mental Stress & Enhances Yoga, Study & Sleep",
            "Stain-Resistant Surface - Rinses Clean with Hot Water"
        ],
        "image_url": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=600&q=80"
        ],
        "is_trending": 0
    },
    {
        "id": "SAGA-DEC-004",
        "title": "3D Moon Desk Lamp with Touch Sensor & 16 RGB Remote Control Colors (Wooden Stand)",
        "slug": "3d-moon-desk-lamp-touch-sensor-rgb-remote",
        "category": "desk-decor",
        "deodap_sku": "DD-DECR-MOON-16C",
        "wholesale_price": 240.0,
        "selling_price": 599.0,
        "mrp": 1299.0,
        "stock": 80,
        "rating": 4.9,
        "review_count": 425,
        "badge": "Night Companion 🌙",
        "description": "High-accuracy 3D printed lunar surface based on NASA satellite topography. Switch between 16 soothing ambient color hues and 4 light modes via touch metal ring or included wireless remote control.",
        "features": [
            "Ultra-Realistic 3D Printed Lunar Topography Surface",
            "16 Dynamic RGB Colors with Dimmable Brightness",
            "Dual Control: Sensitive Touch Ring & Remote Control",
            "USB Rechargeable Lithium Battery with Warm Wooden Tripod Base",
            "Romantic Ambient Light for Study Desks & Bedside Tables"
        ],
        "image_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600&q=80"
        ],
        "is_trending": 1
    },

    # --- 5. SAGA OFFICIAL BRAND SIGNATURE APPAREL (Uploaded by User) ---
    {
        "id": "SAGA-OG-001",
        "title": "Saga Fine Men's Outfitters 100% Merino Wool Tailored Blazer",
        "slug": "saga-fine-mens-outfitters-100-merino-wool-tailored-blazer",
        "category": "apparel-hoodies",
        "deodap_sku": "DD-SAGA-BLAZ-WOOL",
        "wholesale_price": 899.0,
        "selling_price": 1999.0,
        "mrp": 4499.0,
        "stock": 40,
        "rating": 4.9,
        "review_count": 185,
        "badge": "Saga Signature 🏷️",
        "description": "Exquisite Italian cut tailored suit jacket crafted from 100% superfine Australian Merino wool. Features embossed gold 'Saga Store - Fine Men's Outfitters' signature label, hand-finished peak lapels, horn buttons, and breathable silk-blend interior lining.",
        "features": [
            "100% Superfine Australian Merino Wool",
            "Signature Embossed Gold 'Saga Store - Fine Men's Outfitters' Tag",
            "Hand-Tailored Structured Shoulders & Notched Lapel",
            "Breathable Silk-Blend Luxury Interior Lining",
            "Includes Saga Garment Cover & Wooden Suit Hanger"
        ],
        "image_url": "/static/images/products/saga_merino_wool_blazer_tag.jpg",
        "gallery": [
            "/static/images/products/saga_merino_wool_blazer_tag.jpg",
            "/static/images/products/saga_luxury_suit_box_set.jpg"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-OG-002",
        "title": "Saga Luxury Suiting Gift Box Set (Tailored Blazer + Trousers + Signature Bag)",
        "slug": "saga-luxury-suiting-gift-box-set",
        "category": "apparel-hoodies",
        "deodap_sku": "DD-SAGA-SUIT-SET",
        "wholesale_price": 1299.0,
        "selling_price": 2799.0,
        "mrp": 5999.0,
        "stock": 35,
        "rating": 5.0,
        "review_count": 94,
        "badge": "Luxury Gift Box 🎁",
        "description": "The complete luxury gentleman's ensemble presented in a premium rigid gift presentation box with gold-foil Saga Store branding. Includes precision-tailored charcoal wool blazer, matching flat-front trousers, leather belt, pocket square, and Saga gold-stamped luxury carry bag.",
        "features": [
            "Complete 3-Piece Gentleman's Luxury Set in Rigid Gift Box",
            "Woven Gold 'Saga Store' Neck & Pocket Interior Labels",
            "Matching Flat-Front Trousers with Adjustable Waistband",
            "Includes Premium Saga Gold-Foil Rope Shopping Bag",
            "Perfect for Weddings, Executive Meetings & Black-Tie Galas"
        ],
        "image_url": "/static/images/products/saga_luxury_suit_box_set.jpg",
        "gallery": [
            "/static/images/products/saga_luxury_suit_box_set.jpg",
            "/static/images/products/saga_merino_wool_blazer_tag.jpg"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-OG-003",
        "title": "Saga Gold-Embroidered Sage Green Heavyweight Streetwear Hoodie",
        "slug": "saga-gold-embroidered-sage-green-hoodie",
        "category": "apparel-hoodies",
        "deodap_sku": "DD-SAGA-HOOD-SAGE",
        "wholesale_price": 450.0,
        "selling_price": 999.0,
        "mrp": 2299.0,
        "stock": 90,
        "rating": 4.9,
        "review_count": 410,
        "badge": "Brand Icon 🔥",
        "description": "Our iconic brand staple. 420 GSM ultra-heavyweight combed French Terry cotton in aesthetic sage green with high-density metallic gold thread 'Saga' script chest embroidery. Finished with custom Saga Store embossed hangtag, double-walled hood, and brass hardware.",
        "features": [
            "420 GSM Ultra-Heavy Combed French Terry Cotton",
            "High-Density 3D Metallic Gold Thread Chest Embroidery",
            "Custom Saga Store Premium Tag with Golden Cord",
            "Double-Layer Thermal Hood with Brass Metal Aglets",
            "Relaxed Drop-Shoulder Silhouette & Kangaroo Pocket"
        ],
        "image_url": "/static/images/products/saga_gold_embroidered_sage_hoodie.jpg",
        "gallery": [
            "/static/images/products/saga_gold_embroidered_sage_hoodie.jpg",
            "/static/images/banners/showcase_3d_circular_podium.jpg"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-OG-004",
        "title": "Saga Winter Thermal Sherpa-Lined Heavy Fleece Hoodie (Beige Sand)",
        "slug": "saga-winter-thermal-sherpa-lined-hoodie-beige",
        "category": "apparel-hoodies",
        "deodap_sku": "DD-SAGA-SHRP-HOOD",
        "wholesale_price": 520.0,
        "selling_price": 1199.0,
        "mrp": 2699.0,
        "stock": 65,
        "rating": 4.8,
        "review_count": 320,
        "badge": "Winter Warmth ❄️",
        "description": "Engineered for harsh winter chills. Heavyweight brushed cotton-poly fleece outer shell insulated with an ultra-soft, cloud-like sherpa fleece inner lining throughout the body and hood. Features chest embroidered Saga script, dual-tone drawstrings, and deep kangaroo warming pockets.",
        "features": [
            "Plush Cloud-Soft Sherpa Fleece Thermal Body & Hood Lining",
            "Subtle Gold Embroidered 'Saga' Script on Chest",
            "Heavy-Duty Dual-Tone Contrast Thermal Drawstrings",
            "Windproof Ribbed Ankle Cuffs & Waistband",
            "Deep Sherpa-Lined Hand-Warmer Kangaroo Pocket"
        ],
        "image_url": "/static/images/products/saga_sherpa_fleece_winter_hoodie.jpg",
        "gallery": [
            "/static/images/products/saga_sherpa_fleece_winter_hoodie.jpg",
            "/static/images/products/saga_gold_embroidered_sage_hoodie.jpg"
        ],
        "is_trending": 1
    },

    # --- 6. BABY & KIDS ---
    {
        "id": "SAGA-KID-001",
        "title": "Baby Ergonomic Silicone Suction Bowl & Spoon Feeding Set (BPA-Free)",
        "slug": "baby-ergonomic-silicone-suction-bowl-spoon-set",
        "category": "baby-kids",
        "deodap_sku": "DD-KID-BOWL-SET",
        "wholesale_price": 120.0,
        "selling_price": 349.0,
        "mrp": 799.0,
        "stock": 110,
        "rating": 4.9,
        "review_count": 245,
        "badge": "Mom's Choice ⭐",
        "description": "Premium 100% food-grade platinum silicone suction bowl with matching soft-tip spoon. Features powerful non-slip suction base that sticks firmly to high chairs, preventing spills, throws, and mess during self-feeding training.",
        "features": [
            "100% BPA, PVC, Phthalate & Lead-Free Platinum Silicone",
            "Super Strong Suction Base - Prevents High-Chair Spills",
            "Gentle Soft-Tip Gum-Friendly Training Spoon",
            "Microwave, Dishwasher, Freezer & Boil-Water Safe",
            "Ergonomic Curved Lip for Easy Food Scooping"
        ],
        "image_url": "https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?w=600&q=80",
        "gallery": [
            "/static/images/banners/banner_baby_home_diagonal.jpg"
        ],
        "is_trending": 0
    },
    {
        "id": "SAGA-KID-002",
        "title": "Ultra-Soft Plush Elephant Baby Cuddle Pillow & Sleep Companion",
        "slug": "ultra-soft-plush-elephant-baby-cuddle-pillow",
        "category": "baby-kids",
        "deodap_sku": "DD-KID-ELEPH-PLSH",
        "wholesale_price": 140.0,
        "selling_price": 399.0,
        "mrp": 899.0,
        "stock": 85,
        "rating": 4.8,
        "review_count": 310,
        "badge": "Top Gift Pick 🎁",
        "description": "Incredibly huggable, velvety-soft plush elephant companion. Stuffed with hypoallergenic PP cotton for calming, comforting sleep. Perfect decorative addition for baby nursery and toddler playtime.",
        "features": [
            "Hypoallergenic Ultra-Soft Velveteen Fabric",
            "Embroidered Safe Baby Eyes - Zero Choking Hazard",
            "Machine Washable on Gentle Cycle",
            "Calming Hug Pillow for Peaceful Sleep",
            "Dimensions: 30cm - Ideal for Tiny Arms to Hug"
        ],
        "image_url": "https://images.unsplash.com/photo-1559454403-b8fb88521f11?w=600&q=80",
        "gallery": [
            "/static/images/banners/banner_baby_home_diagonal.jpg"
        ],
        "is_trending": 0
    },

    # --- 7. CAR ACCESSORIES ---
    {
        "id": "SAGA-CAR-001",
        "title": "360° Magnetic Rotatable Car Air Vent Phone Mount Holder",
        "slug": "360-magnetic-rotatable-car-air-vent-mount",
        "category": "car-accessories",
        "deodap_sku": "DD-CAR-MAGN-MNT",
        "wholesale_price": 95.0,
        "selling_price": 299.0,
        "mrp": 699.0,
        "stock": 130,
        "rating": 4.8,
        "review_count": 360,
        "badge": "Driver Essential 🚗",
        "description": "Equipped with 6 ultra-strong N52 neodymium magnets that securely hold any smartphone even over bumpy speed breakers and sharp turns. Silicone-cushioned steel hook twist-locks firmly onto all AC vent blades without scratching.",
        "features": [
            "6 Strong N52 Neodymium Magnets - Holds Up to 2.5kg",
            "Upgraded Twist-Lock Vent Hook - Zero Sagging or Falling",
            "Full 360° Swivel Ball Joint for Landscape GPS & Portrait Calls",
            "One-Hand Instant Magnetic Snap and Release",
            "Compatible with iPhone MagSafe & All Android Devices"
        ],
        "image_url": "https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?w=600&q=80",
        "gallery": [
            "/static/images/banners/showcase_3d_circular_podium.jpg"
        ],
        "is_trending": 0
    },

    # --- 8. VIRAL TECH & GADGETS ---
    {
        "id": "SAGA-TEC-001",
        "title": "4-in-1 Fast Wireless Charger with RGB Ambient Lamp & Bluetooth Speaker",
        "slug": "4-in-1-fast-wireless-charger-rgb-speaker",
        "category": "viral-gadgets",
        "deodap_sku": "DD-TEC-CHRG-4IN1",
        "wholesale_price": 499.0,
        "selling_price": 1299.0,
        "mrp": 2999.0,
        "stock": 40,
        "rating": 4.8,
        "review_count": 412,
        "badge": "G-Shape Viral Lamp 🎵",
        "description": "The viral all-in-one bedside table centerpiece. Features 15W Qi fast wireless charging for iPhone and Android, high-fidelity Bluetooth 5.2 speaker, 256 RGB dynamic ambient light modes synced to your music, and digital alarm clock.",
        "features": [
            "15W Qi-Certified Fast Wireless Charging Pad",
            "High-Bass Bluetooth 5.2 Surround Sound Speaker",
            "256 RGB Light Modes Sync to Music Beats",
            "Digital Clock with Gentle Sunrise Alarm Setting",
            "USB-C Powered with Built-in Auxiliary & TF Card Slot"
        ],
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&q=80"
        ],
        "is_trending": 0
    }
]

COUPONS = [
    {
        "code": "SAGA10",
        "discount_type": "percent",
        "value": 10.0,
        "min_order_value": 299.0,
        "is_active": 1
    },
    {
        "code": "WELCOME50",
        "discount_type": "fixed",
        "value": 50.0,
        "min_order_value": 399.0,
        "is_active": 1
    },
    {
        "code": "FREESHIP",
        "discount_type": "fixed",
        "value": 49.0,
        "min_order_value": 499.0,
        "is_active": 1
    }
]

def seed_database():
    conn = get_db()
    cursor = conn.cursor()

    # Clear and insert categories
    cursor.execute("DELETE FROM categories")
    for cat in CATEGORIES:
        cursor.execute(
            "INSERT INTO categories (id, name, slug, icon, image_url) VALUES (?, ?, ?, ?, ?)",
            (cat["id"], cat["name"], cat["slug"], cat["icon"], cat["image_url"])
        )

    # Clear and insert products
    cursor.execute("DELETE FROM products")
    for prod in PRODUCTS:
        cursor.execute("""
        INSERT INTO products (
            id, title, slug, category, deodap_sku, wholesale_price, selling_price,
            mrp, stock, rating, review_count, badge, description, features_json,
            image_url, gallery_json, is_trending
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            prod["id"], prod["title"], prod["slug"], prod["category"], prod["deodap_sku"],
            prod["wholesale_price"], prod["selling_price"], prod["mrp"], prod["stock"],
            prod["rating"], prod["review_count"], prod["badge"], prod["description"],
            json.dumps(prod["features"]), prod["image_url"], json.dumps(prod["gallery"]),
            prod["is_trending"]
        ))

    # Clear and insert coupons
    cursor.execute("DELETE FROM coupons")
    for cp in COUPONS:
        cursor.execute(
            "INSERT INTO coupons (code, discount_type, value, min_order_value, is_active) VALUES (?, ?, ?, ?, ?)",
            (cp["code"], cp["discount_type"], cp["value"], cp["min_order_value"], cp["is_active"])
        )

    conn.commit()
    conn.close()
    print("Database re-seeded successfully with 5 user products, bathroom needs, home needs & desk decor!")

if __name__ == "__main__":
    from .database import init_db
    init_db()
    seed_database()
