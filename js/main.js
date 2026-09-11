// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');

if (navToggle && mainNav) {
  navToggle.addEventListener('click', () => {
    const open = mainNav.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

// Floating call button: only reveal it once the page's banner is scrolled past
const floatCall = document.querySelector('.float-call');
const banner = document.querySelector('.hero, .page-hero');

if (floatCall && banner && 'IntersectionObserver' in window) {
  const observer = new IntersectionObserver(
    ([entry]) => floatCall.classList.toggle('is-visible', !entry.isIntersecting),
    { threshold: 0 }
  );
  observer.observe(banner);
} else if (floatCall) {
  floatCall.classList.add('is-visible');
}

// Quote forms: submit via AJAX so visitors stay on the page, then show a popup
function showFormModal(ok) {
  const overlay = document.createElement('div');
  overlay.className = 'form-modal-overlay';
  overlay.innerHTML = ok
    ? '<div class="form-modal"><div class="fm-icon">✅</div><h3>Request sent!</h3><p>Thanks — we\'ve got your quote request and we\'ll get back to you straight away.</p><button class="btn btn-primary" type="button">Close</button></div>'
    : '<div class="form-modal"><div class="fm-icon">⚠️</div><h3>Something went wrong</h3><p>Your request didn\'t go through. Please try again, or call us on <a href="tel:0403322290"><strong>0403 322 290</strong></a>.</p><button class="btn btn-primary" type="button">Close</button></div>';
  const close = () => overlay.remove();
  overlay.addEventListener('click', (e) => { if (e.target === overlay) close(); });
  overlay.querySelector('button').addEventListener('click', close);
  document.body.appendChild(overlay);
}

document.querySelectorAll('form[action*="formspree.io"]').forEach((form) => {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const original = btn.textContent;
    btn.disabled = true;
    btn.textContent = 'Sending…';
    try {
      const res = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' },
      });
      if (res.ok) form.reset();
      showFormModal(res.ok);
    } catch (err) {
      showFormModal(false);
    }
    btn.disabled = false;
    btn.textContent = original;
  });
});
