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
        "id": "cat-baby-kids",
        "name": "Baby & Kids",
        "slug": "baby-kids",
        "icon": "fa-solid fa-baby",
        "image_url": "/static/images/banners/banner_baby_home_diagonal.jpg"
    },
    {
        "id": "cat-kitchen",
        "name": "Home & Kitchen",
        "slug": "smart-kitchen",
        "icon": "fa-solid fa-kitchen-set",
        "image_url": "/static/images/banners/banner_3tier_essentials.jpg"
    },
    {
        "id": "cat-apparel",
        "name": "Hoodies & Apparel",
        "slug": "apparel-hoodies",
        "icon": "fa-solid fa-shirt",
        "image_url": "/static/images/banners/banner_luxury_departments.jpg"
    },
    {
        "id": "cat-car",
        "name": "Car Accessories",
        "slug": "car-accessories",
        "icon": "fa-solid fa-car-side",
        "image_url": "/static/images/banners/showcase_3d_circular_podium.jpg"
    },
    {
        "id": "cat-fitness",
        "name": "Fitness & Gym",
        "slug": "fitness-care",
        "icon": "fa-solid fa-dumbbell",
        "image_url": "/static/images/banners/banner_3tier_essentials.jpg"
    },
    {
        "id": "cat-tech",
        "name": "Viral Gadgets & Tech",
        "slug": "viral-gadgets",
        "icon": "fa-solid fa-bolt",
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300&q=80"
    },
    {
        "id": "cat-beauty",
        "name": "Beauty & Personal Care",
        "slug": "beauty-care",
        "icon": "fa-solid fa-wand-magic-sparkles",
        "image_url": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=300&q=80"
    }
]

