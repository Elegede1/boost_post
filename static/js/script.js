// Mobile Menu Toggle
const menuBtn = document.querySelector('.mobile-menu-btn');
const navMenu = document.querySelector('.nav-menu');
//Added:
const header = document.querySelector('header');

menuBtn.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    // Added:
    menuBtn.classList.toggle('active');
    header.classList.toggle('active');
});

// Close menu when clicking outside
document.addEventListener('click', (e) => {
    if (!menuBtn.contains(e.target) && !navMenu.contains(e.target)) {
        navMenu.classList.remove('active');
        // Added:
        menuBtn.classList.remove('active');
        header.classList.remove('active');
    }
});

// Dark Mode Toggle
const themeToggle = document.querySelector('.theme-toggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    document.body.setAttribute('data-theme',
        document.body.classList.contains('dark-theme') ? 'dark' : 'light'
    );

    // Save preference
    localStorage.setItem('theme',
        document.body.classList.contains('dark-theme') ? 'dark' : 'light'
    );

    themeToggle.textContent = document.body.classList.contains('dark-theme') ? '🌞' : '🌓';
});

// Load saved theme
const savedTheme = localStorage.getItem('theme') || 'light';
document.body.setAttribute('data-theme', savedTheme);
themeToggle.textContent = savedTheme === 'dark' ? '🌞' : '🌓';