"""Builds guide.html from content.py. Run: python3 build.py && node render.js"""
from html import escape as e
from pathlib import Path

from content import (BANK_CHECKLIST, COMPLIANCE, CONTACT, DAYS, DOC_CHECKLIST, EDITION, FAQ,
                     FREE_ZONES, GLOSSARY, MAINLAND_VS_FZ, TIMELINE, WEEKS, WHY_UAE)

HERE = Path(__file__).parent
QR = (HERE / "assets/brand/whatsapp-qr.svg").read_text().split("?>", 1)[-1]

CSS = """
@font-face { font-family: 'InterV'; src: url('assets/fonts/inter-latin-wght-normal.woff2') format('woff2');
  font-weight: 100 900; }
:root { --orange:#FF5900; --navy:#061D25; --ink:#110024; --peach:#FDCEBE; --coral:#FF9874;
  --mist:#F9F8FC; --line:#E2E2E8; --grey:#474752; --cream:#FFF4EE; }
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'InterV', 'Inter', sans-serif; color: var(--ink); font-size: 10.5pt; line-height: 1.45; }
.page { width: 210mm; height: 297mm; position: relative; overflow: hidden; page-break-after: always;
  background: #fff; padding: 16mm 16mm 18mm; }
.page:last-child { page-break-after: auto; }
h1, h2, h3 { color: var(--navy); line-height: 1.12; letter-spacing: -0.01em; }
h2 { font-size: 24pt; font-weight: 800; margin-bottom: 3mm; }
h3 { font-size: 12.5pt; font-weight: 700; }
.kicker { color: var(--orange); font-weight: 700; font-size: 9pt; letter-spacing: .14em; text-transform: uppercase; margin-bottom: 2mm; }
.lead { font-size: 11.5pt; color: var(--grey); max-width: 160mm; margin-bottom: 7mm; }
.orange { color: var(--orange); }

/* running header / footer */
.top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 9mm; }
.top img { height: 8mm; }
.chip { background: var(--navy); color: #fff; border-radius: 99px; padding: 1.3mm 4mm; font-size: 8pt;
  font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
.chip b { color: var(--orange); }
.foot { position: absolute; left: 16mm; right: 16mm; bottom: 8mm; display: flex; justify-content: space-between;
  font-size: 7.5pt; color: #8a8a96; border-top: 0.3mm solid var(--line); padding-top: 2.5mm; }
.foot .pg { color: var(--navy); font-weight: 700; }

/* cover */
.cover { padding: 0; background: var(--navy); color: #fff; }
.cover .photo { position: absolute; inset: 0; background: url('assets/photos/cover.jpg') center/cover; }
.cover .shade { position: absolute; inset: 0;
  background: linear-gradient(180deg, rgba(6,29,37,.15) 0%, rgba(6,29,37,.35) 40%, rgba(6,29,37,.96) 70%, #061D25 100%); }
.cover .inner { position: absolute; inset: 0; padding: 18mm; display: flex; flex-direction: column; }
.cover .logo { height: 13mm; align-self: flex-start; }
.cover .badge { margin-top: auto; display: inline-block; background: var(--orange); color: #fff; font-weight: 800;
  font-size: 10pt; letter-spacing: .14em; text-transform: uppercase; padding: 2mm 5mm; border-radius: 1.5mm; align-self: flex-start; }
.cover h1 { color: #fff; font-size: 50pt; font-weight: 900; line-height: .98; margin: 6mm 0 5mm; letter-spacing: -0.025em; }
.cover h1 span { color: var(--orange); }
.cover .sub { font-size: 14pt; color: #dfe6e8; max-width: 150mm; margin-bottom: 9mm; }
.cover .stats { display: flex; gap: 0; border-top: 0.4mm solid rgba(255,255,255,.25); padding-top: 6mm; }
.cover .stats div { flex: 1; font-size: 8.5pt; color: #b9c6ca; }
.cover .stats b { display: block; font-size: 17pt; color: #fff; font-weight: 800; }
.cover .ed { margin-top: 7mm; font-size: 8pt; color: #8fa1a6; letter-spacing: .08em; text-transform: uppercase; }

/* welcome */
.hero-img { height: 82mm; border-radius: 4mm; background-size: cover; background-position: center; margin-bottom: 8mm; }
.cols2 { display: grid; grid-template-columns: 1fr 1fr; gap: 7mm; }
.howto { display: grid; grid-template-columns: repeat(2, 1fr); gap: 4mm; margin-top: 4mm; }
.howto div { background: var(--mist); border-radius: 3mm; padding: 4.5mm; font-size: 9.5pt; color: var(--grey); }
.howto b { display: block; color: var(--navy); font-size: 10.5pt; margin-bottom: 1mm; }
.howto i { font-style: normal; display: inline-block; width: 7mm; height: 7mm; border-radius: 50%; background: var(--orange);
  color: #fff; text-align: center; line-height: 7mm; font-weight: 800; margin-bottom: 2mm; }
.sign { margin-top: 7mm; padding: 5mm 6mm; border-left: 1.2mm solid var(--orange); background: var(--cream); border-radius: 0 3mm 3mm 0;
  font-size: 10.5pt; color: var(--ink); }

/* why uae */
.why { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; }
.why div { border: 0.3mm solid var(--line); border-radius: 4mm; padding: 6mm; }
.why b { display: block; font-size: 28pt; font-weight: 900; color: var(--orange); line-height: 1; letter-spacing: -0.02em; }
.why h3 { margin: 2mm 0 1.5mm; }
.why p { font-size: 9.5pt; color: var(--grey); }
.strip { height: 52mm; border-radius: 4mm; margin-top: 6mm; background-size: cover; background-position: center 40%; }

/* roadmap */
.road { display: grid; grid-template-columns: repeat(4, 1fr); gap: 4mm; }
.road .wk { border-radius: 4mm; overflow: hidden; border: 0.3mm solid var(--line); }
.road .wk header { background: var(--navy); color: #fff; padding: 4mm; }
.road .wk:nth-child(even) header { background: var(--orange); }
.road .wk header small { display: block; font-size: 7.5pt; letter-spacing: .12em; text-transform: uppercase; opacity: .8; }
.road .wk header b { font-size: 15pt; }
.road ol { list-style: none; padding: 3mm 3.5mm; }
.road li { font-size: 8.4pt; padding: 1.6mm 0; border-bottom: 0.25mm dashed var(--line); display: flex; gap: 2mm; color: var(--grey); }
.road li:last-child { border: 0; }
.road li span { font-weight: 800; color: var(--navy); min-width: 5.5mm; }
.note { font-size: 8.5pt; color: var(--grey); margin-top: 6mm; background: var(--mist); padding: 4mm 5mm; border-radius: 3mm; }

/* tables */
table { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 9.2pt; }
th { text-align: left; background: var(--navy); color: #fff; padding: 3mm 3.5mm; font-weight: 700; }
th:first-child { border-radius: 3mm 0 0 0; } th:last-child { border-radius: 0 3mm 0 0; }
td { padding: 3mm 3.5mm; border-bottom: 0.3mm solid var(--line); vertical-align: top; color: var(--grey); }
td:first-child { font-weight: 700; color: var(--navy); width: 30%; }
tr:nth-child(even) td { background: var(--mist); }
th.fz { background: var(--orange); }

/* free zones */
.fzs { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; }
.fz-card { border: 0.3mm solid var(--line); border-radius: 4mm; padding: 5.5mm; position: relative; }
.fz-card .tag { position: absolute; top: 5mm; right: 5mm; background: var(--peach); color: var(--navy); font-size: 7.5pt;
  font-weight: 700; padding: 1mm 3mm; border-radius: 99px; }
.fz-card h3 { font-size: 20pt; font-weight: 900; color: var(--orange); }
.fz-card .nm { font-size: 9pt; font-weight: 600; color: var(--navy); }
.fz-card .em { font-size: 8.5pt; color: var(--grey); margin-bottom: 3mm; }
.fz-card .best { font-size: 9pt; background: var(--mist); border-radius: 2mm; padding: 2.5mm 3mm; margin-bottom: 3mm; }
.fz-card .best b { color: var(--navy); }
.fz-card ul { list-style: none; font-size: 9pt; }
.fz-card li { padding: 1mm 0 1mm 5mm; position: relative; }
.fz-card li::before { content: ''; position: absolute; left: 0; top: 2.6mm; width: 2.2mm; height: 2.2mm; border-radius: 50%; background: var(--orange); }
.fz-card .off { margin-top: 2.5mm; font-size: 8.5pt; color: var(--grey); border-top: 0.25mm dashed var(--line); padding-top: 2.5mm; }

/* timeline chart */
.tl { margin-top: 2mm; }
.tl .row { display: grid; grid-template-columns: 52mm 1fr 20mm; align-items: center; gap: 3mm; padding: 2.6mm 0; border-bottom: 0.25mm solid var(--line); }
.tl .lbl { font-size: 9.3pt; font-weight: 600; color: var(--navy); }
.tl .track { position: relative; height: 6mm; background: var(--mist); border-radius: 99px; }
.tl .bar { position: absolute; top: 0; height: 6mm; border-radius: 99px; }
.tl .val { font-size: 8.5pt; color: var(--grey); text-align: right; font-weight: 600; }
.tl .scale { display: grid; grid-template-columns: 52mm 1fr 20mm; gap: 3mm; font-size: 7.5pt; color: #8a8a96; margin-top: 1.5mm; }
.tl .scale div:nth-child(2) { display: flex; justify-content: space-between; }
.legend { display: flex; gap: 6mm; font-size: 8.5pt; color: var(--grey); margin: 2mm 0 5mm; }
.legend span::before { content: ''; display: inline-block; width: 3.5mm; height: 3.5mm; border-radius: 1mm; margin-right: 1.5mm; vertical-align: -0.5mm; background: var(--c); }

/* week opener */
.week { padding: 0; }
.week .photo { height: 150mm; background-size: cover; background-position: center; position: relative; }
.week .photo::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(6,29,37,.1), rgba(6,29,37,.85)); }
.week .ttl { position: absolute; left: 16mm; bottom: 12mm; z-index: 2; color: #fff; }
.week .ttl small { font-size: 11pt; font-weight: 800; letter-spacing: .2em; text-transform: uppercase; color: var(--orange); }
.week .ttl h2 { color: #fff; font-size: 44pt; font-weight: 900; margin: 1mm 0 0; }
.week .wlogo { position: absolute; top: 14mm; left: 16mm; height: 9mm; z-index: 2; }
.week .body { padding: 10mm 16mm 0; display: grid; grid-template-columns: 1.15fr 1fr; gap: 9mm; }
.week .body p { font-size: 11.5pt; color: var(--grey); }
.week .days { list-style: none; margin-top: 5mm; }
.week .days li { display: flex; gap: 3mm; align-items: center; padding: 2mm 0; border-bottom: 0.25mm dashed var(--line); font-size: 9.6pt; }
.week .days li span { font-weight: 800; color: var(--orange); min-width: 13mm; }
.outcomes { background: var(--navy); color: #fff; border-radius: 4mm; padding: 6mm; align-self: start; }
.outcomes h3 { color: #fff; font-size: 11pt; margin-bottom: 3mm; }
.outcomes li { list-style: none; padding: 1.8mm 0 1.8mm 7mm; position: relative; font-size: 9.6pt; color: #dfe6e8; }
.outcomes li::before { content: '✓'; position: absolute; left: 0; color: var(--orange); font-weight: 900; }

/* day page */
.dayhead { display: flex; align-items: flex-end; gap: 6mm; margin-bottom: 5mm; }
.daynum { background: var(--orange); color: #fff; border-radius: 4mm; width: 30mm; height: 30mm; display: flex; flex-direction: column;
  align-items: center; justify-content: center; flex-shrink: 0; }
.daynum small { font-size: 8pt; font-weight: 700; letter-spacing: .2em; }
.daynum b { font-size: 34pt; font-weight: 900; line-height: 1; }
.dayhead h2 { font-size: 25pt; margin: 0 0 1mm; }
.progress { display: flex; gap: 0.8mm; margin-top: 2.5mm; }
.progress i { width: 3.2mm; height: 1.6mm; border-radius: 1mm; background: var(--line); }
.progress i.on { background: var(--orange); }
.progress i.now { background: var(--navy); }
.goal { background: var(--cream); border-radius: 3mm; padding: 4.5mm 6mm; display: flex; gap: 4mm; align-items: center; margin-bottom: 6mm; }
.goal .ic { flex-shrink: 0; width: 10mm; height: 10mm; border-radius: 50%; background: var(--orange); position: relative; }
.goal .ic::before, .goal .ic::after { content: ''; position: absolute; border-radius: 50%; border: 0.6mm solid #fff; }
.goal .ic::before { inset: 2mm; } .goal .ic::after { inset: 3.9mm; background: #fff; }
.goal small { display: block; font-size: 7.5pt; font-weight: 800; letter-spacing: .16em; color: var(--orange); text-transform: uppercase; }
.goal p { font-size: 13pt; font-weight: 600; color: var(--navy); }
.actions { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; margin-bottom: 6mm; }
.act { border: 0.3mm solid var(--line); border-radius: 4mm; padding: 5mm; }
.act .lab { font-size: 7.5pt; font-weight: 800; letter-spacing: .16em; color: var(--orange); text-transform: uppercase; }
.act h3 { margin: 1mm 0 3.5mm; min-height: 11mm; font-size: 13.5pt; }
.act ol { list-style: none; counter-reset: s; }
.act li { counter-increment: s; position: relative; padding: 0 0 3mm 8mm; font-size: 10.4pt; color: var(--grey); }
.act li::before { content: counter(s); position: absolute; left: 0; top: 0.2mm; width: 5.4mm; height: 5.4mm; border-radius: 50%;
  background: var(--navy); color: #fff; font-size: 7.5pt; font-weight: 800; text-align: center; line-height: 5.4mm; }
.duo { display: grid; grid-template-columns: 1.35fr 1fr; gap: 5mm; }
.tip { background: var(--navy); color: #dfe6e8; border-radius: 4mm; padding: 6mm 6.5mm; font-size: 10.4pt; position: relative; }
.tip .lab { display: flex; align-items: center; gap: 2mm; color: var(--orange); font-size: 7.5pt; font-weight: 800;
  letter-spacing: .16em; text-transform: uppercase; margin-bottom: 2mm; }
.tip .lab::before { content: '★'; font-size: 10pt; }
.docs { background: var(--mist); border-radius: 4mm; padding: 5.5mm 6mm; }
.docs .lab { color: var(--navy); font-size: 7.5pt; font-weight: 800; letter-spacing: .16em; text-transform: uppercase; margin-bottom: 2mm; }
.docs li { list-style: none; font-size: 9.8pt; color: var(--grey); padding: 0.9mm 0 0.9mm 6mm; position: relative; }
.docs li::before { content: ''; position: absolute; left: 0; top: 1.6mm; width: 3mm; height: 3mm; border: 0.35mm solid var(--orange); border-radius: 0.7mm; }
.page.day { display: flex; flex-direction: column; }
.notes { margin-top: 6mm; display: grid; grid-template-columns: 1fr 44mm; gap: 6mm; flex: 1; margin-bottom: 4mm; }
.notes .lines { background: repeating-linear-gradient(180deg, transparent 0 8.7mm, var(--line) 8.7mm 9mm); background-position: 0 4mm; }
.notes .lines { font-size: 7.5pt; font-weight: 800; letter-spacing: .16em; color: #8a8a96; text-transform: uppercase; }
.done { align-self: start; border: 0.4mm dashed var(--orange); border-radius: 4mm; padding: 4mm; text-align: center; font-size: 8.5pt; color: var(--grey); }
.done .box { width: 9mm; height: 9mm; border: 0.6mm solid var(--orange); border-radius: 2mm; margin: 0 auto 2mm; }
.done b { display: block; color: var(--navy); font-size: 10pt; }
.done .dt { margin-top: 3mm; border-top: 0.3mm solid var(--line); padding-top: 1.5mm; font-size: 7.5pt; text-align: left; }

/* tracker */
.tracker { display: grid; grid-template-columns: repeat(5, 1fr); gap: 3mm; }
.tracker div { border: 0.3mm solid var(--line); border-radius: 3mm; padding: 3mm; height: 33mm; display: flex; flex-direction: column; }
.tracker div small { font-size: 7pt; font-weight: 800; letter-spacing: .12em; color: var(--orange); }
.tracker div p { font-size: 8.2pt; color: var(--navy); font-weight: 600; line-height: 1.25; margin-top: 1mm; }
.tracker div i { margin-top: auto; align-self: flex-end; width: 6mm; height: 6mm; border: 0.5mm solid var(--orange); border-radius: 1.5mm; }
.tracker div.w2 small, .tracker div.w4 small { color: var(--navy); }

/* checklists */
.cl { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; }
.cl section { border: 0.3mm solid var(--line); border-radius: 4mm; padding: 5mm; }
.cl section.wide { grid-column: span 2; }
.cl h3 { font-size: 11pt; margin-bottom: 2.5mm; padding-bottom: 2mm; border-bottom: 0.6mm solid var(--orange); }
.cl ul { list-style: none; }
.cl section.wide ul { columns: 2; column-gap: 8mm; }
.cl li { font-size: 9.2pt; color: var(--grey); padding: 1.5mm 0 1.5mm 7mm; position: relative; break-inside: avoid; }
.cl li::before { content: ''; position: absolute; left: 0; top: 1.9mm; width: 3.8mm; height: 3.8mm; border: 0.4mm solid var(--navy); border-radius: 0.9mm; }

/* glossary + faq */
.gl { columns: 2; column-gap: 8mm; }
.gl div { break-inside: avoid; padding: 2.4mm 0; border-bottom: 0.25mm solid var(--line); font-size: 9.2pt; color: var(--grey); }
.gl b { color: var(--navy); display: block; font-size: 9.8pt; }
.faq div { padding: 4mm 0; border-bottom: 0.3mm solid var(--line); }
.faq h3 { font-size: 11pt; margin-bottom: 1.2mm; }
.faq h3::before { content: 'Q. '; color: var(--orange); }
.faq p { font-size: 9.8pt; color: var(--grey); }
.disc { font-size: 7.8pt; color: #8a8a96; margin-top: 6mm; line-height: 1.5; }

/* back cover */
.back { background: var(--navy); color: #fff; padding: 0; }
.back .photo { height: 112mm; background: url('assets/photos/celebrate.jpg') center 30%/cover; position: relative; }
.back .photo::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(6,29,37,0) 40%, #061D25 100%); }
.back .inner { padding: 4mm 18mm 0; }
.back h2 { color: #fff; font-size: 34pt; font-weight: 900; }
.back h2 span { color: var(--orange); }
.back .sub { color: #c6d1d4; font-size: 12pt; margin: 3mm 0 7mm; max-width: 165mm; }
.back .grid { display: grid; grid-template-columns: 1fr 46mm; gap: 8mm; align-items: start; }
.back ul { list-style: none; }
.back li { padding: 2.2mm 0; border-bottom: 0.3mm solid rgba(255,255,255,.12); font-size: 10.5pt; display: flex; gap: 4mm; }
.back li small { width: 24mm; color: var(--orange); font-weight: 800; font-size: 7.5pt; letter-spacing: .14em; text-transform: uppercase; padding-top: 0.8mm; }
.back .qr { background: #fff; border-radius: 4mm; padding: 4mm; text-align: center; color: var(--navy); font-size: 8pt; font-weight: 700; }
.back .qr svg { width: 38mm; height: 38mm; display: block; margin: 0 auto 2mm; }
.back .cta { display: inline-block; background: var(--orange); color: #fff; font-weight: 800; padding: 3.5mm 7mm; border-radius: 99px; font-size: 11pt; margin-top: 7mm; }
.back .services { margin-top: 7mm; display: flex; flex-wrap: wrap; gap: 2mm; }
.back .services span { border: 0.3mm solid rgba(255,255,255,.25); border-radius: 99px; padding: 1.2mm 3.5mm; font-size: 8.2pt; color: #dfe6e8; }
.back .logo { position: absolute; bottom: 12mm; left: 18mm; height: 10mm; }
.back .fine { position: absolute; bottom: 12mm; right: 18mm; font-size: 7pt; color: #7f9297; text-align: right; max-width: 110mm; }
"""

