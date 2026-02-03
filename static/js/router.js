const routes = {
  "/": "/pages/Home.html",
  "/services": "/pages/Services.html",
  "/portfolio": "/pages/Portfolio.html",
  "/portfolioDetails": "/pages/PortfolioDetails.html",
  "/about": "/pages/About.html",
  "/careers": "/pages/Careers.html",
  "/contact": "/pages/Contact.html",
  "/details": "/pages/ProductDetails.html",
};

function getPath() {
  // 🔹 faqat path qismini olish (id=... ni olib tashlash)
  const hash = location.hash.slice(1); // masalan: /details?id=2
  const path = hash.split("?")[0]; // → faqat /details qismi
  return path || "/";
}
// Sahifa yuklanganda
async function loadPage() {
  const pathname = getPath();
  const route = routes[pathname] || routes["/"];
  const html = await fetch(route).then((res) => res.text());
  document.getElementById("app").innerHTML = html;

  if (typeof initScripts === "function") {
    initScripts();
  }
}

// Link bosilganda
document.addEventListener("click", (e) => {
  if (e.target.matches("[data-link]")) {
    e.preventDefault();

    const href = e.target.getAttribute("href"); // #/about, #/portfolio
    location.hash = href; // 🟢 hash o‘zgardi → hashchange event ishga tushadi

    // agar mobil menyu bo‘lsa, uni yopish
    const mobileMenu = document.querySelector(".mobile-menu");
    if (mobileMenu) mobileMenu.classList.add("d-none");
  }
});

window.addEventListener("hashchange", loadPage);

loadPage();
