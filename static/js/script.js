function initScripts() {
  if (typeof Swiper !== "undefined" && document.querySelector(".mySwiper")) {
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

  const faqs = document.querySelectorAll(".faq-item");
  if (faqs.length > 0) {
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

  const bars = document.querySelector(".bars");
  const mobileMenu = document.querySelector(".mobile-menu");
  const closeBtn = document.querySelector(".close-btn");
  if (bars && mobileMenu && closeBtn) {
    bars.addEventListener("click", () => mobileMenu.classList.remove("d-none"));
    closeBtn.addEventListener("click", () => mobileMenu.classList.add("d-none"));
  }

  const searchInput = document.getElementById("searchInput");
  const categorySelect = document.getElementById("categorySelect");
  const projectCards = document.querySelectorAll(".project-card");
  if (searchInput && categorySelect && projectCards.length > 0) {
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

  const form = document.getElementById("application-form");
  const fileInput = document.getElementById("file-upload");
  const fileNameDisplay = document.getElementById("file-name");

  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      alert("Arizangiz muvaffaqiyatli yuborildi!");
      form.reset();
      if (fileNameDisplay) fileNameDisplay.textContent = "";
    });
  }

  if (fileInput && fileNameDisplay) {
    fileInput.addEventListener("change", () => {
      const file = fileInput.files && fileInput.files[0];
      fileNameDisplay.textContent = file ? "File: " + file.name : "";
    });
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initScripts);
} else {
  initScripts();
}
