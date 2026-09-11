// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');

if (navToggle && mainNav) {
  navToggle.addEventListener('click', () => {
    const open = mainNav.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

// Floating call button: reveal it once the quote form reaches the top of the
// screen. Pages with no form fall back to their banner being scrolled past.
const floatCall = document.querySelector('.float-call');
const quoteForm = document.querySelector('.quote-card');
const trigger = quoteForm || document.querySelector('.hero, .page-hero');

if (floatCall && trigger) {
  const reached = quoteForm
    ? (rect) => rect.top <= 0
    : (rect) => rect.bottom <= 0;

  let queued = false;
  const update = () => {
    queued = false;
    floatCall.classList.toggle('is-visible', reached(trigger.getBoundingClientRect()));
  };
  const onScroll = () => {
    if (!queued) {
      queued = true;
      requestAnimationFrame(update);
    }
  };

  update();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
} else if (floatCall) {
  floatCall.classList.add('is-visible');
}

// Instagram: swap the built-in tiles for the live Behold feed once it loads.
// The tiles already in the HTML stay put as the fallback, so the section still
// shows real work if the feed is slow, rate-limited or unavailable.
const instaGrid = document.querySelector('.insta-grid');

if (instaGrid && 'fetch' in window) {
  const FEED_URL = 'https://feeds.behold.so/rF2mFXV2UAcRoEFfkhDG';

  const IG_GLYPH =
    '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.6" y="2.6" width="18.8" height="18.8" rx="5.4"/>' +
    '<circle cx="12" cy="12" r="4.4"/><circle class="dot" cx="17.8" cy="6.2" r="1.25"/></svg>';

  const BADGES = {
    VIDEO:
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M8 5.2v13.6L19 12z"/></svg>',
    CAROUSEL_ALBUM:
      '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#fff" stroke-width="2.2" stroke-linejoin="round">' +
      '<rect x="8.5" y="2.5" width="13" height="13" rx="3"/><rect x="2.5" y="8.5" width="13" height="13" rx="3"/></svg>',
  };

  const tileFor = (post) => {
    const sizes = post.sizes || {};
    const source = sizes.medium || sizes.large || sizes.small;
    const src = (source && source.mediaUrl) || post.mediaUrl;
    if (!src || !post.permalink) return null;

    const link = document.createElement('a');
    link.className = 'insta-tile';
    link.href = post.permalink;
    link.target = '_blank';
    link.rel = 'noopener';

    const image = document.createElement('img');
    image.src = src;
    image.loading = 'lazy';
    // Assigned as a property, so caption text is never parsed as markup
    const caption = (post.prunedCaption || post.caption || '').replace(/\s+/g, ' ').trim();
    image.alt = caption ? caption.slice(0, 120) : 'Straight Away Plumbing on Instagram';
    link.appendChild(image);

    const badge = BADGES[post.mediaType];
    if (badge) {
      const mark = document.createElement('span');
      mark.className = 'insta-badge';
      mark.innerHTML = badge;
      link.appendChild(mark);
    }

    const overlay = document.createElement('span');
    overlay.className = 'insta-overlay';
    overlay.innerHTML = IG_GLYPH;
    link.appendChild(overlay);

    return link;
  };

  fetch(FEED_URL)
    .then((response) => (response.ok ? response.json() : Promise.reject(response.status)))
    .then((feed) => {
      const tiles = (feed.posts || []).slice(0, 6).map(tileFor).filter(Boolean);
      if (!tiles.length) return;
      instaGrid.replaceChildren(...tiles);
    })
    .catch(() => {
      /* Leave the fallback tiles in place */
    });
}

// Reviews carousel: arrows scroll one card at a time, and reviews long enough
// to be clipped get a Read more toggle.
const reviewsTrack = document.getElementById('reviewsTrack');

if (reviewsTrack) {
  const prev = document.querySelector('.rv-prev');
  const next = document.querySelector('.rv-next');

  const step = () => {
    const card = reviewsTrack.querySelector('.review-card');
    if (!card) return reviewsTrack.clientWidth;
    return card.getBoundingClientRect().width + parseFloat(getComputedStyle(reviewsTrack).columnGap || 0);
  };

  // Tolerance covers the track's padding and sub-pixel rounding at either end
  const EDGE = 12;

  const syncArrows = () => {
    const max = reviewsTrack.scrollWidth - reviewsTrack.clientWidth;
    prev.disabled = reviewsTrack.scrollLeft <= EDGE;
    next.disabled = reviewsTrack.scrollLeft >= max - EDGE;
  };

  prev.addEventListener('click', () => reviewsTrack.scrollBy({ left: -step(), behavior: 'smooth' }));
  next.addEventListener('click', () => reviewsTrack.scrollBy({ left: step(), behavior: 'smooth' }));
  reviewsTrack.addEventListener('scroll', syncArrows, { passive: true });
  window.addEventListener('resize', syncArrows);
  syncArrows();

  reviewsTrack.querySelectorAll('.review-card').forEach((card) => {
    const text = card.querySelector('p');
    if (!text) return;

    // scrollHeight is unreliable under -webkit-line-clamp, so measure the
    // unclamped height by briefly opening the card.
    const clampedHeight = text.clientHeight;
    card.classList.add('is-open');
    const fullHeight = text.scrollHeight;
    card.classList.remove('is-open');
    if (fullHeight <= clampedHeight + 1) return;

    const toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.className = 'rc-more';
    toggle.textContent = 'Read more';
    toggle.addEventListener('click', () => {
      const open = card.classList.toggle('is-open');
      toggle.textContent = open ? 'Read less' : 'Read more';
      syncArrows();
    });
    card.appendChild(toggle);
  });
}

// Quote forms: submit via AJAX so visitors stay on the page, then show a popup
function showFormModal(ok) {
  const overlay = document.createElement('div');
  overlay.className = 'form-modal-overlay';
  overlay.innerHTML = ok
    ? '<div class="form-modal"><div class="fm-icon">✅</div><h3>Request sent!</h3><p>Thanks - we\'ve got your quote request and we\'ll get back to you straight away.</p><button class="btn btn-primary" type="button">Close</button></div>'
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
