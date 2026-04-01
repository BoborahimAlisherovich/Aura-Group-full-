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
      const targetPath = `/${targetLang}${normalizedPath.startsWith('/') ? normalizedPath : '/' + normalizedPath}`.replace('//', '/');
      const targetUrl = `${targetPath}${window.location.search}${window.location.hash}`;

      overlay.classList.add("is-active");
      window.setTimeout(() => {
        window.location.href = targetUrl;
      }, 320);
    });
  });
}

function initLangDropdown() {
  const dropdown = document.querySelector(".lang-dropdown");
  if (!dropdown) return;
  const toggle = dropdown.querySelector(".lang-dropdown-toggle");
  if (!toggle) return;

  // Mobile: toggle on click
  toggle.addEventListener("click", function (e) {
    e.stopPropagation();
    dropdown.classList.toggle("open");
  });

  // Close when clicking outside
  document.addEventListener("click", function (e) {
    if (!dropdown.contains(e.target)) {
      dropdown.classList.remove("open");
    }
  });

  window.addEventListener("pageshow", () => {
    const overlay = document.querySelector(".page-transition-overlay");
    if (overlay) overlay.classList.remove("is-active");
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
  initLangDropdown();
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

function init3DTilt() {
  const tiltElements = document.querySelectorAll(".js-3d-tilt");
  if (!tiltElements.length) return;

  tiltElements.forEach(el => {
    el.addEventListener("mousemove", (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * -15;
      const rotateY = ((x - centerX) / centerX) * 15;

      el.style.transform = `perspective(1200px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
    });

    el.addEventListener("mouseleave", () => {
      el.style.transform = "perspective(1200px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)";
    });
  });
}

function initAppleReveal() {
  const revealNodes = document.querySelectorAll(".reveal-apple, .reveal-apple-slide-up, .reveal-apple-scale, .reveal-apple-delayed");
  if (!revealNodes.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

  revealNodes.forEach(node => observer.observe(node));
}

document.addEventListener("DOMContentLoaded", () => {
  setTimeout(() => {
    init3DTilt();
    initAppleReveal();
  }, 100);
});

 
 f u n c t i o n   i n i t W o w E f f e c t s ( )   { 
     / /   P r e l o a d e r 
     c o n s t   p r e l o a d e r   =   d o c u m e n t . g e t E l e m e n t B y I d ( " w o w - p r e l o a d e r " ) ; 
     i f   ( p r e l o a d e r )   { 
         w i n d o w . a d d E v e n t L i s t e n e r ( " l o a d " ,   ( )   = >   { 
             s e t T i m e o u t ( ( )   = >   { 
                 p r e l o a d e r . c l a s s L i s t . a d d ( " l o a d e d " ) ; 
             } ,   1 5 0 0 ) ;   / /   g i v e   i t   a   c o o l   l o a d i n g   t i m e 
         } ) ; 
     } 
 
     / /   C u s t o m   C u r s o r 
     c o n s t   c u r s o r   =   d o c u m e n t . g e t E l e m e n t B y I d ( " w o w C u r s o r " ) ; 
     c o n s t   f o l l o w e r   =   d o c u m e n t . g e t E l e m e n t B y I d ( " w o w C u r s o r F o l l o w e r " ) ; 
     i f   ( c u r s o r   & &   f o l l o w e r )   { 
         l e t   p o s X   =   0 ,   p o s Y   =   0 ,   m o u s e X   =   0 ,   m o u s e Y   =   0 ; 
         
         / /   F o l l o w e r   a n i m a t i o n   l o o p 
         c o n s t   u p d a t e F o l l o w e r   =   ( )   = >   { 
             p o s X   + =   ( m o u s e X   -   p o s X )   *   0 . 1 5 ; 
             p o s Y   + =   ( m o u s e Y   -   p o s Y )   *   0 . 1 5 ; 
             f o l l o w e r . s t y l e . t r a n s f o r m   =   ` t r a n s l a t e ( $ { p o s X } p x ,   $ { p o s Y } p x ) ` ; 
             r e q u e s t A n i m a t i o n F r a m e ( u p d a t e F o l l o w e r ) ; 
         } ; 
         u p d a t e F o l l o w e r ( ) ; 
 
         w i n d o w . a d d E v e n t L i s t e n e r ( " m o u s e m o v e " ,   ( e )   = >   { 
             m o u s e X   =   e . c l i e n t X ; 
             m o u s e Y   =   e . c l i e n t Y ; 
             c u r s o r . s t y l e . t r a n s f o r m   =   ` t r a n s l a t e ( $ { m o u s e X } p x ,   $ { m o u s e Y } p x ) ` ; 
         } ) ; 
 
         / /   H o v e r   e f f e c t   o n   l i n k s   a n d   b u t t o n s 
         c o n s t   h o v e r E l e m e n t s   =   d o c u m e n t . q u e r y S e l e c t o r A l l ( " a ,   b u t t o n ,   . m a g n e t - t a r g e t " ) ; 
         h o v e r E l e m e n t s . f o r E a c h ( e l   = >   { 
             e l . a d d E v e n t L i s t e n e r ( " m o u s e e n t e r " ,   ( )   = >   { 
                 c u r s o r . c l a s s L i s t . a d d ( " h o v e r i n g " ) ; 
                 f o l l o w e r . c l a s s L i s t . a d d ( " h o v e r i n g " ) ; 
             } ) ; 
             e l . a d d E v e n t L i s t e n e r ( " m o u s e l e a v e " ,   ( )   = >   { 
                 c u r s o r . c l a s s L i s t . r e m o v e ( " h o v e r i n g " ) ; 
                 f o l l o w e r . c l a s s L i s t . r e m o v e ( " h o v e r i n g " ) ; 
             } ) ; 
         } ) ; 
     } 
 } 
 
 / /   E n s u r e   W o w   E f f e c t s   r u n 
 i f   ( d o c u m e n t . r e a d y S t a t e   = = =   " l o a d i n g " )   { 
     d o c u m e n t . a d d E v e n t L i s t e n e r ( " D O M C o n t e n t L o a d e d " ,   i n i t W o w E f f e c t s ) ; 
 }   e l s e   { 
     i n i t W o w E f f e c t s ( ) ; 
 } 
 
 