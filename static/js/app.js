/**
 * SAGA ONLINE SHOP - Main Application JavaScript
 * Connects frontend with FastAPI dropshipping backend and WhatsApp support
 */

const WHATSAPP_NUMBER = "9922163722";

const state = {
  products: [],
  categories: [],
  currentCategory: "all",
  searchQuery: "",
  sortOption: "popular",
  cart: [],
  appliedCoupon: null,
  ownerMode: false,
  selectedProduct: null,
  pincodeInfo: null,
};

// Initialize app on DOM loaded
document.addEventListener("DOMContentLoaded", () => {
  loadCartFromStorage();
  loadOwnerModeFromStorage();
  setupEventListeners();
  fetchCategories();
  fetchProducts();
  updateCartBadge();
});

// Storage helpers
function loadCartFromStorage() {
  try {
    const saved = localStorage.getItem("saga_cart");
    if (saved) state.cart = JSON.parse(saved);
  } catch (e) {
    state.cart = [];
  }
}

function saveCartToStorage() {
  localStorage.setItem("saga_cart", JSON.stringify(state.cart));
  updateCartBadge();
  renderCartDrawer();
}

function loadOwnerModeFromStorage() {
  const saved = localStorage.getItem("saga_owner_mode");
  if (saved === "true") {
    state.ownerMode = true;
    document.body.classList.add("owner-mode-active");
  }
  updateOwnerModeToggleUI();
}

function toggleOwnerMode() {
  state.ownerMode = !state.ownerMode;
  localStorage.setItem("saga_owner_mode", state.ownerMode);
  if (state.ownerMode) {
    document.body.classList.add("owner-mode-active");
    showToast("Merchant Dropship Mode Enabled: DeoDap base prices & profit margins are now visible!");
  } else {
    document.body.classList.remove("owner-mode-active");
    showToast("Customer View Enabled: Dropship margins hidden.");
  }
  updateOwnerModeToggleUI();
  renderProducts();
}

function updateOwnerModeToggleUI() {
  const toggleBtn = document.getElementById("ownerModeToggle");
  const toggleCheckbox = document.getElementById("ownerModeCheckbox");
  if (toggleCheckbox) {
    toggleCheckbox.checked = state.ownerMode;
  }
  if (toggleBtn) {
    if (state.ownerMode) {
      toggleBtn.classList.add("bg-emerald-600", "text-white");
      toggleBtn.classList.remove("bg-slate-100", "text-slate-700");
    } else {
      toggleBtn.classList.remove("bg-emerald-600", "text-white");
      toggleBtn.classList.add("bg-slate-100", "text-slate-700");
    }
  }
}

// Event Listeners setup
function setupEventListeners() {
  // Search input
  const searchInput = document.getElementById("searchInput");
  const mobileSearchInput = document.getElementById("mobileSearchInput");

  const handleSearch = (e) => {
    state.searchQuery = e.target.value.trim();
    fetchProducts();
  };

  if (searchInput) searchInput.addEventListener("input", debounce(handleSearch, 300));
  if (mobileSearchInput) mobileSearchInput.addEventListener("input", debounce(handleSearch, 300));

  // Sort dropdown
  const sortSelect = document.getElementById("sortSelect");
  if (sortSelect) {
    sortSelect.addEventListener("change", (e) => {
      state.sortOption = e.target.value;
      fetchProducts();
    });
  }

  // Owner mode toggle
  const ownerToggle = document.getElementById("ownerModeCheckbox");
  if (ownerToggle) {
    ownerToggle.addEventListener("change", toggleOwnerMode);
  }
}

function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

// Fetch Categories
async function fetchCategories() {
  try {
    const res = await fetch("/api/categories");
    state.categories = await res.json();
    renderCategories();
  } catch (err) {
    console.error("Error fetching categories:", err);
  }
}

function renderCategories() {
  const container = document.getElementById("categoriesContainer");
  if (!container) return;

  container.innerHTML = state.categories
    .map(
      (cat) => `
      <button 
        onclick="selectCategory('${cat.slug}')"
        class="category-pill flex items-center space-x-2 px-4 py-2.5 rounded-full text-sm font-semibold transition-all whitespace-nowrap shadow-sm border ${
          state.currentCategory === cat.slug
            ? "bg-blue-900 text-white border-blue-900 shadow-md scale-105"
            : "bg-white text-slate-700 hover:bg-slate-50 border-slate-200"
        }"
      >
        <i class="${cat.icon} ${state.currentCategory === cat.slug ? "text-amber-400" : "text-blue-600"}"></i>
        <span>${cat.name}</span>
        <span class="text-xs px-2 py-0.5 rounded-full ${
          state.currentCategory === cat.slug ? "bg-blue-800 text-amber-300" : "bg-slate-100 text-slate-500"
        }">${cat.count}</span>
      </button>
    `
    )
    .join("");
}

function selectCategory(slug) {
  state.currentCategory = slug;
  renderCategories();
  fetchProducts();

  // Scroll to products section smoothly
  const section = document.getElementById("productsSection");
  if (section) section.scrollIntoView({ behavior: "smooth" });
}

// Fetch Products
async function fetchProducts() {
  const grid = document.getElementById("productsGrid");
  if (grid) {
    grid.innerHTML = Array(8)
      .fill(0)
      .map(
        () => `
        <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-sm animate-pulse flex flex-col space-y-3">
          <div class="w-full h-48 bg-slate-200 rounded-xl"></div>
          <div class="h-4 bg-slate-200 rounded w-3/4"></div>
          <div class="h-3 bg-slate-200 rounded w-1/2"></div>
          <div class="h-6 bg-slate-200 rounded w-1/3"></div>
        </div>
      `
      )
      .join("");
  }

  try {
    let url = `/api/products?category=${encodeURIComponent(state.currentCategory)}&search=${encodeURIComponent(
      state.searchQuery
    )}&sort=${encodeURIComponent(state.sortOption)}`;

    const res = await fetch(url);
    state.products = await res.json();
    renderProducts();
  } catch (err) {
    console.error("Error fetching products:", err);
    if (grid) {
      grid.innerHTML = `
        <div class="col-span-full py-16 text-center text-slate-500">
          <i class="fa-solid fa-triangle-exclamation text-4xl text-amber-500 mb-3"></i>
          <p class="text-lg font-medium">Failed to load products. Please check back shortly.</p>
        </div>
      `;
    }
  }
}

