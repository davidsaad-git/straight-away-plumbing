// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');

if (navToggle && mainNav) {
  navToggle.addEventListener('click', () => {
    const open = mainNav.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

// Quote form: no backend connected yet — show a friendly fallback
document.querySelectorAll('form[action="#"]').forEach((form) => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Thanks! Online quotes are coming soon.\n\nFor now, please call us on 0403 322 290 and we’ll help you straight away.');
  });
});
