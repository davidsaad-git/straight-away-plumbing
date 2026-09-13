# Straight Away Plumbing - Website

A static website for Straight Away Plumbing (Schofields NSW). No build step, no
frameworks - just HTML, CSS and a little JavaScript.

## Pages

- `index.html` - Home (hero + quote form, about, why choose us, services, emergency
  banner, reviews, Instagram feed, service areas)
- `about.html` - About Us
- `services.html` - All 12 services (from the Facebook page's services list)
- `contact.html` - Contact details + quote form
- `locations.html` - Service Areas: a search box over an A-Z list of every suburb
  covered. The chips are plain text, not links - there are no per-suburb pages, and
  259 near-identical ones would be thin content. Filtering lives in `js/main.js`
  and matches on a `data-suburb` attribute holding the lowercased name, so there is
  no string work per keystroke across 259 elements. Empty letter groups hide
  themselves, and a no-match state offers the phone number instead.
- `privacy.html` - privacy policy, linked from the footer of every page
- `404.html` - shown for any unknown path. Its links are **root-relative**, because
  Cloudflare serves it at whatever depth was requested; relative paths would break
  the stylesheet and nav on anything below the first level.

Shared assets: `css/styles.css`, `js/main.js`, and the icons in `images/`
(`favicon.png`, `apple-touch-icon.png`, `icon-512.png`, `og-image.png`).

Both `styles.css` and `main.js` are linked with a `?v=N` cache-buster. **Bump that
number on every CSS or JS edit**, in all seven HTML files (the five above plus
`privacy.html` and `404.html`), or browsers and the Cloudflare edge will keep
serving the old file and the change will look broken.

## Hosting

Deployed on **Cloudflare Pages**, connected to this GitHub repo.

- Live at https://straightawayplumbing.com.au (apex is canonical; `www` also
  resolves). The project still answers on straight-away-plumbing.pages.dev
- Production branch `main`; no build command; build output directory is the repo root
- **Every push to `main` auto-deploys** in about 30 seconds
- Previous deployments can be restored from the Cloudflare dashboard (Rollback)

Cloudflare serves clean URLs: `/about` rather than `/about.html`, with the `.html`
form redirecting to it (a 308). Canonical tags, `sitemap.xml` **and every internal
link** use the clean, root-relative form - `/about`, `/services#drains`, `/` for
home. Writing `about.html` in a link still works, but costs every visitor and every
crawler a redirect hop, so don't: link to `/about`.

This is also why the local preview below uses Wrangler rather than a plain static
server - nothing else resolves `/about` to `about.html`.

`_headers` caches the versioned CSS and JS, and the images, for a year. That is why
the `?v=N` bump above matters: without it a returning visitor keeps the old file for
a year, not just until they refresh. Images are cached by name, so give a changed
image a new filename rather than overwriting it.

## Business details used

- Phone: 0403 322 290 (tap-to-call everywhere)
- Email: straightawayplumbing@gmail.com
- Hours: Open 24 hours, 7 days
- Postcode: Schofields **2765**, matching the Google Business Profile. Not 2762,
  which Schofields also uses - the structured data said 2762 until it was checked
- Rating: 5.0 stars - 56 Google reviews
- Facebook: https://www.facebook.com/p/Straight-Away-Plumbing-61574400357083/
- Instagram: https://www.instagram.com/straightawayplumbing

No street address is shown anywhere on the site (deliberately). The structured data
gives suburb, state and postcode only.

## Conventions

Decisions already made for this site. They are easy to undo by accident and hard to
spot afterwards, so check these before writing copy or adding markup.

- **No em dashes anywhere.** Use a spaced hyphen (` - `). All 48 were removed from the
  site deliberately; one slipped into new copy undoes that.
- **Customer reviews are quoted verbatim** - the reviewers' own spelling, punctuation
  and grammar. Do not tidy them up. Where a review was truncated on Google, it ends in
  an ellipsis rather than being completed.
- **Bump the `?v=` cache-buster** in all seven HTML files on every CSS or JS edit. See
  the note under Pages above.
- **No street address**, in the copy or the structured data. Suburb, state and
  postcode only.
- **Service icons**: one icon per service, identical on the homepage and the services
  page. Inline SVGs render at 30px, uploaded PNGs at 24px - the PNG artwork runs edge
  to edge, where the SVG shapes carry margin inside their own viewBox, so equal box
  sizes make the PNGs look bigger.
- **The Business Profile address and the site need not agree.** The profile shows
  a street address; the site deliberately shows none. Asked and answered - leave
  the profile as it is rather than switching it to a service-area listing.
- **`.pages.dev` is left serving the site.** It cannot be redirected cleanly - a
  redirect rule needs a zone you own, and that host is Cloudflare's. Every page
  there declares the real domain as canonical, which is the standard fix and is
  live. Do not add a Pages Function just for this.
- **The hard-coded 5.0 Google rating stays as written.** Asked and answered; do
  not raise it again when the profile average differs.