// Render Products Grid
function renderProducts() {
  const grid = document.getElementById("productsGrid");
  const countBadge = document.getElementById("productsCountBadge");
  if (countBadge) countBadge.innerText = `${state.products.length} Products Found`;

  if (!grid) return;

  if (state.products.length === 0) {
    grid.innerHTML = `
      <div class="col-span-full py-16 text-center text-slate-500 bg-white rounded-2xl border border-slate-200 p-8">
        <i class="fa-solid fa-box-open text-5xl text-slate-300 mb-3"></i>
        <h3 class="text-xl font-bold text-slate-800 mb-1">No products found</h3>
        <p class="text-sm text-slate-500 mb-4">Try clearing your search query or choosing another category.</p>
        <button onclick="resetFilters()" class="px-5 py-2.5 bg-blue-900 text-white rounded-xl text-sm font-semibold hover:bg-blue-800 transition">
          View All Products
        </button>
      </div>
    `;
    return;
  }

  grid.innerHTML = state.products
    .map((prod) => {
      return `
      <div class="product-card bg-white rounded-2xl border border-slate-200/90 shadow-sm overflow-hidden flex flex-col justify-between group relative">
        
        <!-- Top Badges -->
        <div class="absolute top-3 left-3 z-10 flex flex-col gap-1.5 items-start">
          ${
            prod.badge
              ? `<span class="bg-blue-900/90 backdrop-blur-md text-amber-300 text-xs font-bold px-2.5 py-1 rounded-full shadow-sm">
                  ${prod.badge}
                </span>`
              : ""
          }
          <span class="discount-ribbon">
            ${prod.discount_percent}% OFF
          </span>
        </div>

        <!-- Wishlist Button -->
        <button 
          onclick="toggleWishlist('${prod.id}')"
          class="absolute top-3 right-3 z-10 w-9 h-9 rounded-full bg-white/90 backdrop-blur-md text-slate-400 hover:text-rose-500 flex items-center justify-center shadow-md transition"
          title="Save to Wishlist"
        >
          <i class="fa-regular fa-heart"></i>
        </button>

        <!-- Product Image Container -->
        <div 
          onclick="openProductModal('${prod.id}')"
          class="product-image-container relative w-full h-52 bg-slate-50 cursor-pointer overflow-hidden flex items-center justify-center p-4 border-b border-slate-100"
        >
          <img 
            src="${prod.image_url}" 
            alt="${escapeHtml(prod.title)}" 
            class="w-full h-full object-contain mix-blend-multiply group-hover:scale-105 transition-transform duration-300"
            loading="lazy"
            onerror="this.src='https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&q=80'"
          />
        </div>

        <!-- Product Content -->
        <div class="p-4 flex-1 flex flex-col justify-between">
          <div>
            <!-- Star Rating & Sales count -->
            <div class="flex items-center space-x-2 mb-1.5">
              <div class="flex items-center text-amber-400 text-xs">
                ${renderStars(prod.rating)}
              </div>
              <span class="text-xs font-semibold text-slate-700">${prod.rating}</span>
              <span class="text-xs text-slate-400">(${prod.review_count} reviews)</span>
            </div>

            <!-- Title -->
            <h3 
              onclick="openProductModal('${prod.id}')"
              class="text-sm font-semibold text-slate-900 line-clamp-2 hover:text-blue-700 cursor-pointer transition mb-2"
              title="${escapeHtml(prod.title)}"
            >
              ${escapeHtml(prod.title)}
            </h3>

            <!-- Price Row -->
            <div class="flex items-baseline space-x-2 mb-2">
              <span class="text-xl font-black text-slate-950">₹${prod.selling_price}</span>
              <span class="text-xs text-slate-400 line-through">₹${prod.mrp}</span>
              <span class="text-xs font-bold text-emerald-600">Save ₹${Math.round(prod.mrp - prod.selling_price)}</span>
            </div>

            <!-- Dropship Margin Badge (Owner Mode Only) -->
            <div class="owner-only mb-3">
              <div class="dropship-margin-badge w-full justify-between">
                <span><i class="fa-solid fa-boxes-packing mr-1"></i>DeoDap Base: ₹${prod.wholesale_price}</span>
                <span class="font-extrabold text-amber-200">+₹${prod.margin} Profit (${prod.margin_percent}%)</span>
              </div>
            </div>

            <!-- Free delivery & COD badges -->
            <div class="flex items-center space-x-3 text-[11px] text-slate-500 mb-3">
              <span class="flex items-center"><i class="fa-solid fa-truck-fast text-blue-600 mr-1"></i> Fast Dispatch</span>
              <span class="flex items-center"><i class="fa-solid fa-hand-holding-dollar text-emerald-600 mr-1"></i> COD Avail</span>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="grid grid-cols-2 gap-2 mt-auto pt-2 border-t border-slate-100">
            <button 
              onclick="addToCart('${prod.id}', 1)"
              class="flex items-center justify-center space-x-1.5 py-2.5 px-3 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold transition active:scale-95"
            >
              <i class="fa-solid fa-cart-plus"></i>
              <span>Add Cart</span>
            </button>
            <button 
              onclick="buyNow('${prod.id}')"
              class="flex items-center justify-center space-x-1 py-2.5 px-3 rounded-xl bg-gradient-to-r from-blue-900 to-indigo-800 hover:from-blue-800 hover:to-indigo-700 text-white text-xs font-bold transition shadow-sm active:scale-95"
            >
              <span>Buy Now</span>
              <i class="fa-solid fa-arrow-right text-[10px]"></i>
            </button>
          </div>
        </div>

      </div>
    `;
    })
    .join("");
}

