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
- Email: straightawayplumbing@gmail.com
- Hours: Open 24 hours, 7 days
- Rating: 5.0★ — 56 Google reviews
- Facebook: https://www.facebook.com/p/Straight-Away-Plumbing-61574400357083/

No street address is shown anywhere on the site (deliberately).

## Before going live — TODO

1. **Logo** — the site uses the real logo images from `images/`
   (`icononly_transparent_nobuffer.png` in the header/footer,
   `icononly_transparent.png` as the favicon).
2. **Quote form** — connected to Formspree (`https://formspree.io/f/myeyonvg`).
   Forms submit via AJAX (`js/main.js`) so visitors stay on the page and see a
   confirmation popup. Submissions are emailed to the Formspree account address.
   Free plan: 50 submissions/month.
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
