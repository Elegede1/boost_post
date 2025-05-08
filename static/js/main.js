/*

BEGIN HEADER LAYOUT

*/

// Verify if page contains header

if (document.getElementById("layout-page-header")) {
  // Open and close mobile nav menu

  let baseMobileModalStyle =
    "mobile-nav-bar hidden text-[20px]/[28px] text-white font-light fixed top-0 left-0 h-screen bg-[rgba(0,0,0,0.5)]";
  let baseMobileMenuStyle =
    "h-full bg-black transition-[width] ease-in duration-[300ms] overflow-auto";
  let newMobileModalStyle;
  let newMobileMenuStyle;

  function openMobileMenu() {
    newMobileModalStyle = baseMobileModalStyle + " w-full";
    newMobileMenuStyle =
      baseMobileMenuStyle + " mobile-nav-width w-[50%] p-[15px_20px]";
    document.getElementById("mobile-modal-container").className =
      newMobileModalStyle;
    document.getElementById("mobile-menu-container").className =
      newMobileMenuStyle;
    document.body.style.overflowY = "hidden";
  }

  function closeMobileMenu() {
    newMobileModalStyle =
      baseMobileModalStyle + " w-[0%] overflow-hidden opacity-0";
    newMobileMenuStyle = baseMobileMenuStyle + " w-[150px]";
    document.getElementById("mobile-modal-container").className =
      newMobileModalStyle;
    document.getElementById("mobile-menu-container").className =
      newMobileMenuStyle;
    document.body.style.overflowY = "visible";
  }

  function handleCloseClick(e) {
    e.target === e.currentTarget ? closeMobileMenu() : null;
  }

  // Reduce navbar while scrolling

  let baseHeaderWhiteStyle =
    "header-inner flex items-center justify-between pl-[36px] pr-[66px] transition-[padding-block] ease-in duration-[300ms]";
  let baseHeaderBlackStyle =
    "h-[50px] bg-black transition-[height] ease-in duration-[300ms]";
  let newHeaderWhiteStyle;
  let newHeaderBlackStyle;

  function handleScroll() {
    if (window.scrollY >= 2) {
      newHeaderWhiteStyle =
        baseHeaderWhiteStyle + " py-[10px] reduce-container-padding";
      newHeaderBlackStyle = baseHeaderBlackStyle + " reduce-container-height";
      document.getElementById("header-white-container").className =
        newHeaderWhiteStyle;
      document.getElementById("header-black-container").className =
        newHeaderBlackStyle;
    } else {
      newHeaderWhiteStyle = baseHeaderWhiteStyle + " py-[24px]";
      newHeaderBlackStyle = baseHeaderBlackStyle;
      document.getElementById("header-white-container").className =
        newHeaderWhiteStyle;
      document.getElementById("header-black-container").className =
        newHeaderBlackStyle;
    }
  }

  window.addEventListener("scroll", handleScroll);
}

/*

END HEADER LAYOUT

*/

/*

BEGIN ABOUT US PAGE

*/

// Verify if the page is the About Us page

if (document.getElementById("about-us-page")) {
  // Handle faq accordion
  let baseFAQStyle = "bg-white rounded-[15px]";
  let newFAQStyle;

  function handleAccordion(e) {
    if (
      e.currentTarget.parentElement
        .closest("div")
        .className.includes("open-faq")
    ) {
      newFAQStyle = baseFAQStyle;
      e.currentTarget.parentElement.closest("div").className = newFAQStyle;
    } else {
      newFAQStyle = baseFAQStyle + " open-faq";
      e.currentTarget.parentElement.closest("div").className = newFAQStyle;
    }
  }
}

/*

END ABOUT US PAGE

*/

/*

BEGIN COMMUNITY PAGE

*/

if (document.getElementById("community-page")) {
  function toggleSearchBar() {
    searchBar = document.getElementById("community-toggle-search-bar");
    if (
      searchBar.className.includes(
        "sm:p-[10.6px_29px_11.6px] p-[10.6px_29px_11.6px_18px]"
      )
    ) {
      searchBar.className =
        "absolute top-0 left-0 bg-white shadow-[4px_4px_4px_0px_rgba(0,0,0,0.2)] lg:hidden flex w-[0px] overflow-hidden";
    } else {
      searchBar.className =
        "absolute top-0 left-0 bg-white sm:p-[10.6px_29px_11.6px] p-[10.6px_29px_11.6px_18px] transition-[width] ease-in duration-[300ms] shadow-[4px_4px_4px_0px_rgba(0,0,0,0.2)] lg:hidden flex w-full overflow-hidden";
    }
  }

  const form = document.getElementById("desktop-search-form");
  const input = document.getElementById("desktop-search-input");

  form.addEventListener("click", () => {
    if (document.activeElement !== input) {
      input.focus();
    }
  });
}

/*

END COMMUNITY PAGE

*/
