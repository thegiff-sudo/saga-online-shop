import json
from .database import get_db

CATEGORIES = [
    {
        "id": "cat-all",
        "name": "All Products",
        "slug": "all",
        "icon": "fa-solid fa-border-all",
        "image_url": "https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=300&q=80"
    },
    {
        "id": "cat-kitchen",
        "name": "Smart Kitchen",
        "slug": "smart-kitchen",
        "icon": "fa-solid fa-utensils",
        "image_url": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=300&q=80"
    },
    {
        "id": "cat-home",
        "name": "Home & Organizers",
        "slug": "home-organizers",
        "icon": "fa-solid fa-couch",
        "image_url": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=300&q=80"
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
    },
    {
        "id": "cat-fitness",
        "name": "Fitness & Car Accessories",
        "slug": "fitness-car",
        "icon": "fa-solid fa-dumbbell",
        "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=300&q=80"
    }
]

PRODUCTS = [
    # --- Smart Kitchen ---
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
            "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=600&q=80",
            "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=600&q=80"
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
        "id": "SAGA-KTC-004",
        "title": "6-Piece Reusable Stretch Silicone Food Storage Bowl Lids",
        "slug": "6-piece-reusable-stretch-silicone-food-lids",
        "category": "smart-kitchen",
        "deodap_sku": "DD-KTC-LIDS-6PC",
        "wholesale_price": 49.0,
        "selling_price": 189.0,
        "mrp": 399.0,
        "stock": 150,
        "rating": 4.5,
        "review_count": 112,
        "badge": "Eco-Friendly",
        "description": "Never struggle with plastic cling wrap again. These 6 flexible silicone stretch lids form an airtight, leak-proof seal over bowls, containers, pots, watermelons, and cups. Microwave, freezer, and dishwasher safe.",
        "features": [
            "6 Varied Sizes (6.5cm to 21cm) Fits Any Bowl or Fruit",
            "100% Airtight & Leak-Proof Seal Prevents Odor",
            "BPA-Free Food-Grade Platinum Silicone",
            "Temperature Resistant from -40°C to 230°C",
            "Reusable for Years, Zero Plastic Waste"
        ],
        "image_url": "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=600&q=80"
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
    {
        "id": "SAGA-KTC-006",
        "title": "Portable Mini Bag Heat Sealer with Hidden Cutter",
        "slug": "portable-mini-bag-heat-sealer-hidden-cutter",
        "category": "smart-kitchen",
        "deodap_sku": "DD-KTC-SEAL-MINI",
        "wholesale_price": 55.0,
        "selling_price": 199.0,
        "mrp": 449.0,
        "stock": 95,
        "rating": 4.4,
        "review_count": 98,
        "badge": "Snack Saver",
        "description": "Pocket-sized 2-in-1 sealing machine that locks freshness in chip bags, snack packets, pulses, and dry fruits. Equipped with magnetic bottom for easy storage on the refrigerator door.",
        "features": [
            "Fast 3-Second Heating for Instant Airtight Seal",
            "Built-in Hidden Sharp Blade for Easy Bag Opening",
            "Magnetic Base to Stick Right on Fridge",
            "Keeps Chips & Snacks Crispy for Weeks",
            "Battery Operated, Lightweight & Portable"
        ],
        "image_url": "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=600&q=80"
        ],
        "is_trending": 0
    },

    # --- Home & Organizers ---
    {
        "id": "SAGA-HOM-001",
        "title": "Astronaut Galaxy Starry Sky Projector with 360° Remote & Timer",
        "slug": "astronaut-galaxy-starry-sky-projector-remote",
        "category": "home-organizers",
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
    {
        "id": "SAGA-HOM-002",
        "title": "Wireless USB Rechargeable LED Motion Sensor Light (Pack of 2)",
        "slug": "wireless-usb-rechargeable-led-motion-sensor-light",
        "category": "home-organizers",
        "deodap_sku": "DD-HOM-MOTN-LGT2",
        "wholesale_price": 125.0,
        "selling_price": 379.0,
        "mrp": 799.0,
        "stock": 70,
        "rating": 4.7,
        "review_count": 280,
        "badge": "Smart Living",
        "description": "Hands-free smart illumination for wardrobes, staircases, kitchen cabinets, and dark corridors. Detects human motion within 3-5 meters and turns off automatically after 20 seconds. Built-in strong magnet installs anywhere with included 3M adhesive plates.",
        "features": [
            "PIR Motion Sensor + Day/Night Light Sensor",
            "Warm White / Cool White Gentle Eye-Care Illumination",
            "Magnetic Stick-on Base - No Wiring or Tools Needed",
            "USB Rechargeable Lithium Battery (Up to 60 Days on Auto)",
            "Sleek Ultra-Thin Body Design"
        ],
        "image_url": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=600&q=80"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-HOM-003",
        "title": "9-Hole Space-Saving Magic Foldable Clothes Hanger (Pack of 3)",
        "slug": "9-hole-space-saving-magic-foldable-clothes-hanger",
        "category": "home-organizers",
        "deodap_sku": "DD-HOM-HNGR-3PC",
        "wholesale_price": 79.0,
        "selling_price": 249.0,
        "mrp": 549.0,
        "stock": 110,
        "rating": 4.6,
        "review_count": 164,
        "badge": "Wardrobe Must",
        "description": "Multiply your wardrobe closet space by 4X. Each hanger features 9 slots and a 360° rotating hook that can be used horizontally or vertically to store shirts, dresses, suits, and coats without creasing.",
        "features": [
            "Saves 80% Closet Space When Used Vertically",
            "Heavy-Duty Reinforced PP Plastic Holds up to 10kg",
            "360° Swivel Hook with Anti-Drop Smooth Edge",
            "Pack of 3 Multicolored Organizers",
            "Organize Clothes by Season, Color, or Type"
        ],
        "image_url": "https://images.unsplash.com/photo-1582735689369-4fe89db7114c?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1582735689369-4fe89db7114c?w=600&q=80"
        ],
        "is_trending": 0
    },
    {
        "id": "SAGA-HOM-004",
        "title": "Self-Adhesive Rustproof Bathroom Corner Triangle Shelf (Pack of 2)",
        "slug": "self-adhesive-rustproof-bathroom-corner-triangle-shelf",
        "category": "home-organizers",
        "deodap_sku": "DD-HOM-BATH-CRNR",
        "wholesale_price": 95.0,
        "selling_price": 299.0,
        "mrp": 699.0,
        "stock": 88,
        "rating": 4.8,
        "review_count": 310,
        "badge": "No Drill Needed",
        "description": "Maximize 90-degree corner spaces in bathrooms and kitchens. Strong trace-less magic adhesive strips provide up to 5kg load capacity without damaging tiles or drilling holes. Drainage grid prevents stagnant water.",
        "features": [
            "Strong Adhesive Hooks - No Drilling, No Nails, No Holes",
            "Corrosion-Resistant Powder Coated Stainless Metal",
            "Rapid Water Drainage Hollow Grid Design",
            "Holds Shampoo Bottles, Body Wash, Oils & Soaps",
            "Works on Ceramic Tiles, Glass, Granite & Polished Marble"
        ],
        "image_url": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=600&q=80"
        ],
        "is_trending": 0
    },
    {
        "id": "SAGA-HOM-005",
        "title": "360° Spin Floor Cleaning Microfiber Magic Mop with Dual Bucket",
        "slug": "360-spin-floor-cleaning-microfiber-magic-mop",
        "category": "home-organizers",
        "deodap_sku": "DD-HOM-MOP-360",
        "wholesale_price": 220.0,
        "selling_price": 599.0,
        "mrp": 1299.0,
        "stock": 28,
        "rating": 4.7,
        "review_count": 195,
        "badge": "Deep Clean",
        "description": "Effortless cleaning with hands-free spin wringing system. Super-absorbent microfiber strands trap fine dust, hair, and stubborn liquid stains on all types of floorings including marble, wood, and tiles.",
        "features": [
            "Stainless Steel Rapid Spin Dryer Basket",
            "Thick Microfiber Pad Traps 3X More Dust & Dirt",
            "Extendable 360° Flexible Stainless Steel Handle",
            "Includes 2 Washable Reusable Microfiber Mop Heads",
            "Built-in Water Drain Plug for Mess-Free Emptying"
        ],
        "image_url": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=600&q=80"
        ],
        "is_trending": 0
    },

    # --- Viral Gadgets & Tech ---
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
    {
        "id": "SAGA-TEC-003",
        "title": "10-Inch LED Selfie Ring Light with 7ft Heavy Tripod & Phone Mount",
        "slug": "10-inch-led-selfie-ring-light-tripod-phone-mount",
        "category": "viral-gadgets",
        "deodap_sku": "DD-TEC-RING-10IN",
        "wholesale_price": 210.0,
        "selling_price": 549.0,
        "mrp": 1199.0,
        "stock": 65,
        "rating": 4.6,
        "review_count": 380,
        "badge": "Creator Essential",
        "description": "Professional studio lighting designed for YouTube videos, Instagram Reels, Zoom calls, makeup tutorials, and photography. Features 3 color temperatures (Warm, Natural, Cool White) with 10 dimmable brightness levels and full 360° pan-tilt.",
        "features": [
            "3 Color Modes (3000K - 6500K) & 10 Brightness Levels",
            "Heavy-Duty Adjustable 7-Foot Metal Tripod Stand",
            "360° Universal Rotatable Smartphone Holder",
            "USB-Powered - Works with Powerbanks, Laptops & Adapters",
            "Includes In-Line Remote Controller"
        ],
        "image_url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=600&q=80"
        ],
        "is_trending": 0
    },
    {
        "id": "SAGA-TEC-004",
        "title": "Portable Hands-Free Bladeless Hanging Neck Fan (USB Rechargeable)",
        "slug": "portable-hands-free-bladeless-hanging-neck-fan",
        "category": "viral-gadgets",
        "deodap_sku": "DD-TEC-NECK-FAN",
        "wholesale_price": 199.0,
        "selling_price": 549.0,
        "mrp": 1199.0,
        "stock": 74,
        "rating": 4.6,
        "review_count": 190,
        "badge": "Beat The Heat",
        "description": "Enjoy a continuous 360° cool breeze around your neck without tangled hair or loud noise. Lightweight headphone-styled design with twin turbine motors and 3 adjustable speed modes.",
        "features": [
            "Safe Bladeless Design - Won't Pinch or Twist Hair",
            "Twin Turbines with 78 Surround Air Outlets",
            "3 Speed Wind Settings (Soft, Medium, Cyclone)",
            "Ultra-Quiet Brushless Motor (<25dB Sound)",
            "2400mAh Battery Runs 4-8 Hours on Single USB Charge"
        ],
        "image_url": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=600&q=80"
        ],
        "is_trending": 0
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
    },
    {
        "id": "SAGA-BEA-002",
        "title": "540 Micro-Needles 0.5mm Titanium Derma Roller for Hair & Beard Growth",
        "slug": "540-micro-needles-titanium-derma-roller-hair-beard",
        "category": "beauty-care",
        "deodap_sku": "DD-BEA-DERM-540",
        "wholesale_price": 75.0,
        "selling_price": 249.0,
        "mrp": 599.0,
        "stock": 85,
        "rating": 4.7,
        "review_count": 230,
        "badge": "Beard & Hair Growth",
        "description": "Clinical grade 0.5mm micro-needling roller designed to stimulate dormant hair follicles, boost collagen synthesis, and maximize the absorption of minoxidil, rosemary oil, and beard growth serums.",
        "features": [
            "540 Ultra-Sharp Medical Grade Titanium Needles (0.5mm)",
            "Stimulates Natural Collagen & Blood Circulation",
            "Proven to Fill Beard Patches and Scalp Thinning",
            "Ergonomic Anti-Slip Grip Handle",
            "Includes Clear Protective Storage Case"
        ],
        "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=600&q=80"
        ],
        "is_trending": 0
    },
    {
        "id": "SAGA-BEA-003",
        "title": "Electric Flawless Eyebrow & Precision Facial Hair Trimmer",
        "slug": "electric-flawless-eyebrow-facial-hair-trimmer",
        "category": "beauty-care",
        "deodap_sku": "DD-BEA-EYEB-TRIM",
        "wholesale_price": 110.0,
        "selling_price": 329.0,
        "mrp": 699.0,
        "stock": 92,
        "rating": 4.6,
        "review_count": 310,
        "badge": "Painless Beauty",
        "description": "Say goodbye to painful waxing, threading, and plucking. 18K gold-plated precision micro-blade gently erases unwanted hair from eyebrows, upper lip, chin, and peach fuzz instantly without redness or irritation.",
        "features": [
            "18K Hypoallergenic Gold-Plated Precision Head",
            "Built-in Bright LED Light to Catch Every Fine Hair",
            "100% Painless - Safe for Sensitive Skin Daily Use",
            "Compact Lipstick-Sized Design for Handbag Portability",
            "USB Rechargeable - No Need to Buy AA Batteries"
        ],
        "image_url": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&q=80"
        ],
        "is_trending": 1
    },

    # --- Fitness & Car Accessories ---
    {
        "id": "SAGA-FIT-001",
        "title": "9-in-1 Color-Coded Foldable Push-Up Board System",
        "slug": "9-in-1-color-coded-foldable-push-up-board",
        "category": "fitness-car",
        "deodap_sku": "DD-FIT-PUSH-9IN1",
        "wholesale_price": 199.0,
        "selling_price": 549.0,
        "mrp": 1199.0,
        "stock": 58,
        "rating": 4.8,
        "review_count": 410,
        "badge": "Home Gym King 💪",
        "description": "Scientifically targets specific upper-body muscle groups through color-coded positions: Blue for Chest, Red for Shoulders, Yellow for Back, and Green for Triceps. Heavy-duty folding design with non-slip handles and floor pads.",
        "features": [
            "Color-Coded Positions Target 4 Major Muscle Groups",
            "Heavy-Duty ABS Engineering Plastic Holds up to 150kg",
            "Foldable Compact Design with Locking Mechanism",
            "Premium Silicone Padded Non-Slip Hand Grips",
            "Perfect for Home Workout, Calisthenics & Travel"
        ],
        "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600&q=80"
        ],
        "is_trending": 1
    },
    {
        "id": "SAGA-FIT-002",
        "title": "Smart LED Temperature Display Insulated Stainless Steel Flask (500ml)",
        "slug": "smart-led-temperature-display-insulated-flask",
        "category": "fitness-car",
        "deodap_sku": "DD-FIT-TEMP-FLSK",
        "wholesale_price": 135.0,
        "selling_price": 399.0,
        "mrp": 899.0,
        "stock": 95,
        "rating": 4.7,
        "review_count": 340,
        "badge": "Top Rated",
        "description": "Double-wall vacuum insulated smart water bottle featuring an ultra-sensitive touch LCD temperature display on the lid. Keeps tea, coffee, and soup hot for 12 hours, or iced water chilled for 24 hours.",
        "features": [
            "High-Definition Touch LCD Screen Shows Live Water Temperature",
            "Double-Wall Vacuum Insulation (12h Hot / 24h Cold)",
            "Food-Grade 304 Stainless Steel Interior (Rust & Odor Proof)",
            "Includes Removable Stainless Steel Tea Infuser Strainer",
            "Leak-Proof Silicone Gasket Cap"
        ],
        "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=600&q=80"
        ],
        "is_trending": 0
    },
    {
        "id": "SAGA-FIT-003",
        "title": "High-Pressure Adjustable Jet Water Spray Gun for Car Washing & Gardening",
        "slug": "high-pressure-adjustable-jet-water-spray-gun",
        "category": "fitness-car",
        "deodap_sku": "DD-CAR-WTR-GUN",
        "wholesale_price": 175.0,
        "selling_price": 489.0,
        "mrp": 999.0,
        "stock": 60,
        "rating": 4.6,
        "review_count": 225,
        "badge": "Car Wash Pro",
        "description": "Commercial-style heavy solid brass nozzle pressure sprayer. Easily switches between pinpoint direct jet, wide shower, fan spray, and misting. Ideal for blasting car mud, patio moss, and delicate plant watering.",
        "features": [
            "Solid Brass High-Pressure Jet Nozzle",
            "Ergonomic Trigger Handle with Hands-Free Locking Clip",
            "Universal Quick-Connect Hose Fitting Included",
            "Leak-Proof Rubber O-Rings Withstands High Water Pressure",
            "Multi-Pattern Spray: Jet, Mist, Shower, Cone, Fan"
        ],
        "image_url": "https://images.unsplash.com/photo-1520340356584-f9917d1eea6f?w=600&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1520340356584-f9917d1eea6f?w=600&q=80"
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

SAMPLE_ORDERS = [
    {
        "id": "SAGA-89214",
        "customer_name": "Rohan Deshmukh",
        "customer_phone": "9823012456",
        "customer_email": "rohan.d@gmail.com",
        "address": "Flat 402, Shiv Shanti Residency, FC Road",
        "city": "Pune",
        "state": "Maharashtra",
        "pincode": "411004",
        "payment_method": "Cash on Delivery",
        "payment_status": "Pending",
        "subtotal": 1498.0,
        "discount": 100.0,
        "shipping_fee": 0.0,
        "total_amount": 1398.0,
        "total_wholesale_cost": 599.0,
        "total_margin": 799.0,
        "status": "In Transit",
        "items": [
            {"id": "SAGA-KTC-001", "title": "Electric USB Mini Vegetable & Garlic Chopper (250ml)", "price": 349.0, "wholesale_price": 119.0, "quantity": 1, "deodap_sku": "DD-KTC-CHOP-250"},
            {"id": "SAGA-HOM-001", "title": "Astronaut Galaxy Starry Sky Projector with 360° Remote & Timer", "price": 1199.0, "wholesale_price": 449.0, "quantity": 1, "deodap_sku": "DD-HOM-ASTRO-LED"}
        ],
        "created_at": "2026-10-23 11:20:00",
        "deodap_sync_status": "Synced to DeoDap",
        "tracking_number": "DEL-EXP-99214456"
    },
    {
        "id": "SAGA-89190",
        "customer_name": "Pooja Sharma",
        "customer_phone": "9167234567",
        "customer_email": "pooja.sharma@yahoo.com",
        "address": "B-12, Green Park Extension, Near Metro Gate 2",
        "city": "New Delhi",
        "state": "Delhi",
        "pincode": "110016",
        "payment_method": "UPI Online",
        "payment_status": "Paid",
        "subtotal": 549.0,
        "discount": 50.0,
        "shipping_fee": 0.0,
        "total_amount": 499.0,
        "total_wholesale_cost": 199.0,
        "total_margin": 300.0,
        "status": "Delivered",
        "items": [
            {"id": "SAGA-FIT-001", "title": "9-in-1 Color-Coded Foldable Push-Up Board System", "price": 549.0, "wholesale_price": 199.0, "quantity": 1, "deodap_sku": "DD-FIT-PUSH-9IN1"}
        ],
        "created_at": "2026-10-22 14:10:00",
        "deodap_sync_status": "Delivered by DeoDap",
        "tracking_number": "BLR-DTP-88712344"
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

    # Seed sample orders if empty
    cursor.execute("SELECT COUNT(*) FROM orders")
    if cursor.fetchone()[0] == 0:
        for ord in SAMPLE_ORDERS:
            cursor.execute("""
            INSERT INTO orders (
                id, customer_name, customer_phone, customer_email, address, city, state,
                pincode, payment_method, payment_status, subtotal, discount, shipping_fee,
                total_amount, total_wholesale_cost, total_margin, status, items_json,
                created_at, deodap_sync_status, tracking_number
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                ord["id"], ord["customer_name"], ord["customer_phone"], ord["customer_email"],
                ord["address"], ord["city"], ord["state"], ord["pincode"], ord["payment_method"],
                ord["payment_status"], ord["subtotal"], ord["discount"], ord["shipping_fee"],
                ord["total_amount"], ord["total_wholesale_cost"], ord["total_margin"],
                ord["status"], json.dumps(ord["items"]), ord["created_at"],
                ord["deodap_sync_status"], ord["tracking_number"]
            ))

    conn.commit()
    conn.close()
    print("Database seeded successfully with realistic DeoDap products and SAGA margins!")

if __name__ == "__main__":
    from .database import init_db
    init_db()
    seed_database()
