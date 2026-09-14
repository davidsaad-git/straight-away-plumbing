"""Generate the per-suburb service-area pages.

Header and footer are lifted from about.html at run time so the pages cannot
drift from the rest of the site. Everything else comes from the per-suburb
dicts in sub_data_*.py - the point of these pages is that the content actually
differs, so nothing here templates the body copy.
"""
import io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sub_data_a import SUBS as A
from sub_data_b import SUBS as B
from sub_data_c import SUBS as C

SUBS = A + B + C
BY_SLUG = {s['slug']: s for s in SUBS}
SITE = "https://straightawayplumbing.com.au"

PHONE_BTN = ('<a class="btn btn-primary" href="tel:0403322290"><svg class="icon-phone" viewBox="0 0 24 24" '
             'aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24c1.13.37 '
             '2.34.57 3.6.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 '
             '1.26.2 2.47.57 3.6a1 1 0 0 1-.25 1l-2.2 2.2z"/></svg><span class="cta-number">0403 322 290</span>'
             '<span class="cta-callnow">Call Now</span></a>')

_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
ICONS = {
    'alert':  _SVG % '<path d="M10.3 3.3 1.8 17.9A2 2 0 0 0 3.5 21h17a2 2 0 0 0 1.7-3.1L13.7 3.3a2 2 0 0 0-3.4 0z"/><path d="M12 9.5v4"/><path d="M12 17.2h.01"/>',
    'drain':  _SVG % '<circle cx="12" cy="12" r="9"/><path d="M7.4 8.5h9.2M5.5 12h13M7.4 15.5h9.2"/>',
    'hot':    _SVG % '<path d="M12 3c4 5 6.5 8 6.5 11.5a6.5 6.5 0 0 1-13 0C5.5 11 8 8 12 3z"/>',
    'tap':    _SVG % '<path d="M3 9.5h12a2.5 2.5 0 0 1 2.5 2.5v1.6"/><path d="M9 9.5V5.5"/><path d="M6.5 5.5h5"/><path d="M19.1 17.7a1.6 1.6 0 1 1-3.2 0c0-1.1 1.6-3.1 1.6-3.1s1.6 2 1.6 3.1z"/>',
    'jet':    _SVG % '<path d="M2 12h6"/><path d="M8 9.6h4.2L15 12l-2.8 2.4H8z"/><path d="M17.6 8.4 21.6 6.6M17.6 12h4.2M17.6 15.6l4 1.8"/>',
    'cctv':   _SVG % '<circle cx="12" cy="12" r="3"/><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6z"/>',
    'storm':  _SVG % '<path d="M7.6 16h9.8a3.5 3.5 0 0 0 .2-7 5.6 5.6 0 0 0-10.7-1.3A4.2 4.2 0 0 0 7.6 16z"/><path d="M8.6 18.7 7.6 21M12.6 18.7 11.6 21M16.6 18.7 15.6 21"/>',
    'gas':    _SVG % '<path d="M12 21.2a6.2 6.2 0 0 0 6.2-6.2c0-4.2-3.1-6.3-4.7-9.4-.5 2.1-1.6 3.2-2.6 4.2-1-1-1.3-2.1-1.1-3.7C8 8.2 5.8 11 5.8 15A6.2 6.2 0 0 0 12 21.2z"/>',
    'filter': _SVG % '<path d="M3.5 4h17l-6.6 8.2V18l-3.8 2.6V12.2z"/>',
    'reno':   _SVG % '<path d="M3 12.5h18V15a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4z"/><path d="M6.6 12.5V6.9a2.3 2.3 0 0 1 4.6 0"/><path d="M6.2 19 5 21.2M17.8 19l1.2 2.2"/>',
    'house':  _SVG % '<path d="M3 12l9-9 9 9M5 10v10h5v-6h4v6h5V10"/>',
    'shield': _SVG % '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
    'card':   _SVG % '<rect x="3" y="6" width="18" height="14" rx="2"/><path d="M3 10h18M8 15h4"/>',
    'bolt':   _SVG % '<path d="M13 2L4 14h6l-1 8 9-12h-6z"/>',
    'clock':  _SVG % '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    'block':  _SVG % '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2"/>',
    'pipe':   '<img src="images/icon-burst-pipe.png" width="48" height="48" alt="">',
    'wrench': '<img src="images/icon-wrench.png" width="48" height="48" alt="">',
}

TAGS = re.compile(r'<[^>]+>')
def plain(html):
    """FAQ answers carry links; the JSON-LD copy must not."""
    return TAGS.sub('', html).replace('&amp;', '&').replace('&#x27;', "'").strip()


def chrome():
    src = io.open(os.path.join(ROOT, 'about.html'), encoding='utf-8').read()
    head = src[src.index('<body>'):src.index('</header>') + len('</header>\n')]
    head = head.replace('<a href="/about" class="active">About Us</a>', '<a href="/about">About Us</a>')
    head = head.replace('<a href="/locations">Service Areas</a>\n',
                        '<a href="/locations" class="active">Service Areas</a>\n')
    assert 'class="active"' in head, 'nav active state not set'
    foot = src[src.index('  <footer class="site-footer">'):]
    return head, foot


