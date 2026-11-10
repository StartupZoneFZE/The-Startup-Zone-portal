# The 30-Day UAE Business Setup Guide

A 48-page printable A4 lead magnet for overseas investors, built in Startup Zone branding (logo,
orange `#FF5900`, navy `#061D25`, Inter font from thestartupzone.ae).

- `Startup-Zone-30-Day-UAE-Business-Setup-Guide.pdf`: the finished guide
- `content.py`: all text (days, free zones, checklists, glossary, FAQ, contact details)
- `build.py`: page layout and styles, which generate `guide.html`
- `render.js`: prints `guide.html` to the PDF and warns if any page overflows

## Rebuild after editing text

```bash
python3 build.py && node render.js
```

Needs Python 3 and Node with Playwright (Chromium). Photos are from Unsplash (free licence).
Review the tax and visa facts in `content.py` before each reprint, because UAE rules change.