function resetFilters() {
  state.currentCategory = "all";
  state.searchQuery = "";
  state.sortOption = "popular";
  const searchInput = document.getElementById("searchInput");
  if (searchInput) searchInput.value = "";
  renderCategories();
  fetchProducts();
}

function renderStars(rating) {
  const full = Math.floor(rating);
  const half = rating % 1 >= 0.5 ? 1 : 0;
  let str = "";
  for (let i = 0; i < full; i++) str += '<i class="fa-solid fa-star"></i>';
  if (half) str += '<i class="fa-solid fa-star-half-stroke"></i>';
  for (let i = full + half; i < 5; i++) str += '<i class="fa-regular fa-star text-slate-300"></i>';
  return str;
}

// Product Detail Modal
async function openProductModal(productId) {
  try {
    const res = await fetch(`/api/products/${productId}`);
    if (!res.ok) return;
    const data = await res.json();
    state.selectedProduct = data.product;
    renderProductModalContent(data.product, data.related);
    document.getElementById("productModal").classList.remove("hidden");
    document.body.classList.add("overflow-hidden");
  } catch (err) {
    console.error("Error opening product modal:", err);
  }
}

function closeProductModal() {
  document.getElementById("productModal").classList.add("hidden");
  document.body.classList.remove("overflow-hidden");
  state.selectedProduct = null;
}