PRODUCTS = [
    # --- Official SAGA Brand Signature Products (Uploaded by User) ---
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
    # --- Baby & Kids (From Saga Uploaded Banners) ---
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
            "Microwave, Dishwasher, Freezer & Boil-Water Safe (-40°C to 220°C)",
            "Ergonomic Curved Lip for Easy Food Scooping"
        ],
        "image_url": "https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?w=600&q=80",
        "gallery": [
            "/static/images/banners/banner_baby_home_diagonal.jpg",
            "/static/images/banners/banner_3tier_essentials.jpg"
        ],
        "is_trending": 1
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
        "is_trending": 1
    },
    {
        "id": "SAGA-KID-003",
        "title": "Montessori Educational Wooden Alphabet & Building Blocks Puzzle",
        "slug": "montessori-educational-wooden-building-blocks",
        "category": "baby-kids",
        "deodap_sku": "DD-KID-WOOD-BLKS",
        "wholesale_price": 160.0,
        "selling_price": 449.0,
        "mrp": 999.0,
        "stock": 70,
        "rating": 4.7,
        "review_count": 180,
        "badge": "Brain Booster 🧠",
        "description": "Inspire creative thinking, spatial awareness, and motor coordination with this smooth natural hardwood block puzzle set. Coated with non-toxic, child-safe organic water-based paints.",
        "features": [
            "Handcrafted Natural Beech Wood with Rounded Safe Edges",
            "Eco-Friendly Non-Toxic Water-Based Paints",
            "Develops Fine Motor Skills & Color Recognition",
            "Includes Wooden Storage Tray with Pattern Guide",
            "Ideal for Ages 1 to 5 Years Old"
        ],
        "image_url": "https://images.unsplash.com/photo-1587654780291-39c9404d746b?w=600&q=80",
        "gallery": [
            "/static/images/banners/banner_welcome_story.jpg"
        ],
        "is_trending": 0
    },

    # --- Home & Kitchen (From Saga Uploaded Banners) ---
    {
        "id": "SAGA-HOM-007",
        "title": "Vintage Rose Copper Whistling Stove-Top Tea Kettle (2.5L)",
        "slug": "vintage-rose-copper-whistling-tea-kettle-2-5l",
        "category": "smart-kitchen",
        "deodap_sku": "DD-KTC-COPP-KTL",
        "wholesale_price": 380.0,
        "selling_price": 899.0,
        "mrp": 1999.0,
        "stock": 45,
        "rating": 4.9,
        "review_count": 275,
        "badge": "Luxury Home 🌟",
        "description": "Stunning metallic rose-copper finish whistling kettle that elevates your kitchen countertop. Made of food-grade 304 stainless steel with encapsulated 5-layer thermal base for lightning-fast, even water boiling. Loud melodic whistle alerts you when ready.",
        "features": [
            "Food-Grade 304 Stainless Steel with Rose Copper Mirror Finish",
            "Capsulated Thermal Induction Base - Boils Water in Minutes",
            "Ergonomic Heat-Resistant Stay-Cool Wood-Grain Handle",
            "Audible Whistle Automatically Alerts When Water Reaches Boil",
            "Compatible with Induction, Gas, Electric & Ceramic Cooktops"
        ],
        "image_url": "https://images.unsplash.com/photo-1544233726-9f1d2b27be8b?w=600&q=80",
        "gallery": [
            "/static/images/banners/banner_3tier_essentials.jpg",
            "/static/images/banners/banner_baby_home_diagonal.jpg"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-HOM-008",
        "title": "Airtight Matte Black Kitchen Canister Tins with Bamboo Lids (Set of 3)",
        "slug": "airtight-matte-black-kitchen-canister-tins",
        "category": "smart-kitchen",
        "deodap_sku": "DD-KTC-CAN-3SET",
        "wholesale_price": 220.0,
        "selling_price": 599.0,
        "mrp": 1299.0,
        "stock": 60,
        "rating": 4.8,
        "review_count": 195,
        "badge": "Kitchen Organizer",
        "description": "Minimalist Scandinavian design tea, coffee, and sugar storage containers. Durable carbon steel construction with natural airtight silicone-sealed bamboo lids to keep pantry essentials fresh, dry, and moisture-free.",
        "features": [
            "Airtight Food-Grade Silicone Seal Keeps Moisture Out",
            "Natural Eco Bamboo Lids with Matte Powder-Coated Metal",
            "Rust-Proof, Dent-Resistant & Easy Wipe Clean",
            "Set of 3 Matching Canisters for Tea, Coffee, Sugar & Spices",
            "Modern Farmhouse Aesthetic for Countertop Display"
        ],
        "image_url": "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=600&q=80",
        "gallery": [
            "/static/images/banners/banner_3tier_essentials.jpg"
        ],
        "is_trending": 0
    },

    # --- Hoodies & Apparel (From Saga Uploaded Banners) ---
    {
        "id": "SAGA-APP-001",
        "title": "Premium Heavyweight Oversized Unisex Fleece Hoodie (Charcoal Heather)",
        "slug": "premium-heavyweight-oversized-unisex-fleece-hoodie",
        "category": "apparel-hoodies",
        "deodap_sku": "DD-APP-HOOD-OVR",
        "wholesale_price": 399.0,
        "selling_price": 899.0,
        "mrp": 1999.0,
        "stock": 75,
        "rating": 4.8,
        "review_count": 420,
        "badge": "Streetwear Hot 🔥",
        "description": "Crafted from 380 GSM ultra-dense combed cotton-poly fleece. Features double-layered hood with metallic eyelets, drop-shoulder oversized aesthetic, spacious kangaroo pouch pocket, and ribbed cuffs that maintain their shape wash after wash.",
        "features": [
            "380 GSM Heavyweight Brushed Cotton Interior",
            "Oversized Drop-Shoulder Relaxed Streetwear Fit",
            "Double-Layered Hood with Premium Drawstrings",
            "Pre-Shrunk Bio-Washed Fabric - Zero Color Bleeding",
            "Kangaroo Pocket with Reinforced Stitching"
        ],
        "image_url": "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?w=600&q=80",
        "gallery": [
            "/static/images/banners/showcase_3d_circular_podium.jpg",
            "/static/images/banners/banner_luxury_departments.jpg"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-APP-002",
        "title": "Relaxed Fit Cotton Cargo Jogger Pants with Drawstring (Khaki & Olive)",
        "slug": "relaxed-fit-cotton-cargo-jogger-pants",
        "category": "apparel-hoodies",
        "deodap_sku": "DD-APP-CRGO-PNT",
        "wholesale_price": 340.0,
        "selling_price": 799.0,
        "mrp": 1699.0,
        "stock": 65,
        "rating": 4.7,
        "review_count": 280,
        "badge": "Everyday Comfort",
        "description": "Versatile all-day wear cargo trousers tailored with 98% breathable cotton twill and 2% elastane for maximum stretch and mobility. Features 6 deep functional pockets, elastic waistband, and tapered ankle cuffs.",
        "features": [
            "98% Breathable Cotton Twill + 2% Spandex Stretch",
            "6 Deep Utility Pockets Including Side Snap Flaps",
            "Elastic Drawstring Waistband for Custom Fit",
            "Reinforced Knee Seams for Maximum Durability",
            "Tapered Ankle Rib Cuffs - Pairs Perfectly with Sneakers"
        ],
        "image_url": "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=600&q=80",
        "gallery": [
            "/static/images/banners/showcase_3d_circular_podium.jpg"
        ],
        "is_trending": 1
    },

    # --- Car Accessories (From Saga Uploaded Banners) ---
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
            "/static/images/banners/showcase_3d_circular_podium.jpg",
            "/static/images/banners/banner_luxury_departments.jpg"
        ],
        "is_trending": 1
    },

    # --- Fitness & Gym (From Saga Uploaded Banners) ---
    {
        "id": "SAGA-FIT-005",
        "title": "Eco-Friendly Non-Slip Dual Texture Yoga & Workout Mat (6mm)",
        "slug": "eco-friendly-non-slip-yoga-workout-mat-6mm",
        "category": "fitness-care",
        "deodap_sku": "DD-FIT-YOGA-6MM",
        "wholesale_price": 260.0,
        "selling_price": 699.0,
        "mrp": 1499.0,
        "stock": 70,
        "rating": 4.8,
        "review_count": 290,
        "badge": "Gym & Yoga 🧘",
        "description": "High-density TPE dual-layer exercise mat with laser-engraved posture alignment lines. 6mm thick cushioning protects knees, wrists, and spine during intense yoga, pilates, and floor workouts.",
        "features": [
            "Laser-Etched Body Alignment System Guides Perfect Poses",
            "Dual-Side Non-Slip Texture Grips Wood, Tile & Marble Floors",
            "High-Density 6mm TPE Foam Absorbs Joint Impact",
            "100% Non-Toxic, Odor-Free & Sweat-Resistant",
            "Includes Free Carrying Strap & Breathable Mesh Bag"
        ],
        "image_url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600&q=80",
        "gallery": [
            "/static/images/banners/banner_3tier_essentials.jpg"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-FIT-006",
        "title": "Insulated Stainless Steel Gym Protein Shaker Bottle (750ml)",
        "slug": "insulated-stainless-steel-gym-protein-shaker-750ml",
        "category": "fitness-care",
        "deodap_sku": "DD-FIT-SHKR-750",
        "wholesale_price": 180.0,
        "selling_price": 479.0,
        "mrp": 999.0,
        "stock": 90,
        "rating": 4.7,
        "review_count": 210,
        "badge": "Lump-Free Mix ⚡",
        "description": "Never smell foul plastic shaker odor again. Made of premium food-grade 304 stainless steel with built-in silent blending whisk. Keeps protein shakes chilled for 24 hours without condensation.",
        "features": [
            "Food-Grade 304 Stainless Steel - 100% Odor Resistant",
            "Double-Wall Vacuum Insulation Keeps Cold for 24 Hours",
            "Leak-Proof Flip Cap with Protective Spout Cover",
            "Built-in Surgical Stainless Whisk for Smooth Shakes",
            "Embossed Measurement Markings (ml & oz) Inside"
        ],
        "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600&q=80",
        "gallery": [
            "/static/images/banners/banner_3tier_essentials.jpg"
        ],
        "is_trending": 0
    },

    # --- Smart Kitchen Original DeoDap Catalog ---
    {
        "id": "SAGA-KTC-001",
        "title": "Electric USB Mini Vegetable & Garlic Chopper (250ml)",
        "slug": "electric-usb-mini-vegetable-garlic-chopper",
        "category": "smart-kitchen",
        "deodap_sku": "DD-KTC-CHOP-250",
        "wholesale_price": 119.0,
        "selling_price": 349.0,
        "mrp": 799.0,
        "stock": 85,
        "rating": 4.8,
        "review_count": 342,
        "badge": "Viral on Reels 🔥",
        "description": "High-speed electric mini chopper equipped with 3 food-grade stainless steel blades. Chops garlic, ginger, onions, chilies, peanuts, and vegetables in under 10 seconds with a single push button. USB rechargeable with long battery life.",
        "features": [
            "Food-Grade 304 Stainless Steel Blades",
            "One-Touch Electric Operation with Safety Lock",
            "Compact 250ml BPA-Free Bowl",
            "USB Rechargeable - Lasts up to 35 Chops per Charge",
            "Easy to Disassemble and 100% Waterproof Washable"
        ],
        "image_url": "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=600&q=80"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-KTC-002",
        "title": "2-in-1 Automatic Dumpling Maker & Gujiya Press Machine",
        "slug": "2-in-1-automatic-dumpling-maker-gujiya-press",
        "category": "smart-kitchen",
        "deodap_sku": "DD-KTC-DUMP-2N1",
        "wholesale_price": 89.0,
        "selling_price": 279.0,
        "mrp": 599.0,
        "stock": 120,
        "rating": 4.6,
        "review_count": 189,
        "badge": "Top Kitchen Pick",
        "description": "Revolutionary 2-in-1 kitchen tool that molds the dough skin and seals dumplings, momos, or gujiyas in one press. Ergonomic non-slip handle and tight edge seal prevent filling leakage during boiling or frying.",
        "features": [
            "2-in-1 Dual Function: Dough Flattening & Perfect Sealing",
            "Food Grade PP Material - Durable & Non-Toxic",
            "Saves 50% Time during Festivals & Daily Cooking",
            "Anti-Slip Ergonomic Handle for Effortless Pressing",
            "Dishwasher Safe and Easy to Store"
        ],
        "image_url": "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=600&q=80"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-KTC-003",
        "title": "2-in-1 Oil Dispenser Spray & Pour Bottle with Silicone Brush (550ml)",
        "slug": "2-in-1-oil-dispenser-spray-pour-silicone-brush",
        "category": "smart-kitchen",
        "deodap_sku": "DD-KTC-OIL-SPRY",
        "wholesale_price": 65.0,
        "selling_price": 229.0,
        "mrp": 499.0,
        "stock": 64,
        "rating": 4.7,
        "review_count": 215,
        "badge": "Best Seller",
        "description": "Premium borosilicate glass oil container designed for healthy air fryer cooking, pan frying, baking, and barbecue. Switch effortlessly between fine mist spray and controlled pour spout with an integrated heat-resistant silicone basting brush.",
        "features": [
            "Dual Mode: Controlled Pouring & Ultra-Fine Mist Spray",
            "Integrated Heat-Resistant Silicone Basting Brush",
            "Leak-Proof Seal Ring & Wide Neck for Mess-Free Refills",
            "Promotes Healthy Diet by Reducing Oil Consumption by 60%",
            "High Quality Glass & Food-Grade Silicone"
        ],
        "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=600&q=80"
        ],
        "is_trending": 0
    },
    {
        "id": "SAGA-KTC-005",
        "title": "9-in-1 Multifunction Vegetable Chopper, Slicer & Drain Basket",
        "slug": "9-in-1-multifunction-vegetable-chopper-slicer-drain",
        "category": "smart-kitchen",
        "deodap_sku": "DD-KTC-SLIC-9IN1",
        "wholesale_price": 189.0,
        "selling_price": 499.0,
        "mrp": 999.0,
        "stock": 42,
        "rating": 4.9,
        "review_count": 420,
        "badge": "Chef Choice",
        "description": "The ultimate kitchen prep station. Features 7 interchangeable stainless steel cutting blades, hand protector guard, egg white separator, and an ingenious 360° rotating colander drain basket for effortless washing and slicing.",
        "features": [
            "7 Razor-Sharp Interchangeable Stainless Blades",
            "Integrated Rotating Drain Basket for Instant Rinsing",
            "Ergonomic Hand Safety Guard & Finger Protector",
            "Chop, Julienne, Grate, Ribbon & Dice Vegetables",
            "Heavy-Duty Sturdy Base with Non-Skid Rubber Feet"
        ],
        "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=600&q=80"
        ],
        "is_trending": 1
    },

    # --- Viral Tech Gadgets ---
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
        "is_trending": 1
    },
    {
        "id": "SAGA-TEC-002",
        "title": "Mini Pocket Wireless Bluetooth Thermal Photo & Note Printer",
        "slug": "mini-pocket-wireless-bluetooth-thermal-printer",
        "category": "viral-gadgets",
        "deodap_sku": "DD-TEC-PRNT-MINI",
        "wholesale_price": 599.0,
        "selling_price": 1399.0,
        "mrp": 2999.0,
        "stock": 32,
        "rating": 4.7,
        "review_count": 275,
        "badge": "Reel Sensation 📸",
        "description": "Zero ink, zero mess! Connects instantly via Bluetooth to iOS and Android smartphones using a companion app. Print study notes, to-do checklists, labels, journals, QR codes, and black & white photos anywhere on thermal paper rolls.",
        "features": [
            "200 DPI Thermal Print Head - Never Requires Ink Cartridges",
            "Instant Bluetooth 4.0 Connection with Free App",
            "Ultra-Compact Cat-Ear Design (Fits in Shirt Pocket)",
            "Includes 1 Thermal Paper Roll + USB Charging Cable",
            "Rechargeable 1000mAh Battery for Hours of Printing"
        ],
        "image_url": "https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?w=600&q=80"
        ],
        "is_trending": 1
    },

    # --- Home & Projector ---
    {
        "id": "SAGA-HOM-001",
        "title": "Astronaut Galaxy Starry Sky Projector with 360° Remote & Timer",
        "slug": "astronaut-galaxy-starry-sky-projector-remote",
        "category": "viral-gadgets",
        "deodap_sku": "DD-HOM-ASTRO-LED",
        "wholesale_price": 449.0,
        "selling_price": 1199.0,
        "mrp": 2499.0,
        "stock": 35,
        "rating": 4.9,
        "review_count": 530,
        "badge": "Viral Sensation ⭐",
        "description": "Transform any bedroom into a magical universe. Features a magnetic 360° rotating astronaut head that projects ultra-vivid nebula clouds and twinkling stars onto walls and ceilings. Includes wireless remote control, brightness adjustment, and auto-off sleep timer.",
        "features": [
            "High-Definition 8 Nebula Modes & Twinkling Green Stars",
            "360° Magnetic Head Rotation with Adjustable Angle",
            "Smart Wireless Remote Control (Range up to 5m)",
            "Automatic Sleep Timer (45 / 90 Minutes)",
            "Perfect Mood Lighting for Bedrooms, Gaming & Parties"
        ],
        "image_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600&q=80"
        ],
        "is_trending": 1
    },

    # --- Beauty & Personal Care ---
    {
        "id": "SAGA-BEA-001",
        "title": "100% Natural Himalayan Rose Quartz Jade Roller & Gua Sha Scraping Tool",
        "slug": "natural-rose-quartz-jade-roller-gua-sha-tool",
        "category": "beauty-care",
        "deodap_sku": "DD-BEA-JADE-GUA",
        "wholesale_price": 89.0,
        "selling_price": 289.0,
        "mrp": 699.0,
        "stock": 110,
        "rating": 4.8,
        "review_count": 390,
        "badge": "Skincare Trend",
        "description": "Authentic natural cooling crystal stone duo for facial lymphatic drainage, reducing puffiness, tightening jawline contours, and enhancing serum absorption. Comes in a protective satin gift box.",
        "features": [
            "100% Authentic Natural Rose Quartz Cooling Crystal",
            "Dual-Ended Roller for Face, Under-Eye & Neck Contouring",
            "Heart-Shaped Gua Sha Stone for Deep Lymphatic Massage",
            "Reduces Fine Lines, Puffiness & Dark Circles",
            "Reinforced Zinc Alloy Metal Frame - Squeak-Free Rolling"
        ],
        "image_url": "https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?w=600&q=80"
        ],
        "is_trending": 1
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
    print("Database seeded successfully with Saga brand products & categories!")

if __name__ == "__main__":
    from .database import init_db
    init_db()
    seed_database()