DAYS_BY_WEEK = {w["num"]: [d for d in DAYS if d["week"] == w["num"]] for w in WEEKS}
WEEK_NAME = {w["num"]: w["name"] for w in WEEKS}


class Doc:
    def __init__(self):
        self.pages = []

    def add(self, body, cls="", footer=True, chip=None):
        n = len(self.pages) + 1
        top = ""
        if chip is not None:
            top = (f'<div class="top"><img src="assets/brand/Logo-Black.png" alt="Startup Zone">'
                   f'<span class="chip">{chip}</span></div>')
        foot = (f'<div class="foot"><span>The 30-Day UAE Business Setup Guide · {CONTACT["web"]}</span>'
                f'<span class="pg">{n:02d}</span></div>') if footer else ""
        self.pages.append(f'<section class="page {cls}">{top}{body}{foot}</section>')
        return n


def cover():
    return f"""
<div class="photo"></div><div class="shade"></div>
<div class="inner">
  <img class="logo" src="assets/brand/Logo-white.png" alt="Startup Zone">
  <span class="badge">For overseas investors</span>
  <h1>Your UAE company<br>in <span>30 days</span></h1>
  <p class="sub">A friendly, day-by-day guide to setting up your business, getting your residence
  visa and opening for business in the UAE, from anywhere in the world.</p>
  <div class="stats">
    <div><b>30</b>simple daily steps</div>
    <div><b>4</b>free zones compared</div>
    <div><b>100%</b>foreign ownership</div>
    <div><b>1,000+</b>founders helped</div>
  </div>
  <div class="ed">{EDITION} · thestartupzone.ae</div>
</div>"""