function renderProductModalContent(prod, related) {
  const container = document.getElementById("productModalContent");
  if (!container) return;

  const waProductUrl = `https://wa.me/91${WHATSAPP_NUMBER}?text=${encodeURIComponent(
    `Hello SAGA Online Shop! I am interested in ordering: "${prod.title}" (₹${prod.selling_price}). Please share details.`
  )}`;

  container.innerHTML = `
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      
      <!-- Left: Image Gallery -->
      <div class="flex flex-col space-y-4">
        <div class="w-full h-80 sm:h-96 bg-slate-50 rounded-2xl overflow-hidden border border-slate-200 flex items-center justify-center p-6 relative">
          <img 
            id="modalMainImage"
            src="${prod.image_url}" 
            alt="${escapeHtml(prod.title)}" 
            class="max-h-full max-w-full object-contain mix-blend-multiply"
          />
          <span class="absolute top-4 left-4 discount-ribbon text-xs font-bold px-3 py-1.5">
            ${prod.discount_percent}% OFF
          </span>
        </div>

        <!-- Thumbnails -->
        <div class="flex space-x-3 overflow-x-auto pb-2">
          ${[prod.image_url, ...(prod.gallery || [])]
            .map(
              (img, idx) => `
            <button 
              onclick="document.getElementById('modalMainImage').src='${img}'"
              class="w-16 h-16 rounded-xl border-2 border-slate-200 hover:border-blue-600 p-1 flex-shrink-0 bg-white"
            >
              <img src="${img}" class="w-full h-full object-contain" />
            </button>
          `
            )
            .join("")}
        </div>

        <!-- Dropshipping Margin Calculator (Owner Mode Only) -->
        <div class="owner-only bg-emerald-50 border border-emerald-200 rounded-2xl p-4 text-emerald-950">
          <div class="flex items-center justify-between mb-2">
            <span class="font-bold text-xs uppercase tracking-wider text-emerald-800 flex items-center">
              <i class="fa-solid fa-calculator mr-1.5"></i> SAGA Margin Breakdown
            </span>
            <span class="text-xs bg-emerald-200 text-emerald-900 font-bold px-2 py-0.5 rounded">DeoDap Sourced</span>
          </div>
          <div class="grid grid-cols-3 gap-2 text-center text-xs">
            <div class="bg-white p-2 rounded-xl border border-emerald-100">
              <div class="text-slate-500 text-[11px]">DeoDap Base</div>
              <div class="font-extrabold text-slate-800 text-sm">₹${prod.wholesale_price}</div>
            </div>
            <div class="bg-white p-2 rounded-xl border border-emerald-100">
              <div class="text-slate-500 text-[11px]">Selling Price</div>
              <div class="font-extrabold text-blue-900 text-sm">₹${prod.selling_price}</div>
            </div>
            <div class="bg-emerald-600 text-white p-2 rounded-xl">
              <div class="text-emerald-100 text-[11px]">Net Profit</div>
              <div class="font-black text-sm">+₹${prod.margin} (${prod.margin_percent}%)</div>
            </div>
          </div>
          <p class="text-[11px] text-emerald-700 mt-2">
            *DeoDap SKU: <b>${prod.deodap_sku}</b>. Fulfillment and packaging handled seamlessly by DeoDap.
          </p>
        </div>
      </div>

      <!-- Right: Product Info & Actions -->
      <div class="flex flex-col justify-between">
        <div>
          <!-- Category & Badge -->
          <div class="flex items-center space-x-2 mb-2">
            <span class="text-xs font-semibold uppercase tracking-wider text-blue-800 bg-blue-50 px-2.5 py-1 rounded-md">
              ${prod.category.replace("-", " ")}
            </span>
            ${
              prod.badge
                ? `<span class="text-xs font-bold text-amber-800 bg-amber-100 px-2.5 py-1 rounded-md">${prod.badge}</span>`
                : ""
            }
          </div>

          <h2 class="text-2xl font-black text-slate-900 leading-tight mb-2">
            ${escapeHtml(prod.title)}
          </h2>

          <!-- Rating & Reviews -->
          <div class="flex items-center space-x-3 mb-4">
            <div class="flex items-center text-amber-400 text-sm">
              ${renderStars(prod.rating)}
            </div>
            <span class="font-bold text-slate-800 text-sm">${prod.rating}</span>
            <span class="text-slate-400 text-sm">|</span>
            <span class="text-slate-600 text-sm font-medium">${prod.review_count} Verified Customer Reviews</span>
          </div>

          <!-- Price Block -->
          <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200/80 mb-5">
            <div class="flex items-baseline space-x-3 mb-1">
              <span class="text-3xl font-black text-blue-950">₹${prod.selling_price}</span>
              <span class="text-base text-slate-400 line-through">₹${prod.mrp}</span>
              <span class="text-xs font-extrabold text-emerald-600 bg-emerald-100 px-2.5 py-1 rounded-md">
                Save ₹${Math.round(prod.mrp - prod.selling_price)} (${prod.discount_percent}% OFF)
              </span>
            </div>
            <div class="text-xs text-slate-500 flex items-center space-x-2">
              <span>Inclusive of all taxes</span>
              <span>•</span>
              <span class="text-emerald-700 font-bold"><i class="fa-solid fa-circle-check"></i> In Stock (${prod.stock} units available)</span>
            </div>
          </div>

          <!-- Description -->
          <p class="text-sm text-slate-600 leading-relaxed mb-5">
            ${escapeHtml(prod.description)}
          </p>

          <!-- Key Highlights -->
          <div class="mb-5">
            <h4 class="text-xs font-bold uppercase tracking-wider text-slate-900 mb-2.5">Key Features:</h4>
            <ul class="space-y-1.5">
              ${(prod.features || [])
                .map(
                  (f) => `
                <li class="flex items-start text-xs text-slate-700">
                  <i class="fa-solid fa-check-circle text-emerald-600 mt-0.5 mr-2 flex-shrink-0"></i>
                  <span>${escapeHtml(f)}</span>
                </li>
              `
                )
                .join("")}
            </ul>
          </div>

          <!-- Pincode Check -->
          <div class="bg-white p-3.5 rounded-2xl border border-slate-200 mb-6">
            <div class="text-xs font-bold text-slate-800 mb-1.5 flex items-center justify-between">
              <span><i class="fa-solid fa-location-dot text-blue-900 mr-1.5"></i> Check Delivery & COD Availability:</span>
            </div>
            <div class="flex space-x-2">
              <input 
                id="modalPincodeInput"
                type="text" 
                maxlength="6"
                placeholder="Enter 6-digit Pincode" 
                class="flex-1 px-3 py-2 border border-slate-300 rounded-xl text-xs focus:outline-none focus:border-blue-900"
              />
              <button 
                onclick="checkDeliveryPincode()"
                class="px-4 py-2 bg-slate-900 text-white rounded-xl text-xs font-bold hover:bg-slate-800 transition"
              >
                Check
              </button>
            </div>
            <div id="pincodeResultBox" class="mt-2 text-xs hidden"></div>
          </div>
        </div>

        <!-- Purchase Actions -->
        <div>
          <div class="flex items-center space-x-3 mb-3">
            <!-- Quantity selector -->
            <div class="flex items-center border border-slate-300 rounded-xl overflow-hidden bg-white">
              <button 
                onclick="changeModalQty(-1)"
                class="w-10 h-11 flex items-center justify-center text-slate-600 hover:bg-slate-100 font-bold"
              >-</button>
              <span id="modalProductQty" class="w-10 text-center font-bold text-sm text-slate-900">1</span>
              <button 
                onclick="changeModalQty(1)"
                class="w-10 h-11 flex items-center justify-center text-slate-600 hover:bg-slate-100 font-bold"
              >+</button>
            </div>

            <!-- Add to Cart -->
            <button 
              onclick="addModalProductToCart()"
              class="flex-1 py-3 px-4 rounded-xl border-2 border-blue-900 text-blue-950 font-bold text-sm hover:bg-blue-50 transition active:scale-95 flex items-center justify-center space-x-2"
            >
              <i class="fa-solid fa-cart-plus"></i>
              <span>Add to Cart</span>
            </button>

            <!-- Buy Now -->
            <button 
              onclick="buyNowFromModal()"
              class="flex-1 py-3 px-4 rounded-xl bg-gradient-to-r from-blue-900 to-indigo-800 hover:from-blue-800 hover:to-indigo-700 text-white font-bold text-sm shadow-md transition active:scale-95 flex items-center justify-center space-x-2"
            >
              <span>Instant Buy</span>
              <i class="fa-solid fa-bolt text-amber-300"></i>
            </button>
          </div>

          <!-- WhatsApp Chat for Product -->
          <a 
            href="${waProductUrl}"
            target="_blank"
            rel="noopener noreferrer"
            class="w-full py-2.5 px-4 rounded-xl bg-emerald-50 text-emerald-800 hover:bg-emerald-100 font-semibold text-xs border border-emerald-200 flex items-center justify-center space-x-2 transition"
          >
            <i class="fa-brands fa-whatsapp text-emerald-600 text-base"></i>
            <span>Have questions? Chat on WhatsApp (${WHATSAPP_NUMBER})</span>
          </a>
        </div>

      </div>

    </div>
  `;
}

function changeModalQty(delta) {
  const el = document.getElementById("modalProductQty");
  if (!el) return;
  let cur = parseInt(el.innerText) || 1;
  cur = Math.max(1, cur + delta);
  el.innerText = cur;
}

function addModalProductToCart() {
  if (!state.selectedProduct) return;
  const qty = parseInt(document.getElementById("modalProductQty").innerText) || 1;
  addToCart(state.selectedProduct.id, qty);
  closeProductModal();
  openCartDrawer();
}

function buyNowFromModal() {
  if (!state.selectedProduct) return;
  const qty = parseInt(document.getElementById("modalProductQty").innerText) || 1;
  addToCart(state.selectedProduct.id, qty);
  closeProductModal();
  openCheckoutModal();
}

