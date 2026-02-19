function initNavbarState() {
  const navbar = document.getElementById("mainNavbar");
  if (!navbar) return;

  const setState = () => {
    if (window.scrollY > 24) {
      navbar.classList.add("scrolled");
    } else {
      navbar.classList.remove("scrolled");
    }
  };

  setState();
  window.addEventListener("scroll", setState, { passive: true });
}

function initBackToTop() {
  const backToTop = document.getElementById("backToTop");
  if (!backToTop) return;

  const onScroll = () => {
    backToTop.classList.toggle("show", window.scrollY > 360);
  };

  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
  backToTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
}

function initRevealAnimations() {
  const revealNodes = document.querySelectorAll(".reveal");
  if (!revealNodes.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.14, rootMargin: "0px 0px -8% 0px" }
  );

  revealNodes.forEach((node) => observer.observe(node));
}

function initParallax() {
  const layers = document.querySelectorAll(".parallax-layer");
  if (!layers.length) return;

  window.addEventListener(
    "mousemove",
    (event) => {
      const x = event.clientX / window.innerWidth - 0.5;
      const y = event.clientY / window.innerHeight - 0.5;
      layers.forEach((layer) => {
        const speed = Number(layer.dataset.speed || 0.05);
        layer.style.transform = `translate3d(${x * speed * 32}px, ${y * speed * 32}px, 0)`;
      });
    },
    { passive: true }
  );
}

function initMagneticButtons() {
  const nodes = document.querySelectorAll(".magnet-target");
  if (!nodes.length) return;

  nodes.forEach((node) => {
    node.addEventListener("mousemove", (event) => {
      const rect = node.getBoundingClientRect();
      const x = event.clientX - rect.left - rect.width / 2;
      const y = event.clientY - rect.top - rect.height / 2;
      node.style.transform = `translate(${x * 0.12}px, ${y * 0.12}px)`;
    });
    node.addEventListener("mouseleave", () => {
      node.style.transform = "";
    });
  });
}

function initPortfolioPreview() {
  const cards = document.querySelectorAll(".js-case-card");
  const image = document.getElementById("portfolioPreviewImage");
  const title = document.getElementById("portfolioPreviewTitle");
  const category = document.getElementById("portfolioPreviewCategory");
  const metric = document.getElementById("portfolioPreviewMetric");
  const link = document.getElementById("portfolioPreviewLink");

  if (!cards.length || !image || !title || !category || !metric || !link) return;

  const updatePreview = (card) => {
    cards.forEach((item) => item.classList.remove("is-active"));
    card.classList.add("is-active");

    image.classList.add("is-updating");
    window.setTimeout(() => {
      image.src = card.dataset.previewImage || image.src;
      title.textContent = card.dataset.previewTitle || "";
      category.textContent = card.dataset.previewCategory || "";
      metric.textContent = card.dataset.previewMetric || "";
      link.href = card.dataset.previewLink || "#";
      image.classList.remove("is-updating");
    }, 120);
  };

  cards.forEach((card) => {
    card.addEventListener("mouseenter", () => updatePreview(card));
    card.addEventListener("focusin", () => updatePreview(card));
  });

  updatePreview(cards[0]);
}

function initLanguageTransition() {
  const links = document.querySelectorAll(".js-lang-link");
  const overlay = document.querySelector(".page-transition-overlay");
  if (!links.length || !overlay) return;

  const pathNoLang = () => {
    const path = window.location.pathname.replace(/^\/(uz|ru|en)(?=\/|$)/, "");
    return path.startsWith("/") ? path : `/${path}`;
  };

  links.forEach((link) => {
    link.addEventListener("click", (event) => {
      const targetLang = link.dataset.lang;
      if (!targetLang || link.classList.contains("active")) return;
      event.preventDefault();

      const basePath = pathNoLang();
      const normalizedPath = basePath === "" ? "/" : basePath;
      const targetPath =
        targetLang === "uz" ? normalizedPath : `/${targetLang}${normalizedPath}`;
      const targetUrl = `${targetPath}${window.location.search}${window.location.hash}`;

      overlay.classList.add("is-active");
      window.setTimeout(() => {
        window.location.href = targetUrl;
      }, 320);
    });
  });

  window.addEventListener("pageshow", () => {
    overlay.classList.remove("is-active");
  });
}