def welcome():
    return f"""
<div class="kicker">Welcome</div>
<h2>Your UAE business starts here</h2>
<div class="hero-img" style="background-image:url('assets/photos/burj-khalifa.jpg')"></div>
<p class="lead">Thousands of founders from around the world choose the UAE every year. This guide
breaks the whole journey into 30 small, doable steps, one page per day, so you always know
exactly what to do next.</p>
<div class="howto">
  <div><i>1</i><b>One page a day</b>Each day has one goal and two short actions with numbered steps.</div>
  <div><i>2</i><b>Pro tips</b>Insider advice from our team that saves you time, money and stress.</div>
  <div><i>3</i><b>Tick as you go</b>Mark each day done and track progress on the 30-day tracker.</div>
  <div><i>4</i><b>Tools at the back</b>Checklists, a timeline, a compliance calendar and a glossary.</div>
</div>
<div class="sign"><b>You don't have to do this alone.</b> Every step in this guide is something our team
handles for clients every day. Stuck, or want it done for you? Message us on WhatsApp at
<b>{CONTACT["phone"]}</b>.</div>"""


def why_uae():
    cards = "".join(f'<div><b>{e(a)}</b><h3>{e(b)}</h3><p>{e(c)}</p></div>' for a, b, c in WHY_UAE)
    return f"""
<div class="kicker">Why the UAE</div>
<h2>Six reasons founders choose the UAE</h2>
<p class="lead">A safe, modern and business-friendly base with low taxes and world-class connections.</p>
<div class="why">{cards}</div>
<div class="strip" style="background-image:url('assets/photos/dubai-night.jpg')"></div>"""


