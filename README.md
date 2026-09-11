# Straight Away Plumbing - Website

A static website for Straight Away Plumbing (Schofields NSW). No build step, no
frameworks - just HTML, CSS and a little JavaScript.

## Pages

- `index.html` - Home (hero + quote form, about, why choose us, services, emergency
  banner, reviews, Instagram feed, service areas)
- `about.html` - About Us
- `services.html` - All 12 services (from the Facebook page's services list)
- `contact.html` - Contact details + quote form

Shared assets: `css/styles.css`, `js/main.js`, and the icons in `images/`
(`favicon.png`, `apple-touch-icon.png`, `icon-512.png`, `og-image.png`).

Both `styles.css` and `main.js` are linked with a `?v=N` cache-buster. **Bump that
number on every CSS or JS edit**, in all four HTML files, or browsers and the
Cloudflare edge will keep serving the old file and the change will look broken.

## Hosting

Deployed on **Cloudflare Pages**, connected to this GitHub repo.

- Live at https://straight-away-plumbing.pages.dev
- Production branch `main`; no build command; build output directory is the repo root
- **Every push to `main` auto-deploys** in about 30 seconds
- Previous deployments can be restored from the Cloudflare dashboard (Rollback)

Cloudflare serves clean URLs: `/about` rather than `/about.html`, with the `.html`
form redirecting to it. Canonical tags and `sitemap.xml` use the clean form.

## Business details used

- Phone: 0403 322 290 (tap-to-call everywhere)
- Email: straightawayplumbing@gmail.com
- Hours: Open 24 hours, 7 days
- Rating: 5.0 stars - 56 Google reviews
- Facebook: https://www.facebook.com/p/Straight-Away-Plumbing-61574400357083/
- Instagram: https://www.instagram.com/straightawayplumbing

No street address is shown anywhere on the site (deliberately). The structured data
gives suburb, state and postcode only.

## SEO

- **Open Graph + Twitter card** tags on all four pages, sharing `images/og-image.png`
  (1200x630, generated from the logo). This is what Facebook and WhatsApp render
  when the link is shared.
- **`Plumber` JSON-LD schema** on `index.html` and `contact.html` - phone, email,
  hours, area served and the 12 services.
- **`sitemap.xml`** and **`robots.txt`** at the repo root.
- **Canonical tags** on every page.

All of these carry absolute URLs. **They point at the `.pages.dev` address and must
be updated when the real domain goes live** - see the TODO below.

## Analytics

Cloudflare Web Analytics is installed (the beacon snippet before `</body>` on each
page). It is cookieless, so no consent banner is needed.

`js/main.js` defines a `track()` helper and fires two conversion events:

- `call_click` - any tap on a phone number, labelled by where it was clicked
  (`header`, `hero`, `floating_button`, `footer`)
- `quote_submit` / `quote_error` - the quote form result

Cloudflare Web Analytics has **no custom-event API**, so these events are recorded
but not yet stored anywhere. They start working, with no code changes, as soon as
either is enabled:

- **Cloudflare Zaraz** (`zaraz.track`) - free, but needs the domain on Cloudflare
- **Google Analytics 4** (`gtag`) - free, works today, needs a snippet added

Events are also pushed to `window.dataLayer` for anything else that reads it.

## Before going live - TODO

1. **Domain** - buy the `.com.au` (needs an ABN), point its nameservers at
   Cloudflare, then add it under the Pages project's Custom domains.
2. **Swap the base URL** once the domain is live: canonical tags and OG tags in all
   four HTML files, `sitemap.xml`, `robots.txt`, and the `url` / `image` / `logo` /
   `@id` fields in the JSON-LD. Also update the hostname in Cloudflare Web Analytics.
3. **ABN / Licence number** - add to the footer (`footer-bottom`). A NSW contractor
   licence number is required in advertising, and the website counts.
4. **Google reviews link** - the "Read Our Reviews" buttons link to a Google search.
   Replace with the direct Google Business Profile review link.
5. **Review counts** - the 5.0 stars / 56 reviews figures are hard-coded in
   `index.html`, `about.html` and `contact.html`; update them as the numbers grow.
6. **Conversion tracking** - switch on Zaraz or GA4 so `call_click` and
   `quote_submit` are actually recorded. Data only exists from the day it is
   enabled; it cannot be backfilled.

### Already done

- Logo, favicons and home-screen icons, generated from the real logo
- Quote form, live on Formspree (`https://formspree.io/f/myeyonvg`), submitting via
  AJAX so visitors stay on the page. Free plan: 50 submissions/month
- Instagram section, live via a [Behold](https://behold.so) JSON feed (`FEED_URL` in
  `js/main.js`). The six tiles hard-coded in `index.html` point at
  `images/instagram/` and act as the fallback if the feed fails, so the section
  always shows real work. Free plan: 6 posts, refreshed daily, 1,200 page views a
  month - if the site outgrows that, the feed stops updating and visitors see the
  fallback, so it's worth watching

## Preview locally

```bash
python -m http.server 8735
```

Then open http://localhost:8735
