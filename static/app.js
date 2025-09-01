document.addEventListener("DOMContentLoaded", function () {
  // --- Navigation ---
  const navLinks = document.querySelectorAll(".nav-link");
  const mobileMenuToggle = document.getElementById("mobileMenuToggle");
  const mainNav = document.getElementById("mainNav");

  function setActiveLink(pageId) {
    navLinks.forEach((link) => {
      if (link.getAttribute("data-page") === pageId) {
        link.classList.add("active-section");
      } else {
        link.classList.remove("active-section");
      }
    });
  }

  // Set initial active link
  const initialPage = window.location.href.split("/")[3] || "home";
  setActiveLink(initialPage);

  // --- Mobile Menu Toggle ---
  if (mobileMenuToggle && mainNav) {
    mobileMenuToggle.addEventListener("click", () => {
      mainNav.classList.toggle("active"); // toggle nav visibility
      mobileMenuToggle.classList.toggle("open"); // animate hamburger to "X"
    });
  }

  // Close menu when a nav link is clicked (for mobile)
  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      mainNav.classList.remove("active");
      mobileMenuToggle.classList.remove("open");
    });
  });

  // --- Hero Carousel ---
  const heroSlides = document.querySelectorAll(".hero-slide");
  const carouselPrev = document.getElementById("carouselPrev");
  const carouselNext = document.getElementById("carouselNext");
  const indicators = document.querySelectorAll(".indicator");

  let currentSlide = 0;
  let autoPlayInterval;

  function showSlide(index) {
    if (index < 0) index = heroSlides.length - 1;
    if (index >= heroSlides.length) index = 0;

    heroSlides.forEach((slide, i) => {
      slide.classList.toggle("active", i === index);
    });
    indicators.forEach((indicator, i) => {
      indicator.classList.toggle("active", i === index);
    });

    currentSlide = index;

    // restart autoplay whenever slide is manually changed
    stopAutoPlay();
    startAutoPlay();
  }

  function nextSlide() {
    const next = (currentSlide + 1) % heroSlides.length;
    showSlide(next);
  }

  function prevSlide() {
    const prev = (currentSlide - 1 + heroSlides.length) % heroSlides.length;
    showSlide(prev);
  }

  function startAutoPlay() {
    if (autoPlayInterval) clearInterval(autoPlayInterval);
    autoPlayInterval = setInterval(() => {
      nextSlide();
    }, 5000);
  }

  function stopAutoPlay() {
    if (autoPlayInterval) clearInterval(autoPlayInterval);
  }

  // Event listeners for buttons
  if (carouselNext) {
    carouselNext.addEventListener("click", (e) => {
      e.preventDefault();
      stopAutoPlay();
      nextSlide();
      startAutoPlay();
    });
  }

  if (carouselPrev) {
    carouselPrev.addEventListener("click", (e) => {
      e.preventDefault();
      stopAutoPlay();
      prevSlide();
      startAutoPlay();
    });
  }

  // Indicator click
  indicators.forEach((indicator, index) => {
    indicator.addEventListener("click", (e) => {
      e.preventDefault();
      stopAutoPlay();
      showSlide(index);
      startAutoPlay();
    });
  });

  // Initialize
  if (heroSlides.length > 0) {
    showSlide(0);
    startAutoPlay();
  }
});
