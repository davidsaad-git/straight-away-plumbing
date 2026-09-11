# Straight Away Plumbing - Website

A static website for Straight Away Plumbing (Schofields NSW). No build step, no
frameworks - just HTML, CSS and a little JavaScript.

## Pages

- `index.html` - Home (hero + quote form, about, why choose us, services, emergency
  banner, reviews, Instagram feed, service areas)
- `about.html` - About Us
- `services.html` - All 12 services (from the Facebook page's services list)
- `contact.html` - Contact details + quote form

- `privacy.html` - privacy policy, linked from the footer of every page
- `404.html` - shown for any unknown path. Its links are **root-relative**, because
  Cloudflare serves it at whatever depth was requested; relative paths would break
  the stylesheet and nav on anything below the first level.

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

`_headers` caches the versioned CSS and JS, and the images, for a year. That is why
the `?v=N` bump above matters: without it a returning visitor keeps the old file for
a year, not just until they refresh. Images are cached by name, so give a changed
image a new filename rather than overwriting it.

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

## Security and accessibility

`_headers` sets HSTS, `X-Frame-Options: DENY`, a `Permissions-Policy` switching off
APIs the site never uses, and a Content Security Policy. Cloudflare adds
`referrer-policy` and `x-content-type-options` itself.

The CSP keeps `img-src` open to any https host on purpose: the Instagram section
loads whatever CDN the Behold feed returns, which is currently `behold.pictures` and
is not guaranteed to stay that way. A strict allowlist there breaks the section
silently. `connect-src` does name its hosts - Formspree, Behold and Cloudflare - so
check it if you ever add a third-party script.

On accessibility: the quote form is designed around placeholders, which vanish as
soon as someone types and say nothing to a screen reader, so each field carries a
visually hidden `<label>` (`.sr-only`). Every page has a skip link and a visible
`:focus-visible` ring. Link colour is `--blue-700`, which clears WCAG AA on white at
5.75; the old `--blue-600` failed at 3.68, so do not put it back on text links.

## Analytics

Cloudflare Web Analytics is installed (the beacon snippet before `</body>` on each
page). It is cookieless, so no consent banner is needed.

`js/main.js` defines a `track()` helper and fires two conversion events:

- `call_click` - any tap on a phone number, labelled by where it was clicked
  (`header`, `hero`, `floating_button`, `footer`)
- `quote_submit` / `quote_error` - the quote form result

Cloudflare Web Analytics has **no custom-event API**, so these events fire but are
not yet stored anywhere.

**The decision is Cloudflare Zaraz** (`zaraz.track`), switched on once the real
domain is live - Zaraz needs the domain to be a Cloudflare zone, so it cannot be
enabled on `.pages.dev`. No code change is needed when the time comes: `track()`
already calls it. The same helper also supports GA4 (`gtag`) if that is ever
preferred instead.

Events are also pushed to `window.dataLayer` for anything else that reads it.

## Before going live - TODO

1. **Domain** - buy the `.com.au` (needs an ABN), point its nameservers at
   Cloudflare, then add it under the Pages project's Custom domains.
2. **Swap the base URL** once the domain is live: canonical tags and OG tags in all
   four HTML files, `sitemap.xml`, `robots.txt`, and the `url` / `image` / `logo` /
   `@id` fields in the JSON-LD. Also update the hostname in Cloudflare Web Analytics.
3. **Google reviews link** - the "Read Our Reviews" buttons link to a Google search.
   Replace with the direct Google Business Profile review link.
4. **Review counts** - the 5.0 stars / 56 reviews figures are hard-coded in
   `index.html`, `about.html` and `contact.html`; update them as the numbers grow.
5. **Confirm the privacy policy matches reality** - it was written from what the
   site verifiably does. Check three claims in particular: that enquiry records are
   kept only as long as needed for the job, warranty and tax obligations; that you
   do not add people to any marketing list; and that you never share enquiry details
   beyond what a job requires. Correct them if any is wrong.
6. **Conversion tracking** - switch on Cloudflare Zaraz so `call_click` and
   `quote_submit` are actually recorded. Needs the domain on Cloudflare first, so it
   is a launch-day job. Data only exists from the day it is enabled; it cannot be
   backfilled.

### Already done

- ABN and contractor licence number in the footer, so they appear on every page
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
