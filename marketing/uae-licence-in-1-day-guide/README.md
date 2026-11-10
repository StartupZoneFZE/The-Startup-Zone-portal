# Your UAE Licence in 1 Day

An 11-page printable A4 lead magnet for overseas investors (short version of the 30-day guide).
The 1-day licence claim covers SHAMS and ANCFZ only, with terms on page 3. Prices and timelines
come from thestartupzone.ae and the startupzone-proposals system (November 2026).

- `Startup-Zone-UAE-Licence-in-1-Day-Guide.pdf`: the finished guide
- `build.py`: all text (CONTENT section at the top) and layout; generates `guide.html`
- `render.js`: prints `guide.html` to the PDF and warns if any page overflows

Rebuild: `python3 build.py && node render.js` (Python 3, Node with Playwright).