def roadmap():
    cols = ""
    for w in WEEKS:
        items = "".join(f'<li><span>{d["day"]:02d}</span>{e(d["title"])}</li>' for d in DAYS_BY_WEEK[w["num"]])
        cols += (f'<div class="wk"><header><small>Week {w["num"]}</small><b>{w["name"]}</b></header>'
                 f'<ol>{items}</ol></div>')
    return f"""
<div class="kicker">Your roadmap</div>
<h2>30 days at a glance</h2>
<p class="lead">Four weeks, four milestones. Follow the days in order, or jump to the step you're on.</p>
<div class="road">{cols}</div>
<div class="note"><b>Good to know:</b> "Day" means a step, not a fixed calendar date. Government
processing times vary, and some steps (like bank accounts) can take longer. Many steps also
run in parallel. The timeline on page 07 shows typical durations.</div>"""


def mainland_vs_fz():
    rows = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td></tr>" for a, b, c in MAINLAND_VS_FZ)
    return f"""
<div class="kicker">Day 3 companion</div>
<h2>Mainland vs free zone</h2>
<p class="lead">Both let you own 100% of your company. The right choice depends on who your customers are
and where you'll do business.</p>
<table><tr><th>&nbsp;</th><th>Mainland</th><th class="fz">Free zone</th></tr>{rows}</table>
<div class="note"><b>Our view for overseas investors:</b> if you serve international clients, sell
online or offer consulting, a free zone is usually faster, simpler and more cost-effective. You
can always add a mainland branch later as you grow.</div>"""


