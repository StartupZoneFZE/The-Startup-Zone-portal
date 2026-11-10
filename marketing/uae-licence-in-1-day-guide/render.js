// Renders guide.html to an A4 PDF. Run after build.py: node render.js
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(__dirname, 'guide.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);

  // Warn about any page whose content runs past the bottom of the A4 sheet.
  const overflows = await page.evaluate(() =>
    [...document.querySelectorAll('.page')].flatMap((p, i) => {
      const bottom = p.getBoundingClientRect().bottom;
      const foot = p.querySelector('.foot');
      const limit = foot ? foot.getBoundingClientRect().top : bottom;
      const worst = Math.max(...[...p.querySelectorAll('*')]
        .filter((el) => !el.closest('.foot') && getComputedStyle(el).position !== 'absolute')
        .map((el) => el.getBoundingClientRect().bottom));
      return worst > limit + 1 ? [`page ${i + 1}: ${Math.round(worst - limit)}px over`] : [];
    }));
  if (overflows.length) console.warn('Overflow:\n' + overflows.join('\n'));

  const out = path.join(__dirname, 'Startup-Zone-UAE-Licence-in-1-Day-Guide.pdf');
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log('PDF written:', out);
})();
