// getting, selcting all element we need
const collaspedNav = document.querySelectorAll(".__collapse-sm-screen");
const bringNav = document.querySelectorAll(".btn--navbar");

// looping throught the navbar btn
bringNav.forEach((btnDropNav) => {
  // listening to navbar dropdown btn
  btnDropNav.addEventListener("click", () => {
    console.log("toggleing Navbar class");

    // looping throught navbar collapsed divs for ->
    collaspedNav.forEach((collapseNav) => {
      collapseNav.classList.toggle("drop-nav");
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