function initLegacyFaq() {
  const faqs = document.querySelectorAll(".faq-item");
  if (!faqs.length) return;

  faqs.forEach((faq) => {
    const header = faq.querySelector(".faq-header");
    const toggle = faq.querySelector(".faq-toggle");
    if (!header || !toggle) return;

    header.addEventListener("click", () => {
      faqs.forEach((item) => {
        if (item !== faq) {
          item.classList.remove("active");
          const itemToggle = item.querySelector(".faq-toggle");
          if (itemToggle) itemToggle.textContent = "+";
        }
      });

      faq.classList.toggle("active");
      toggle.textContent = faq.classList.contains("active") ? "-" : "+";
    });
  });
}

function initLegacyPortfolioFilter() {
  const searchInput = document.getElementById("searchInput");
  const categorySelect = document.getElementById("categorySelect");
  const projectCards = document.querySelectorAll(".project-card");
  if (!searchInput || !categorySelect || !projectCards.length) return;

  const filterProjects = () => {
    const searchText = searchInput.value.toLowerCase();
    const selectedCategory = categorySelect.value;
    projectCards.forEach((card) => {
      const titleElement = card.querySelector(".card-title");
      const title = titleElement ? titleElement.textContent.toLowerCase() : "";
      const category = card.getAttribute("data-category");
      const matchesSearch = title.includes(searchText);
      const matchesCategory = selectedCategory === "all" || category === selectedCategory;
      card.style.display = matchesSearch && matchesCategory ? "block" : "none";
    });
  };

  searchInput.addEventListener("input", filterProjects);
  categorySelect.addEventListener("change", filterProjects);
}

function initLegacyFormHelpers() {
  const form = document.getElementById("application-form");
  const fileInput = document.getElementById("file-upload");
  const fileNameDisplay = document.getElementById("file-name");

  if (form) {
    form.addEventListener("submit", () => {
      if (fileNameDisplay) fileNameDisplay.textContent = "";
    });
  }

  if (fileInput && fileNameDisplay) {
    fileInput.addEventListener("change", () => {
      const file = fileInput.files && fileInput.files[0];
      fileNameDisplay.textContent = file ? `File: ${file.name}` : "";
    });
  }
}

function initLegacySwiper() {
  if (typeof Swiper === "undefined" || !document.querySelector(".mySwiper")) return;

  new Swiper(".mySwiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
}

function initHomePortfolioSlider() {
  if (typeof Swiper === "undefined" || !document.querySelector(".portfolio-home-swiper")) return;

  new Swiper(".portfolio-home-swiper", {
    speed: 650,
    spaceBetween: 18,
    slidesPerView: 4,
    loop: true,
    autoplay: {
      delay: 2600,
      disableOnInteraction: false,
      pauseOnMouseEnter: true,
    },
    navigation: {
      nextEl: ".portfolio-nav-next",
      prevEl: ".portfolio-nav-prev",
    },
    pagination: {
      el: ".portfolio-home-pagination",
      clickable: true,
    },
    breakpoints: {
      0: { slidesPerView: 1 },
      576: { slidesPerView: 2 },
      992: { slidesPerView: 3 },
      1200: { slidesPerView: 4 },
    },
  });
}

function initScripts() {
  if (typeof AOS !== "undefined") {
    AOS.init({ duration: 700, easing: "ease-out", once: true });
  }

  initNavbarState();
  initBackToTop();
  initRevealAnimations();
  initParallax();
  initMagneticButtons();
  initPortfolioPreview();
  initLanguageTransition();
  initLegacyFaq();
  initLegacyPortfolioFilter();
  initLegacyFormHelpers();
  initLegacySwiper();
  initHomePortfolioSlider();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initScripts);
} else {
  initScripts();
}