async function checkDeliveryPincode() {
  const input = document.getElementById("modalPincodeInput");
  const resultBox = document.getElementById("pincodeResultBox");
  if (!input || !resultBox) return;

  const pin = input.value.trim();
  if (!pin || pin.length !== 6) {
    resultBox.className = "mt-2 text-xs text-rose-600 block";
    resultBox.innerHTML = '<i class="fa-solid fa-triangle-exclamation mr-1"></i> Please enter a valid 6-digit Indian pincode';
    return;
  }

  try {
    const res = await fetch("/api/pincode/check", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ pincode: pin }),
    });
    const data = await res.json();
    if (data.deliverable) {
      resultBox.className = "mt-2 text-xs text-emerald-700 bg-emerald-50 p-2.5 rounded-xl border border-emerald-200 block";
      resultBox.innerHTML = `
        <div class="font-bold flex items-center"><i class="fa-solid fa-truck text-emerald-600 mr-1.5"></i> ${data.message}</div>
        <div class="text-[11px] text-emerald-600 mt-0.5">Dispatched via DeoDap Express Logistics</div>
      `;
    } else {
      resultBox.className = "mt-2 text-xs text-rose-600 block";
      resultBox.innerHTML = data.message;
    }
  } catch (e) {
    resultBox.innerHTML = "Error checking pincode.";
  }
}

// Cart Operations
function addToCart(productId, quantity = 1) {
  const product = state.products.find((p) => p.id === productId) || state.selectedProduct;
  if (!product) return;

  const existing = state.cart.find((i) => i.product_id === product.id);
  if (existing) {
    existing.quantity += quantity;
  } else {
    state.cart.push({
      product_id: product.id,
      title: product.title,
      price: product.selling_price,
      wholesale_price: product.wholesale_price,
      mrp: product.mrp,
      image_url: product.image_url,
      quantity: quantity,
      deodap_sku: product.deodap_sku,
    });
  }

  saveCartToStorage();
  showToast(`Added "${product.title.substring(0, 24)}..." to cart!`);
}

function buyNow(productId) {
  addToCart(productId, 1);
  openCheckoutModal();
}

function updateCartQuantity(productId, delta) {
  const item = state.cart.find((i) => i.product_id === productId);
  if (!item) return;

  item.quantity += delta;
  if (item.quantity <= 0) {
    state.cart = state.cart.filter((i) => i.product_id !== productId);
  }

  saveCartToStorage();
}

function removeFromCart(productId) {
  state.cart = state.cart.filter((i) => i.product_id !== productId);
  saveCartToStorage();
  showToast("Item removed from cart");
}

function clearCart() {
  state.cart = [];
  state.appliedCoupon = null;
  saveCartToStorage();
}

function updateCartBadge() {
  const totalQty = state.cart.reduce((sum, i) => sum + i.quantity, 0);
  const badges = document.querySelectorAll(".cart-badge-count");
  badges.forEach((b) => {
    b.innerText = totalQty;
    if (totalQty > 0) {
      b.classList.remove("hidden");
    } else {
      b.classList.add("hidden");
    }
  });
}

// Cart Drawer UI
function openCartDrawer() {
  renderCartDrawer();
  const drawer = document.getElementById("cartDrawer");
  if (drawer) {
    drawer.classList.remove("hidden");
    document.body.classList.add("overflow-hidden");
  }
}

function closeCartDrawer() {
  const drawer = document.getElementById("cartDrawer");
  if (drawer) {
    drawer.classList.add("hidden");
    document.body.classList.remove("overflow-hidden");
  }
}

function renderCartDrawer() {
  const itemsContainer = document.getElementById("cartItemsList");
  const summaryContainer = document.getElementById("cartSummarySection");
  if (!itemsContainer || !summaryContainer) return;

  if (state.cart.length === 0) {
    itemsContainer.innerHTML = `
      <div class="py-20 text-center text-slate-400">
        <i class="fa-solid fa-basket-shopping text-5xl mb-3 text-slate-300"></i>
        <h4 class="text-lg font-bold text-slate-700 mb-1">Your cart is empty</h4>
        <p class="text-xs text-slate-400 mb-4">Discover trending products and add them to your cart.</p>
        <button onclick="closeCartDrawer()" class="px-5 py-2.5 bg-blue-900 text-white rounded-xl text-xs font-bold hover:bg-blue-800 transition">
          Continue Shopping
        </button>
      </div>
    `;
    summaryContainer.classList.add("hidden");
    return;
  }

  summaryContainer.classList.remove("hidden");

  // Render items
  itemsContainer.innerHTML = state.cart
    .map((item) => {
      const margin = (item.price - item.wholesale_price) * item.quantity;
      return `
      <div class="flex items-center space-x-3 p-3 bg-white rounded-xl border border-slate-200 shadow-sm relative group">
        <img src="${item.image_url}" alt="${escapeHtml(item.title)}" class="w-16 h-16 object-contain rounded-lg bg-slate-50 p-1 flex-shrink-0" />
        
        <div class="flex-1 min-w-0">
          <h4 class="text-xs font-bold text-slate-800 line-clamp-1 mb-1" title="${escapeHtml(item.title)}">
            ${escapeHtml(item.title)}
          </h4>
          <div class="flex items-baseline space-x-2">
            <span class="text-sm font-black text-slate-900">₹${item.price}</span>
            <span class="text-[11px] text-slate-400 line-through">₹${item.mrp || item.price * 2}</span>
          </div>

          <!-- Dropship Margin in Cart (Owner Mode) -->
          <div class="owner-only text-[11px] text-emerald-700 font-semibold mt-1">
            DeoDap Base: ₹${item.wholesale_price * item.quantity} | Margin: +₹${margin}
          </div>
        </div>

        <!-- Quantity Stepper -->
        <div class="flex flex-col items-end space-y-2">
          <button 
            onclick="removeFromCart('${item.product_id}')"
            class="text-slate-400 hover:text-rose-500 text-xs transition"
            title="Remove item"
          >
            <i class="fa-regular fa-trash-can"></i>
          </button>

          <div class="flex items-center border border-slate-200 rounded-lg bg-slate-50">
            <button onclick="updateCartQuantity('${item.product_id}', -1)" class="w-6 h-6 flex items-center justify-center text-xs font-bold text-slate-600 hover:bg-slate-200">-</button>
            <span class="w-6 text-center text-xs font-bold text-slate-900">${item.quantity}</span>
            <button onclick="updateCartQuantity('${item.product_id}', 1)" class="w-6 h-6 flex items-center justify-center text-xs font-bold text-slate-600 hover:bg-slate-200">+</button>
          </div>
        </div>
      </div>
    `;
    })
    .join("");

  // Calculate totals
  const subtotal = state.cart.reduce((sum, i) => sum + i.price * i.quantity, 0);
  const wholesaleTotal = state.cart.reduce((sum, i) => sum + i.wholesale_price * i.quantity, 0);

  let discount = 0;
  if (state.appliedCoupon) {
    discount = state.appliedCoupon.discount;
  }

  const shipping = subtotal - discount >= 499 ? 0 : 49;
  const total = Math.max(0, subtotal - discount + shipping);
  const netMargin = total - wholesaleTotal - shipping;

  // Update summary fields
  document.getElementById("cartSubtotal").innerText = `₹${subtotal}`;
  document.getElementById("cartShipping").innerText = shipping === 0 ? "FREE" : `₹${shipping}`;
  document.getElementById("cartDiscountRow").style.display = discount > 0 ? "flex" : "none";
  document.getElementById("cartDiscount").innerText = `-₹${discount}`;
  document.getElementById("cartTotal").innerText = `₹${total}`;

  // Owner mode cart profit
  const ownerProfitEl = document.getElementById("cartOwnerProfit");
  if (ownerProfitEl) {
    ownerProfitEl.innerHTML = `
      <div class="p-2.5 bg-emerald-50 border border-emerald-200 rounded-xl text-emerald-900 text-xs flex justify-between items-center">
        <span><i class="fa-solid fa-sack-dollar text-emerald-600 mr-1"></i> Dropship Profit on this Cart:</span>
        <span class="font-extrabold text-sm text-emerald-800">+₹${netMargin}</span>
      </div>
    `;
  }
}