def free_zones():
    cards = ""
    for z in FREE_ZONES:
        li = "".join(f"<li>{e(s)}</li>" for s in z["strengths"])
        cards += f"""<div class="fz-card"><span class="tag">{e(z["vibe"])}</span><h3>{z["code"]}</h3>
<div class="nm">{e(z["name"])}</div><div class="em">{e(z["emirate"])}</div>
<div class="best"><b>Best for:</b> {e(z["best"])}</div><ul>{li}</ul>
<div class="off"><b>Office options:</b> {e(z["office"])}</div></div>"""
    return f"""
<div class="kicker">Day 4 companion</div>
<h2>Four free zones we recommend</h2>
<p class="lead">Each one is fully open to overseas founders. Pick the one that fits your business, your
budget and the address your clients expect.</p>
<div class="fzs">{cards}</div>
<div class="note"><b>Pricing changes often</b>, so ask us for a current all-in quote showing year-1 and renewal
costs side by side, with our service fee included.</div>"""


def timeline():
    colors = ["#061D25", "#FF5900", "#FF9874", "#474752"]
    maxd = 30
    rows = ""
    for step, lo, hi, w in TIMELINE:
        left = (lo - 1) / maxd * 100
        width = max((hi - lo + 1) / maxd * 100, 3)
        rows += (f'<div class="row"><div class="lbl">{e(step)}</div><div class="track">'
                 f'<div class="bar" style="left:0;width:{lo / maxd * 100:.1f}%;background:{colors[w]};opacity:.35"></div>'
                 f'<div class="bar" style="left:{left:.1f}%;width:{width:.1f}%;background:{colors[w]}"></div></div>'
                 f'<div class="val">{lo}–{hi} days</div></div>')
    legend = "".join(f'<span style="--c:{colors[i]}">Week {i + 1}: {WEEKS[i]["name"]}</span>' for i in range(4))
    return f"""
<div class="kicker">Timeline</div>
<h2>How long does each step take?</h2>
<p class="lead">Typical processing times in working days once your documents are complete. Many steps
overlap, which is how a full setup fits into about a month.</p>
<div class="legend">{legend}</div>
<div class="tl">{rows}<div class="scale"><div></div><div><span>0</span><span>5</span><span>10</span><span>15</span><span>20</span><span>25</span><span>30 days</span></div><div></div></div></div>
<div class="note"><b>Speed it up:</b> clear scans, quick answers to compliance questions and booking your
UAE trip as soon as your entry permit is issued are the three biggest time savers. Times are
typical, not guaranteed, and vary by free zone, nationality and bank.</div>"""


