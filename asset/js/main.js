document.addEventListener("DOMContentLoaded", function () {
  // getting, selcting all element we need
  const collaspedNav = document.querySelectorAll(".__collapse-sm-screen");
  const bringNav = document.querySelectorAll(".btn--navbar");
  const navbar = document.querySelectorAll("nav");

  // looping throught the navbar btn
  bringNav.forEach((btnDropNav) => {
    // listening to navbar dropdown btn
    btnDropNav.addEventListener("click", () => {
      console.log("toggleing Navbar class");

      btnDropNav.querySelectorAll("i").forEach((icon) => {
        icon.classList.toggle("display-none");
      });

      // looping throught navbar collapsed divs for ->
      collaspedNav.forEach((collapseNav) => {
        collapseNav.classList.toggle("active_nav");
      });
    });
  });

  const scrollThreshold = window.innerHeight * 0.3; // 30% of viewport height

  navbar.forEach((navbarC) => {
    window.addEventListener("scroll", function () {
      if (window.scrollY > scrollThreshold) {
        navbarC.classList.add("fixed-navbar"); // Add class when scrolling past 30%
      } else {
        navbarC.classList.remove("fixed-navbar"); // Remove class when scrolling back up
      }
    });
  });
});

// getting all faqs items ------------------------------------
const faqs = document.querySelectorAll(".container-fags-qa");

// looping each Faq container
faqs.forEach((Faq) => {
  const faqItem = Faq.querySelector(".container-a");
  const otherFaq = document.querySelectorAll(".container-a");

  // listening to click event
  Faq.addEventListener("click", () => {
    otherFaq.forEach((otherfaqs) => {
      // if not clicked faq
      if (Faq != otherfaqs) {
        otherfaqs.classList.remove("display-Faq");
        Faq.classList.add("--decrese-height");
      }
    });

    // toggling classList
    faqItem.classList.toggle("display-Faq");
  });
});