def build(s):
    url = '%s/%s' % (SITE, s['slug'])
    faqs = s['faqs']

    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": url + "#service",
                "name": "Plumber in " + s['name'],
                "serviceType": "Plumber",
                "description": s['ld_desc'],
                "url": url,
                "provider": {"@id": SITE + "/#business"},
                "hoursAvailable": {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday",
                                  "Friday", "Saturday", "Sunday"],
                    "opens": "00:00", "closes": "23:59",
                },
                "areaServed": {
                    "@type": "Place",
                    "name": "%s, NSW %s" % (s['name'], s['pc']),
                    "address": {
                        "@type": "PostalAddress",
                        "addressLocality": s['name'],
                        "addressRegion": "NSW",
                        "postalCode": s['pc'],
                        "addressCountry": "AU",
                    },
                },
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Service Areas", "item": SITE + "/locations"},
                    {"@type": "ListItem", "position": 3, "name": "Plumber " + s['name'], "item": url},
                ],
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q,
                     "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
                    for q, a in faqs
                ],
            },
        ],
    }

    cards = '\n'.join(
        '        <div class="why-card">\n'
        '          <div class="why-icon">%s</div>\n'
        '          <h3>%s</h3>\n'
        '          <p>%s</p>\n'
        '        </div>' % (ICONS[i], h, p) for i, h, p in s['cards'])

    nearby = '\n'.join(
        '        <li><a href="/%s">%s</a></li>' % (sl, BY_SLUG[sl]['name']) for sl in s['nearby'])

    faq_html = '\n'.join(
        '        <details class="faq-item">\n'
        '          <summary>%s</summary>\n'
        '          <p>%s</p>\n'
        '        </details>' % (q, a) for q, a in faqs)

    paras = '\n'.join('        <p>%s</p>' % p for p in s['paras'])

    head, foot = chrome()
    return """<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="stylesheet" href="css/styles.css?v=21">
  <link rel="icon" type="image/png" sizes="64x64" href="images/favicon.png">
  <link rel="icon" type="image/png" sizes="512x512" href="images/icon-512.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#081120">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Straight Away Plumbing">
  <meta property="og:locale" content="en_AU">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{og}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{site}/images/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Straight Away Plumbing - 24/7 emergency plumber in Sydney. Call 0403 322 290.">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{site}/images/og-image.png">
  <script type="application/ld+json">
{ld}
  </script>
</head>
{head}
  <section id="main" tabindex="-1" class="page-hero">
    <div class="container">
      <h1>Plumber in {name}</h1>
      <p>{hero}</p>
      <div class="btn-row">
        {phone}
        <a class="btn btn-outline" href="/contact#quote">Get a Free Quote</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container about-grid">
      <div class="about-visual">
        <img src="images/logo-about.jpg" width="1000" height="800" alt="Straight Away Plumbing, servicing {name} NSW">
        <div class="about-stats">
          <div class="stat-chip"><strong>{pc}</strong><small>{name}</small></div>
          <div class="stat-chip"><strong>24/7</strong><small>Availability</small></div>
          <div class="stat-chip"><strong>$0</strong><small>Call Out Fees</small></div>
        </div>
      </div>
      <div class="about-copy">
        <span class="eyebrow">{name}, NSW {pc}</span>
        <h2>{h2}</h2>
{paras}
        <a class="btn btn-primary" href="/contact#quote">Get a Free Quote</a>
      </div>
    </div>
  </section>

  <section class="alt-bg">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">What We Get Called For</span>
        <h2>Common Plumbing Problems in {name}</h2>
        <p>{cards_intro}</p>
      </div>
      <div class="values-grid why-grid">
{cards}
      </div>
      <div class="section-cta">
        <a class="btn btn-dark" href="/services">See All 12 Services</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container areas-grid">
      <div>
        <span class="eyebrow">{nearby_eyebrow}</span>
        <h2 style="font-size: clamp(1.6rem, 3vw, 2.2rem); color: var(--navy-800); margin-bottom: 1rem;">Also Covering Nearby</h2>
        <p style="color: var(--grey-600); margin-bottom: 1.5rem;">{nearby_intro}</p>
        <div class="areas-actions">
          <a class="btn btn-primary" href="/locations">Search All Suburbs</a>
          <a class="btn btn-dark" href="/contact">Get in Touch</a>
        </div>
      </div>
      <ul class="areas-list">
{nearby}
        <li><a href="/locations">+ More</a></li>
      </ul>
    </div>
  </section>

  <section class="alt-bg">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">FAQs</span>
        <h2>Plumbing in {name} - Your Questions</h2>
      </div>
      <div class="faq-list">
{faq}
      </div>
    </div>
  </section>

  <section class="emergency">
    <div class="container">
      <span class="eyebrow">Ready When You Are</span>
      <h2>Need a Plumber in {name}?</h2>
      <p>Call for a free, no-obligation quote - or for help straight away, whatever the hour.</p>
      <div class="btn-row">
        {phone}
        <a class="btn btn-outline" href="/contact#quote">Request a Quote</a>
      </div>
    </div>
  </section>

{foot}""".format(
        title=s['title'], desc=s['desc'], og=s['og'], url=url, site=SITE,
        ld=json.dumps(ld, indent=2), head=head, name=s['name'], pc=s['pc'],
        hero=s['hero'], h2=s['h2'], paras=paras, cards_intro=s['cards_intro'],
        cards=cards, nearby_eyebrow=s['nearby_eyebrow'], nearby_intro=s['nearby_intro'],
        nearby=nearby, faq=faq_html, foot=foot, phone=PHONE_BTN)


if __name__ == '__main__':
    for s in SUBS:
        out = os.path.join(ROOT, s['slug'] + '.html')
        t = build(s)
        # Schofields is fine as a linked service area; claiming it as a base is not.
        for bad in ('based in Schofields', 'we are based in', 'Windsor Road'):
            assert bad.lower() not in t.lower(), (s['slug'], bad)
        json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', t, re.S).group(1))
        io.open(out, 'w', encoding='utf-8', newline='').write(t)
        print('wrote', s['slug'] + '.html', len(t), 'bytes')
    print('\n%d pages' % len(SUBS))