// Coupon Apply
async function applyCouponCode() {
  const input = document.getElementById("couponInput");
  const msgEl = document.getElementById("couponMessage");
  if (!input) return;

  const code = input.value.trim().toUpperCase();
  if (!code) return;

  const subtotal = state.cart.reduce((sum, i) => sum + i.price * i.quantity, 0);

  try {
    const res = await fetch("/api/coupons/apply", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code: code, subtotal: subtotal }),
    });

    const data = await res.json();
    if (res.ok && data.valid) {
      state.appliedCoupon = { code: data.code, discount: data.discount };
      if (msgEl) {
        msgEl.className = "text-xs text-emerald-600 block mt-1";
        msgEl.innerText = data.message;
      }
      renderCartDrawer();
      showToast(`Coupon ${code} applied successfully!`);
    } else {
      if (msgEl) {
        msgEl.className = "text-xs text-rose-600 block mt-1";
        msgEl.innerText = data.detail || "Invalid coupon code";
      }
    }
  } catch (err) {
    if (msgEl) {
      msgEl.className = "text-xs text-rose-600 block mt-1";
      msgEl.innerText = "Error applying coupon";
    }
  }
}

// Checkout Flow
function openCheckoutModal() {
  if (state.cart.length === 0) {
    showToast("Please add items to your cart first.");
    return;
  }
  closeCartDrawer();
  renderCheckoutSummary();
  document.getElementById("checkoutModal").classList.remove("hidden");
  document.body.classList.add("overflow-hidden");
}

function closeCheckoutModal() {
  document.getElementById("checkoutModal").classList.add("hidden");
  document.body.classList.remove("overflow-hidden");
}

function renderCheckoutSummary() {
  const listEl = document.getElementById("checkoutItemsList");
  if (!listEl) return;

  const subtotal = state.cart.reduce((sum, i) => sum + i.price * i.quantity, 0);
  const discount = state.appliedCoupon ? state.appliedCoupon.discount : 0;
  const shipping = subtotal - discount >= 499 ? 0 : 49;
  const total = Math.max(0, subtotal - discount + shipping);

  listEl.innerHTML = state.cart
    .map(
      (i) => `
      <div class="flex items-center justify-between text-xs py-1.5 border-b border-slate-100">
        <span class="text-slate-700 truncate max-w-[200px]">${i.quantity}x ${escapeHtml(i.title)}</span>
        <span class="font-bold text-slate-900">₹${i.price * i.quantity}</span>
      </div>
    `
    )
    .join("");

  document.getElementById("checkoutSubtotal").innerText = `₹${subtotal}`;
  document.getElementById("checkoutDiscount").innerText = `-₹${discount}`;
  document.getElementById("checkoutShipping").innerText = shipping === 0 ? "FREE" : `₹${shipping}`;
  document.getElementById("checkoutTotal").innerText = `₹${total}`;
}

async function submitOrder(e) {
  e.preventDefault();

  const name = document.getElementById("custName").value.trim();
  const phone = document.getElementById("custPhone").value.trim();
  const email = document.getElementById("custEmail").value.trim();
  const address = document.getElementById("custAddress").value.trim();
  const city = document.getElementById("custCity").value.trim();
  const stateVal = document.getElementById("custState").value.trim();
  const pincode = document.getElementById("custPincode").value.trim();
  const paymentMethod = document.querySelector('input[name="paymentMethod"]:checked').value;

  if (!name || !phone || !address || !city || !stateVal || !pincode) {
    showToast("Please fill in all required shipping fields.");
    return;
  }

  if (phone.length < 10) {
    showToast("Please enter a valid 10-digit phone number.");
    return;
  }

  const payload = {
    customer_name: name,
    customer_phone: phone,
    customer_email: email,
    address: address,
    city: city,
    state: stateVal,
    pincode: pincode,
    payment_method: paymentMethod,
    coupon_code: state.appliedCoupon ? state.appliedCoupon.code : "",
    items: state.cart.map((i) => ({ product_id: i.product_id, quantity: i.quantity })),
  };

  const btn = document.getElementById("placeOrderBtn");
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin mr-2"></i> Processing Order...';
  }

  try {
    const res = await fetch("/api/orders", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.detail || "Failed to place order");
    }

    // Success! Clear cart
    clearCart();
    closeCheckoutModal();
    showOrderConfirmationModal(data);
  } catch (err) {
    alert(err.message);
  } finally {
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = '<span>Confirm & Place Order</span><i class="fa-solid fa-arrow-right ml-2"></i>';
    }
  }
}

