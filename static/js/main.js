/*

BEGIN HEADER LAYOUT

*/

// Verify if page contains header

if (document.getElementById("layout-page-header")) {
  // Open and close mobile nav menu

  let mobileMenu = false;
  let baseMobileModalStyle =
    "mobile-nav-bar hidden text-[20px]/[28px] text-white font-light fixed top-0 left-0 h-screen bg-[rgba(0,0,0,0.5)]";
  let baseMobileMenuStyle =
    "h-full bg-black transition-[width] ease-in duration-[300ms] overflow-auto";
  let newMobileModalStyle;
  let newMobileMenuStyle;

  function openMobileMenu() {
    mobileMenu = true;
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
    mobileMenu = false;
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

  let scrolledDown = false;
  let baseHeaderWhiteStyle =
    "header-inner flex items-center justify-between pl-[36px] pr-[66px] transition-[padding-block] ease-in duration-[300ms]";
  let baseHeaderBlackStyle =
    "h-[50px] bg-black transition-[height] ease-in duration-[300ms]";
  let newHeaderWhiteStyle;
  let newHeaderBlackStyle;

  function handleScroll() {
    if (window.scrollY >= 2) {
      scrolledDown = true;
      newHeaderWhiteStyle =
        baseHeaderWhiteStyle + " py-[10px] reduce-container-padding";
      newHeaderBlackStyle = baseHeaderBlackStyle + " reduce-container-height";
      document.getElementById("header-white-container").className =
        newHeaderWhiteStyle;
      document.getElementById("header-black-container").className =
        newHeaderBlackStyle;
    } else {
      scrolledDown = false;
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