def week_page(w):
    days = "".join(f'<li><span>Day {d["day"]:02d}</span>{e(d["title"])}</li>' for d in DAYS_BY_WEEK[w["num"]])
    outs = "".join(f"<li>{e(o)}</li>" for o in w["outcomes"])
    return f"""
<div class="photo" style="background-image:url('assets/photos/{w["photo"]}.jpg')">
  <img class="wlogo" src="assets/brand/Logo-white.png" alt="Startup Zone">
  <div class="ttl"><small>Week {w["num"]} · {w["name"]}</small><h2>{e(w["headline"])}</h2></div>
</div>
<div class="body">
  <div><p>{e(w["intro"])}</p><ul class="days">{days}</ul></div>
  <div class="outcomes"><h3>By the end of this week you'll have</h3><ul>{outs}</ul></div>
</div>"""


def day_page(d):
    prog = "".join(f'<i class="{"on" if i < d["day"] else "now" if i == d["day"] else ""}"></i>' for i in range(1, 31))

    def act(lab, a):
        steps = "".join(f"<li>{e(s)}</li>" for s in a[1])
        return f'<div class="act"><div class="lab">{lab}</div><h3>{e(a[0])}</h3><ol>{steps}</ol></div>'

    docs = "".join(f"<li>{e(x)}</li>" for x in d["docs"])
    return f"""
<div class="dayhead">
  <div class="daynum"><small>DAY</small><b>{d["day"]:02d}</b></div>
  <div><h2>{e(d["title"])}</h2><div class="progress">{prog}</div></div>
</div>
<div class="goal"><div class="ic"></div><div><small>Today's goal</small><p>{e(d["goal"])}</p></div></div>
<div class="actions">{act("Action 1", d["a1"])}{act("Action 2", d["a2"])}</div>
<div class="duo">
  <div class="tip"><div class="lab">Startup Zone pro tip</div>{e(d["tip"])}</div>
  <div class="docs"><div class="lab">Documents needed</div><ul>{docs}</ul></div>
</div>
<div class="notes">
  <div class="lines">My notes</div>
  <div class="done"><div class="box"></div><b>Day {d["day"]} done!</b><div class="dt">Date: ____ / ____ / ______</div></div>
</div>"""