// Order Confirmation Modal
function showOrderConfirmationModal(orderData) {
  const modal = document.getElementById("orderConfirmedModal");
  const content = document.getElementById("orderConfirmedContent");
  if (!modal || !content) return;

  const waUrl = orderData.whatsapp_url;

  content.innerHTML = `
    <div class="text-center mb-6">
      <div class="inline-block bg-white p-2 rounded-2xl shadow-sm border border-amber-200 mb-3 max-w-[200px]">
        <img src="/static/images/logo.png" alt="SAGA ONLINE SHOP" class="h-12 w-auto object-contain mx-auto" />
      </div>
      <div class="w-14 h-14 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center text-2xl mx-auto mb-2 shadow-inner">
        <i class="fa-solid fa-check"></i>
      </div>
      <h3 class="text-2xl font-black text-slate-900 mb-1">Order Successfully Placed!</h3>
      <p class="text-xs text-slate-500">Thank you for ordering with SAGA ONLINE SHOP</p>
    </div>

    <!-- Order Meta Box -->
    <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 mb-6">
      <div class="flex items-center justify-between pb-3 border-b border-slate-200/80 mb-3 text-xs">
        <div>
          <span class="text-slate-400">Order ID:</span>
          <span class="font-extrabold text-blue-900 ml-1">#${orderData.order_id}</span>
        </div>
        <div>
          <span class="text-slate-400">Payment:</span>
          <span class="font-bold text-slate-800 ml-1">${orderData.payment_method}</span>
        </div>
      </div>

      <div class="space-y-1.5 text-xs text-slate-600">
        <div><b class="text-slate-900">Customer:</b> ${escapeHtml(orderData.customer_name)} (${orderData.customer_phone})</div>
        <div><b class="text-slate-900">Delivery Address:</b> ${escapeHtml(orderData.address)}</div>
        <div><b class="text-slate-900">Total Paid/COD:</b> <span class="text-sm font-black text-slate-950">₹${orderData.total_amount}</span></div>
        <div class="text-emerald-700 font-semibold pt-1">
          <i class="fa-solid fa-truck-fast mr-1"></i> Dispatched via DeoDap Direct Air Cargo. Tracking: <b>${orderData.tracking_number}</b>
        </div>
      </div>
    </div>

    <!-- WhatsApp Share CTA -->
    <div class="bg-emerald-50 border-2 border-emerald-200 rounded-2xl p-4 mb-6 text-center">
      <div class="flex items-center justify-center space-x-2 text-emerald-800 font-bold text-sm mb-1">
        <i class="fa-brands fa-whatsapp text-2xl text-emerald-600"></i>
        <span>Connect on WhatsApp for Instant Updates</span>
      </div>
      <p class="text-xs text-emerald-700 mb-3">
        Send your Order ID <b>#${orderData.order_id}</b> to our dedicated WhatsApp support at <b>+91 ${WHATSAPP_NUMBER}</b> to track live delivery progress!
      </p>
      <a 
        href="${waUrl}"
        target="_blank"
        rel="noopener noreferrer"
        class="inline-flex items-center justify-center space-x-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-3 px-6 rounded-xl shadow-md transition w-full"
      >
        <i class="fa-brands fa-whatsapp text-base"></i>
        <span>Send Order to WhatsApp (${WHATSAPP_NUMBER})</span>
      </a>
    </div>

    <!-- Actions -->
    <div class="flex space-x-3">
      <button 
        onclick="window.print()"
        class="flex-1 py-2.5 px-4 rounded-xl border border-slate-300 hover:bg-slate-50 text-slate-700 font-bold text-xs flex items-center justify-center space-x-1.5"
      >
        <i class="fa-solid fa-print"></i>
        <span>Print Receipt</span>
      </button>
      <button 
        onclick="closeOrderConfirmationModal()"
        class="flex-1 py-2.5 px-4 rounded-xl bg-blue-900 hover:bg-blue-800 text-white font-bold text-xs"
      >
        Continue Shopping
      </button>
    </div>
  `;

  modal.classList.remove("hidden");
  document.body.classList.add("overflow-hidden");
}

function closeOrderConfirmationModal() {
  document.getElementById("orderConfirmedModal").classList.add("hidden");
  document.body.classList.remove("overflow-hidden");
}

// Track Order Modal
function openTrackingModal() {
  document.getElementById("trackingModal").classList.remove("hidden");
  document.body.classList.add("overflow-hidden");
}

function closeTrackingModal() {
  document.getElementById("trackingModal").classList.add("hidden");
  document.body.classList.remove("overflow-hidden");
}

