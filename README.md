# Straight Away Plumbing — Website

A static website for Straight Away Plumbing (Schofields NSW). No build step, no
frameworks — just HTML, CSS and a little JavaScript, so it can be hosted anywhere
(Netlify, Vercel, GitHub Pages, cPanel, etc.).

## Pages

- `index.html` — Home (hero + quote form, about, why choose us, services, emergency
  banner, reviews, gallery, service areas)
- `about.html` — About Us
- `services.html` — All 12 services (from the Facebook page's services list)
- `contact.html` — Contact details + quote form

Shared assets: `css/styles.css`, `js/main.js`, `images/favicon.svg`.

## Business details used

- Phone: 0403 322 290 (tap-to-call everywhere)
- Address: Alex Ave, Schofields NSW 2765
- Hours: Open 24 hours, 7 days
- Rating: 4.9★ — 56 Google reviews
- Facebook: https://www.facebook.com/p/Straight-Away-Plumbing-61574400357083/

## Before going live — TODO

1. **Logo** — the drop logo in the header/footer/favicon is an SVG recreation of the
   Facebook logo. To use the real logo file, save it as `images/logo.png` and replace
   the inline `<svg>` inside each `<a class="brand">` with
   `<img src="images/logo.png" alt="Straight Away Plumbing" width="46">`.
2. **Quote form** — currently not connected to anything (it shows a "call us" message
   on submit). Easiest fix: sign up at [formspree.io](https://formspree.io) (free),
   then change `action="#"` to your Formspree URL and `method="post"` on both forms
   (`index.html` and `contact.html`), and remove the form handler at the bottom of
   `js/main.js`.
3. **Gallery photos** — replace the "Add your photo" placeholder tiles in `index.html`
   with real job photos: `<img src="images/job1.jpg" alt="..." style="border-radius:12px">`
   (the Facebook page has photos to pull from).
4. **Google reviews link** — the "Read Our Reviews" buttons link to a Google search.
   Replace with the direct Google Business review link if you have it.
5. **ABN / Licence number** — add to the footer (`footer-bottom`) once you have them,
   as is standard for NSW plumbers.
6. **Review counts** — the 4.9★ / 56 reviews figures are hard-coded; update them as
   the numbers grow.

## Preview locally

```bash
python -m http.server 8735
```

Then open http://localhost:8735