def tracker():
    cells = "".join(f'<div class="w{d["week"]}"><small>DAY {d["day"]:02d} · {WEEK_NAME[d["week"]].upper()}</small>'
                    f'<p>{e(d["title"])}</p><i></i></div>' for d in DAYS)
    return f"""
<div class="kicker">Progress tracker</div>
<h2>Your 30-day tracker</h2>
<p class="lead">Tick each box as you finish a day. Pin this page somewhere you'll see it.</p>
<div class="tracker">{cells}</div>"""


def checklist_page(kicker, title, lead, groups, wide_last=False):
    secs = ""
    for i, (h, items) in enumerate(groups):
        cls = "wide" if wide_last and i == len(groups) - 1 else ""
        secs += f'<section class="{cls}"><h3>{e(h)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></section>'
    return f"""<div class="kicker">{kicker}</div><h2>{title}</h2><p class="lead">{lead}</p><div class="cl">{secs}</div>"""


def compliance():
    rows = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td><td style='width:14mm'>&nbsp;</td></tr>" for a, b, c in COMPLIANCE)
    return f"""
<div class="kicker">Day 30 companion</div>
<h2>Your compliance calendar</h2>
<p class="lead">The dates every UAE company owner must know. Write your own due dates in the last column.</p>
<table><tr><th>What</th><th>How often</th><th>Key point</th><th>My date</th></tr>{rows}</table>
<div class="note"><b>Never miss a deadline:</b> Startup Zone's accounting and compliance clients get
reminders for every renewal and tax filing, plus bookkeeping, VAT and Corporate Tax returns handled
for them.</div>"""