async function searchTrackOrder() {
  const input = document.getElementById("trackingOrderIdInput");
  const resultBox = document.getElementById("trackingResultBox");
  if (!input || !resultBox) return;

  const id = input.value.trim();
  if (!id) return;

  try {
    const res = await fetch(`/api/orders/${encodeURIComponent(id)}`);
    const data = await res.json();
    if (!res.ok) {
      resultBox.innerHTML = `
        <div class="p-4 bg-rose-50 text-rose-700 rounded-xl text-xs border border-rose-200">
          <i class="fa-solid fa-triangle-exclamation mr-1"></i> Order not found. Please double-check your Order ID.
        </div>
      `;
      return;
    }

    resultBox.innerHTML = `
      <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 text-xs">
        <div class="flex justify-between items-center mb-3 pb-2 border-b border-slate-200">
          <span class="font-bold text-blue-900 text-sm">#${data.order_id}</span>
          <span class="bg-blue-100 text-blue-800 font-bold px-2.5 py-1 rounded-full">${data.status}</span>
        </div>
        <div class="space-y-1 text-slate-600 mb-4">
          <div><b>Customer:</b> ${escapeHtml(data.customer_name)}</div>
          <div><b>Shipping To:</b> ${escapeHtml(data.address)}</div>
          <div><b>Tracking Number:</b> ${data.tracking_number || "DD-EXP-88910"}</div>
          <div><b>Fulfillment:</b> DeoDap Central Logistics Surface Air</div>
        </div>

        <!-- Timeline steps -->
        <div class="relative pl-6 space-y-4 border-l-2 border-blue-600 ml-2">
          <div class="relative">
            <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-blue-600 border-2 border-white"></div>
            <div class="font-bold text-slate-800">Order Confirmed & Verified</div>
            <div class="text-[11px] text-slate-400">Order successfully received by SAGA ONLINE SHOP</div>
          </div>
          <div class="relative">
            <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-blue-600 border-2 border-white"></div>
            <div class="font-bold text-slate-800">Direct DeoDap Warehouse Sourcing</div>
            <div class="text-[11px] text-slate-400">Quality inspection & barcode packaging completed</div>
          </div>
          <div class="relative">
            <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-emerald-500 border-2 border-white animate-pulse"></div>
            <div class="font-bold text-emerald-700">In Transit - Expected Delivery in 2-3 Days</div>
            <div class="text-[11px] text-slate-500">Shipped with BlueDart/Delhivery partner</div>
          </div>
        </div>
      </div>
    `;
  } catch (err) {
    resultBox.innerHTML = "Error fetching order status.";
  }
}

// Dropship Admin & Margin Dashboard Modal
async function openAdminDashboardModal() {
  document.getElementById("adminModal").classList.remove("hidden");
  document.body.classList.add("overflow-hidden");
  loadAdminData();
}

function closeAdminDashboardModal() {
  document.getElementById("adminModal").classList.add("hidden");
  document.body.classList.remove("overflow-hidden");
}

async function loadAdminData() {
  try {
    const [statsRes, ordersRes] = await Promise.all([
      fetch("/api/admin/stats"),
      fetch("/api/admin/orders"),
    ]);

    const stats = await statsRes.json();
    const orders = await ordersRes.json();

    // Render stats
    document.getElementById("adminStatOrders").innerText = stats.total_orders;
    document.getElementById("adminStatRevenue").innerText = `₹${stats.gross_revenue}`;
    document.getElementById("adminStatCogs").innerText = `₹${stats.total_cogs}`;
    document.getElementById("adminStatProfit").innerText = `₹${stats.total_profit} (${stats.profit_margin_percent}%)`;

    // Render orders table
    const tableBody = document.getElementById("adminOrdersTableBody");
    if (!tableBody) return;

    tableBody.innerHTML = orders
      .map(
        (o) => `
        <tr class="border-b border-slate-100 hover:bg-slate-50 text-xs">
          <td class="p-3 font-extrabold text-blue-900">#${o.order_id}</td>
          <td class="p-3">
            <div class="font-semibold text-slate-800">${escapeHtml(o.customer_name)}</div>
            <div class="text-[11px] text-slate-400">${o.customer_phone} (${o.city})</div>
          </td>
          <td class="p-3">
            <span class="font-semibold">${o.items_count} items</span>
          </td>
          <td class="p-3 font-bold text-slate-900">₹${o.total_amount}</td>
          <td class="p-3 font-medium text-slate-600">₹${o.total_wholesale_cost}</td>
          <td class="p-3 font-black text-emerald-700 bg-emerald-50/50">+₹${o.total_margin} (${o.margin_percentage}%)</td>
          <td class="p-3">
            <span class="px-2 py-0.5 rounded-full text-[10px] font-bold ${
              o.status === "Delivered" ? "bg-emerald-100 text-emerald-800" : "bg-blue-100 text-blue-800"
            }">${o.status}</span>
          </td>
          <td class="p-3">
            <button 
              onclick="syncOrderWithDeoDap('${o.order_id}')"
              class="px-2.5 py-1 bg-blue-900 hover:bg-blue-800 text-white rounded-lg text-[10px] font-bold transition whitespace-nowrap"
            >
              <i class="fa-solid fa-arrows-rotate mr-1"></i> Sync DeoDap
            </button>
          </td>
        </tr>
      `
      )
      .join("");
  } catch (err) {
    console.error("Error loading admin data:", err);
  }
}

async function syncOrderWithDeoDap(orderId) {
  try {
    const res = await fetch(`/api/admin/orders/${orderId}/sync-deodap`, { method: "POST" });
    const data = await res.json();
    showToast(data.message);
    loadAdminData();
  } catch (err) {
    showToast("Error syncing to DeoDap");
  }
}

// Utility: Toast notifications
function showToast(msg) {
  const container = document.getElementById("toastContainer");
  if (!container) return;

  const toast = document.createElement("div");
  toast.className =
    "bg-slate-900 text-white text-xs font-semibold px-4 py-2.5 rounded-xl shadow-xl flex items-center space-x-2 border border-slate-700 transition-all transform translate-y-2 opacity-0";
  toast.innerHTML = `<i class="fa-solid fa-circle-check text-emerald-400"></i><span>${escapeHtml(msg)}</span>`;

  container.appendChild(toast);
  requestAnimationFrame(() => {
    toast.classList.remove("translate-y-2", "opacity-0");
  });

  setTimeout(() => {
    toast.classList.add("opacity-0", "translate-y-2");
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

function escapeHtml(text) {
  if (!text) return "";
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function toggleWishlist(id) {
  showToast("Added to your wishlist!");
}
