function initScripts() {
  if (document.querySelector(".mySwiper")) {
    var swiper = new Swiper(".mySwiper", {
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
      if (header) {
        header.addEventListener("click", () => {
          faqs.forEach((item) => {
            if (item !== faq) {
              item.classList.remove("active");
              item.querySelector(".faq-toggle").textContent = "+";
            }
          });

          faq.classList.toggle("active");
          const toggle = faq.querySelector(".faq-toggle");
          toggle.textContent = faq.classList.contains("active") ? "×" : "+";
        });
      }
    });
  }

  const bars = document.querySelector(".bars");
  const mobileMenu = document.querySelector(".mobile-menu");
  const closeBtn = document.querySelector(".close-btn");

  if (bars && mobileMenu && closeBtn) {
    bars.addEventListener("click", () => {
      mobileMenu.classList.remove("d-none");
    });

    closeBtn.addEventListener("click", () => {
      mobileMenu.classList.add("d-none");
    });
  }

  const searchInput = document.getElementById("searchInput");
  const categorySelect = document.getElementById("categorySelect");
  const projectCards = document.querySelectorAll(".project-card");

  if (searchInput && categorySelect && projectCards.length > 0) {
    function filterProjects() {
      const searchText = searchInput.value.toLowerCase();
      const selectedCategory = categorySelect.value;

      projectCards.forEach((card) => {
        const title = card
          .querySelector(".card-title")
          .textContent.toLowerCase();
        const category = card.getAttribute("data-category");

        const matchesSearch = title.includes(searchText);
        const matchesCategory =
          selectedCategory === "all" || category === selectedCategory;

        card.style.display =
          matchesSearch && matchesCategory ? "block" : "none";
      });
    }

    searchInput.addEventListener("input", filterProjects);
    categorySelect.addEventListener("change", filterProjects);
  }
  // document.addEventListener("click", (e) => {
  //   if (e.target.matches(".book-btn")) {
  //     const id = e.target.dataset.id;
  //     location.hash = `/${id}`;
  //   }
  // });

  // const params = new URLSearchParams(location.hash.split("?")[1]);
  // const page = location.hash.split("?")[0].replace("#/", "");
  // const id = params.get("id");
  // const services = {
  //   1: {
  //     title: "Machine Learning Solutions",
  //     desc: "Custom ML models designed and optimized for your specific business challenges, leveraging cutting-edge deep learning techniques.",
  //     category: "machine",
  //   },
  //   2: {
  //     title: "Blockchain Development",
  //     desc: "End-to-end blockchain solutions from smart contract development to decentralized application architecture.",
  //     category: "web",
  //   },
  //   3: {
  //     title: "Algorithmic Trading",
  //     desc: "Advanced trading algorithms and systems leveraging ML for market analysis and automated execution.",
  //     category: "web",
  //   },
  //   4: {
  //     title: "Data Engineering",
  //     desc: "Build robust data infrastructure that scales with your business needs using modern data engineering practices.",
  //     category: "data",
  //   },
  //   5: {
  //     title: "Predictive Analytics",
  //     desc: "Transform your data into actionable insights with our advanced predictive modeling and forecasting solutions.",
  //     category: "data",
  //   },
  //   6: {
  //     title: "MLOps & Infrastructure",
  //     desc: "Enterprise-grade infrastructure for deploying and managing ML models in production environments.",
  //     category: "machine",
  //   },
  // };

  const service = services[id];
  if (page == "details") {
    if (service) {
      document.querySelector(".service-title").textContent = service.title;
      document.querySelector(".service-desc").textContent = service.desc;
    } else {
      document.querySelector("#product-detail").innerHTML =
        "<h2 class='text-center mt-5'>Service not found 😕</h2>";
    }
    const productSelect = document.querySelector(".form-select");
    productSelect.value = service.category;
  }

  const form = document.getElementById("application-form");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      alert("✅ Arizangiz muvaffaqiyatli yuborildi!");
      form.reset();
      fileNameDisplay.textContent = "";
    });
  }
  const fileInput = document.getElementById("file-upload");
  const fileNameDisplay = document.getElementById("file-name");

  if (fileInput) {
    fileInput.addEventListener("change", () => {
      const file = fileInput.files[0];
      if (file) {
        fileNameDisplay.textContent = `📄 ${file.name}`;
      } else {
        fileNameDisplay.textContent = "";
      }
    });
  }
  // document.addEventListener("click", (e) => {
  //   const card = e.target.closest(".project-card");
  //   if (card) {
  //     const id = card.dataset.id;
  //     location.hash = `/${id}`;
  //   }
  // });

  // const portfolioParams = new URLSearchParams(location.hash.split("?")[1]);
  // const portfolioPage = location.hash.split("?")[0].replace("#/", "");
  // const portfolioId = portfolioParams.get("id");
  // const portfolioData = {
  //   1: {
  //     title: "MachineLearningProject",
  //     desc: "AI project using ML models and data training with TensorFlow and Keras.",
  //     img: "./image/portfolio-1.png",
  //     category: "machine",
  //   },
  //   2: {
  //     title: "ProjectLoremIpsum",
  //     desc: "Blockchain-based data analytics system with secure smart contracts.",
  //     img: "./image/portfolio-2.png",
  //     category: "data",
  //   },
  //   3: {
  //     title: "FrontendDevelopment",
  //     desc: "Responsive web UI built with HTML, CSS, and JavaScript.",
  //     img: "./image/portfolio-3.png",
  //     category: "web",
  //   },
  //   4: {
  //     title: "DataPipelineProject",
  //     desc: "ETL automation pipeline for large-scale data processing.",
  //     img: "./image/portfolio-4.png",
  //     category: "data",
  //   },
  //   5: {
  //     title: "NeuralNetworkAI",
  //     desc: "Simulation of neural networks and training models for AI research.",
  //     img: "./image/portfolio-5.png",
  //     category: "machine",
  //   },
  //   6: {
  //     title: "FullstackApp",
  //     desc: "MERN stack web application with RESTful backend API.",
  //     img: "./image/portfolio-6.png",
  //     category: "web",
  //   },
  // };

  
  if (
    portfolioPage === "portfolioDetails" &&
    document.getElementById("portfolio-title")
  ) {
    const project = portfolioData[portfolioId];
    if (project) {
      document.getElementById("portfolio-title").textContent = project.title;
      document.getElementById("portfolio-desc").textContent = project.desc;
      document.getElementById("portfolio-img").src = project.img;
      document.getElementById("portfolio-category").textContent =
        project.category;
    } else {
      document.querySelector(".portfolio-details").innerHTML =
        "<h2 class='text-center text-danger mt-5'>Project not found 😕</h2>";
    }
  }
}