def glossary():
    items = "".join(f"<div><b>{e(a)}</b>{e(b)}</div>" for a, b in GLOSSARY)
    return f"""<div class="kicker">Glossary</div><h2>UAE business terms, made simple</h2>
<p class="lead">The words you'll hear most during your setup, in plain English.</p><div class="gl">{items}</div>"""


def faq():
    items = "".join(f"<div><h3>{e(q)}</h3><p>{e(a)}</p></div>" for q, a in FAQ)
    return f"""<div class="kicker">FAQ</div><h2>Questions overseas investors ask us</h2>
<div class="faq">{items}</div>
<p class="disc"><b>Important:</b> This guide is general information correct as of {EDITION.replace(" Edition", "")}.
It is not legal or tax advice. UAE rules, fees, processing times and requirements change regularly and
vary by free zone, nationality and bank. Speak to the Startup Zone team for advice on your situation.
Photos: Unsplash.</p>"""


def back():
    return f"""
<div class="photo"></div>
<div class="inner">
  <h2>Ready to start? <span>We'll do it with you.</span></h2>
  <p class="sub">From your first question to your first invoice, Startup Zone handles your company
  setup, visas, bank introductions, VAT, Corporate Tax and bookkeeping, at a fixed price with no surprises.</p>
  <div class="grid">
    <ul>
      <li><small>WhatsApp</small>{CONTACT["phone"]}</li>
      <li><small>Email</small>{CONTACT["email"]}</li>
      <li><small>Website</small>{CONTACT["web"]}</li>
      <li><small>Visit us</small>{CONTACT["address"]}</li>
    </ul>
    <div class="qr">{QR}Scan to chat on WhatsApp</div>
  </div>
  <span class="cta">Book your free consultation →</span>
  <div class="services"><span>Free zone setup</span><span>Mainland setup</span><span>Residence visas</span>
  <span>Bank account support</span><span>VAT</span><span>Corporate Tax</span><span>Bookkeeping & accounting</span></div>
</div>
<img class="logo" src="assets/brand/Logo-white.png" alt="Startup Zone">
<div class="fine">1,000+ clients · 5.0 on Google<br>© 2026 Startup Zone. General information only, not legal or tax advice.</div>"""


def build():
    doc = Doc()
    doc.add(cover(), "cover", footer=False)
    doc.add(welcome(), chip="Start here")
    doc.add(why_uae(), chip="Why the UAE")
    doc.add(roadmap(), chip="Roadmap")
    doc.add(mainland_vs_fz(), chip="Compare")
    doc.add(free_zones(), chip="Compare")
    doc.add(timeline(), chip="Timeline")
    for w in WEEKS:
        doc.add(week_page(w), "week")
        for d in DAYS_BY_WEEK[w["num"]]:
            doc.add(day_page(d), "day", chip=f'Week {w["num"]} · <b>{w["name"]}</b>')
    doc.add(tracker(), chip="Tracker")
    doc.add(checklist_page("Checklist", "Master document checklist",
                           "Everything you'll provide and receive. Tick each item as it's ready.",
                           DOC_CHECKLIST), chip="Checklists")
    doc.add(checklist_page("Day 24 companion", "Bank account readiness checklist",
                           "Banks open accounts for businesses they understand. A complete pack is your fastest route to a yes.",
                           BANK_CHECKLIST, wide_last=True), chip="Checklists")
    doc.add(compliance(), chip="Compliance")
    doc.add(glossary(), chip="Glossary")
    doc.add(faq(), chip="FAQ")
    doc.add(back(), "back", footer=False)
    html = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            f'<title>The 30-Day UAE Business Setup Guide | Startup Zone</title><style>{CSS}</style></head>'
            f'<body>{"".join(doc.pages)}</body></html>')
    (HERE / "guide.html").write_text(html)
    print(f"guide.html written: {len(doc.pages)} pages")


if __name__ == "__main__":
    build()