- **Copy is plain and first person** ("we"), matching how a tradie actually speaks.
  Avoid marketing filler.

## SEO

- **Open Graph + Twitter card** tags on all six content pages, sharing `images/og-image.png`
  (1200x630, generated from the logo). This is what Facebook and WhatsApp render
  when the link is shared.
- **`Plumber` JSON-LD schema** on `index.html` and `contact.html` - phone, email,
  hours, area served and the 12 services.
- **`sitemap.xml`** and **`robots.txt`** at the repo root.
- **Canonical tags** on every page.

All of these carry absolute URLs, pointing at `https://straightawayplumbing.com.au`.
Keep any new one absolute and on that host.

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

Both now land in **Google Analytics 4** (`G-JG0DEKLDEV`) through Cloudflare Zaraz,
which forwards `zaraz.track()` calls server-side.

Two things about that setup are deliberate. Zaraz's GA4 tool runs with **"Access
client key-value store" off**, so it sets no cookies: event counts - the thing worth
knowing - record fine without one, and audience numbers come from Cloudflare Web
Analytics, which is accurate and cookieless. GA4's own users and sessions figures
are therefore inflated and should be ignored. It also runs with **Hide Originating
IP Address on** and **Audiences off**. Together that is what keeps the privacy
policy's "sets no tracking cookies" and "does not follow you across other sites"
true, and why there is still no consent banner. Turning any of the three back on
means rewriting that policy first.

Zaraz's **auto-injection does not reach responses served by Pages**, even with the
setting switched on, so `/cdn-cgi/zaraz/i.js` is in the markup by hand next to the
beacon. It is same-origin, as is everything it goes on to load, so `script-src
'self'` and `connect-src 'self'` already cover it - the CSP needs no Google host.

**The decision is Cloudflare Zaraz** (`zaraz.track`), switched on once the real
domain is live - Zaraz needs the domain to be a Cloudflare zone, so it cannot be
enabled on `.pages.dev`. No code change is needed when the time comes: `track()`
already calls it. The same helper also supports GA4 (`gtag`) if that is ever
preferred instead.

Events are also pushed to `window.dataLayer` for anything else that reads it.

## Before going live - TODO

Ordered by what blocks what, not by topic. The domain is live, so nothing here is
blocked any more.

Cross-references below name their step rather than numbering it - the list gets
reordered as things land, and numbers rot silently.

### Do now - nothing blocks these

1. **Finish the Business Profile.** Website and categories are set. What is left is
   soft: mirror the 12 services, add photos (the Instagram shots are right there),
   and reply to any review that has not been answered.
2. **Confirm the privacy policy matches reality** - it was written from what the
   site verifiably does. Check three claims in particular: that enquiry records are
   kept only as long as needed for the job, warranty and tax obligations; that you
   do not add people to any marketing list; and that you never share enquiry details
   beyond what a job requires. Correct them if any is wrong.

### After the swap is live

3. **HSTS `preload`** - weeks later, once the domain is settled. Hard to undo.
4. **Watch the free tiers.** Formspree stops at 50 submissions a month and Behold
    at 1,200 page views; both fail quietly. Worth a reminder a month in.

### Already done

- ABN and contractor licence number in the footer, so they appear on every page
- Logo, favicons and home-screen icons, generated from the real logo
- Google Business Profile linked from the reviews carousel and claimed in the
  JSON-LD `sameAs`. The review short link is `g.page/r/CXLUFbnpxEBhEBM/review`;
  the profile is CID `7007817528300131442`, place ID `ChIJI_zfHGtCq2IRctQVuenEQGE`
- Google Search Console verified (via the Cloudflare DNS hookup) with `sitemap.xml`
  submitted; all six pages discovered on the first read
- Cloudflare Web Analytics repointed at the real hostname, same token, history intact
- Business Profile website field set, and categories are Plumber as primary with
  Drainage service, Gas installation service and Hot water system supplier beside it
- Domain live: `straightawayplumbing.com.au`, registered through VentraIP against
  ABN 63 241 616 098 (partnership, registered business name STRAIGHT AWAY PLUMBING),
  nameservers `chloe`/`ezra`.ns.cloudflare.com, apex and www both attached to the
  Pages project with Cloudflare-issued SSL
- Every absolute URL - canonical, OG, Twitter, JSON-LD, sitemap, robots - is on the
  real domain
- Internal links all point at the clean, root-relative URL, so no visitor or crawler
  eats a redirect. See the note under Hosting before adding a link
- `images/` holds only what the site actually references - the source logo exports
  and other unused artwork were removed. If you add an image, use it or drop it
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
npx wrangler pages dev . --port 8735
```

Then open http://localhost:8735

This runs the same Pages runtime the site is deployed on, so the preview matches
production: clean URLs resolve, `/about.html` redirects to `/about`, unknown paths
serve `404.html`, and the `_headers` rules (CSP, HSTS, the cache headers) are
applied. First run downloads Wrangler.

`python -m http.server` will not do - it serves `/` but 404s on `/about`, because
it has no extension-less resolution and ignores `_headers`.
