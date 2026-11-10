"""Builds guide.html for 'Your UAE Licence in 1 Day'. Run: python3 build.py && node render.js

All text lives in the CONTENT section below. Prices and timelines come from the Startup Zone
website and proposal system (November 2026) - check them before each reprint.
"""
from html import escape as e
from pathlib import Path

HERE = Path(__file__).parent
QR = (HERE / "assets/brand/whatsapp-qr.svg").read_text().split("?>", 1)[-1]

# ============================== CONTENT ==============================
EDITION = "November 2026"
CONTACT = dict(phone="+971 52 346 9382", email="info@thestartupzone.ae", web="thestartupzone.ae",
               address="Latifa Tower, Suite 801, Sheikh Zayed Road, Dubai, UAE")

STAGES = [
    ("Stage 1", "Trade licence", "1 working day*", "Choose your free zone, send your documents, complete KYC and e-sign. Your licence is issued the same day."),
    ("Stage 2", "Residence visa", "About 2–3 weeks", "Establishment card, entry permit, medical test and Emirates ID. You visit the UAE for about a week."),
    ("Stage 3", "Bank & tax", "Runs alongside", "Open your corporate bank account and register for Corporate Tax within 90 days."),
]

ONE_DAY_NEEDS = [
    ("Documents ready", "Clear passport scans, photo, 3 company name options and contact details, all received before we submit."),
    ("Shareholders on hand", "Every shareholder completes the online KYC tasks and e-signs the MOA on the same day."),
    ("A standard activity", "Most trading, consulting, media and e-commerce activities qualify. We confirm yours in your first call."),
]

TERMS = [
    "Licence in 1 working day is available for SHAMS and ANCFZ (also SPC and AFZ). IFZA and RAKEZ licences typically take about a week.",
    "All documents must be complete, clear and received before submission. Unclear scans or missing items restart the clock.",
    "Activities that need an outside approval (for example from a ministry, regulator or municipality) take longer. Some approvals are needed before the licence, others after it.",
    "The free zone may request enhanced due diligence (EDD), for example for certain nationalities, activities, sources of funds or business models. EDD adds time and the free zone's decision is final.",
    "Security checks, where required, must be cleared first. Corporate shareholders need attested company documents, which adds time.",
    "Working days only (Monday to Friday, excluding UAE public holidays) and subject to free zone systems being available.",
    "Licence and visa approvals are at the sole discretion of the free zone and UAE authorities.",
]

LICENCE_DAY = [
    ("Pick your activity & free zone", "A quick call or WhatsApp chat. We match your business to the right activity and free zone.", "You + Startup Zone"),
    ("Send your documents", "Passport scans, photo, 3 name options and contact details for every shareholder.", "You"),
    ("We submit & you pay", "We prepare and submit your application. You pay the package fee.", "Startup Zone"),
    ("Complete your KYC", "A short online compliance task on the free zone portal for each shareholder.", "You & shareholders"),
    ("E-sign your MOA", "Sign your Memorandum of Association online. No travel needed.", "All shareholders"),
    ("Licence issued", "Your trade licence, MOA, share certificate and lease agreement arrive by email.", "Free zone"),
]

FREE_ZONES = [
    dict(code="SHAMS", name="Sharjah Media City", emirate="Sharjah", speed="1-day licence*", fast=True,
         price="6,885", visa="With 1 visa, year 1 from AED 14,295 (health insurance by you)",
         best="Media, creative, consulting and e-commerce",
         facts=["Up to 5 activities, up to 10 shareholders", "Virtual office lease and share certificate included",
                "Bank account opening support (Wio / Mashreq Neo)"]),
    dict(code="ANCFZ", name="Ajman Nuventure Centre Free Zone", emirate="Ajman", speed="1-day licence*", fast=True,
         price="4,888", visa="With 1 visa, all-in year 1 from AED 10,800",
         best="Startups, freelancers and budget-conscious founders",
         facts=["Up to 10 activities, up to 10 shareholders", "All-inclusive packages from 0 to 7 visas",
                "Visa, medical, Emirates ID and change of status included"]),
    dict(code="IFZA", name="International Free Zone Authority", emirate="Dubai", speed="About 1 week", fast=False,
         price="12,900", visa="With 1 visa, all-in year 1 from AED 22,050",
         best="Consultancy, trading and tech wanting a Dubai address",
         facts=["3 activities and 3 shareholders included", "15% off the licence on 2-year packages",
                "Dubai address and strong recognition"]),
    dict(code="RAKEZ", name="Ras Al Khaimah Economic Zone", emirate="Ras Al Khaimah", speed="About 1 week", fast=False,
         price="6,000", visa="1-visa bundles from AED 12,000 (RAKEZ package price)",
         best="Trading, manufacturing and growing teams",
         facts=["All-in bundles: licence, lease and establishment card", "Each visa includes entry permit, medical and Emirates ID",
                "Same bundle price every year at renewal"]),
]

DOCS = [
    ("For your licence", [
        "Clear colour scan of every shareholder's passport (photos of passports not accepted)",
        "Passport-size photo of each shareholder (white background)",
        "At least 3 options for your company name",
        "Phone, email and home address of each shareholder",
        "UAE visa or Emirates ID copy, if a shareholder lives in the UAE",
    ]),
    ("For each visa", [
        "Passport copy of each applicant (at least 6 months valid)",
        "Passport-size photo (white background)",
        "Visit visa or entry stamp copy, if the applicant is already in the UAE",
        "Health insurance for each visa holder",
    ]),
    ("If a company is the shareholder", [
        "Certificate of incorporation or trade licence of the parent company",
        "Memorandum & Articles of Association of the parent company",
        "Board resolution appointing the company's representative",
        "Documents issued outside the UAE must be legalised / attested",
    ]),
]

VISA_STEPS = [
    ("Establishment card", "Lets your company sponsor visas. Applied right after your licence.", "2–3 days"),
    ("E-visa (entry permit)", "Your permit to enter the UAE as a future resident.", "1–2 days"),
    ("Change of status", "Only if you're already in the UAE on a visit visa.", "2 days"),
    ("Medical test", "Quick blood test and X-ray at an approved centre.", "2 days"),
    ("Emirates ID biometrics", "Fingerprints and photo for your Emirates ID.", "4 days"),
    ("Residency issued", "Your residence visa, linked to your Emirates ID.", "3 days"),
]

BANK_LIST = [
    "Trade licence, MOA and share certificate",
    "Passport, residence visa and Emirates ID of each signatory",
    "A short business plan with expected monthly turnover",
    "CV or LinkedIn profile showing your experience",
    "Proof of source of funds and 6 months of personal bank statements",
    "Contracts, invoices or letters of intent from clients",
]

COMPLIANCE = [
    ("Corporate Tax registration", "Within 90 days of incorporation", "Late registration penalty: AED 10,000"),
    ("Corporate Tax return", "Every year", "Due within 9 months of financial year end"),
    ("VAT registration", "When turnover qualifies", "Voluntary from AED 187,500; mandatory from AED 375,000"),
    ("VAT return", "Every quarter", "Due within 28 days of quarter end"),
    ("Licence renewal", "Every year", "Renew before expiry to avoid fines"),
    ("Visa & Emirates ID", "Typically every 2 years", "Avoid staying outside the UAE more than 6 months in a row"),
    ("Changes to the company", "When they happen", "Shareholder changes and amendments must also be updated with the FTA"),
]

FAQ = [
    ("Is the licence really issued in one day?",
     "Yes, for SHAMS and ANCFZ when your documents are complete, your activity needs no outside approval and no extra checks are requested. See the terms on page 03."),
    ("Do I need to travel to the UAE?",
     "Not for your licence: it's fully online. You visit for about a week for your visa medical test and Emirates ID."),
    ("Can I own 100% of my company?",
     "Yes. All four free zones in this guide allow 100% foreign ownership."),
    ("What if my activity needs an approval?",
     "We tell you in your first call, explain the extra time and cost, and handle the approval for you."),
    ("Will I pay tax?",
     "No personal income tax. Your company pays 9% Corporate Tax on profit above AED 375,000, or 0% on qualifying free zone income. VAT is 5% once registered."),
    ("Can you handle my accounting too?",
     "Yes. Bookkeeping, VAT and Corporate Tax registrations and returns, all under one roof."),
]

# ============================== LAYOUT ==============================
CSS = """
@font-face { font-family: 'InterV'; src: url('assets/fonts/inter-latin-wght-normal.woff2') format('woff2'); font-weight: 100 900; }
:root { --orange:#FF5900; --navy:#061D25; --ink:#110024; --peach:#FDCEBE; --mist:#F9F8FC; --line:#E2E2E8; --grey:#474752; --cream:#FFF4EE; --green:#1F7A4D; }
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'InterV', 'Inter', sans-serif; color: var(--ink); font-size: 10.5pt; line-height: 1.45; }
.page { width: 210mm; height: 297mm; position: relative; overflow: hidden; page-break-after: always; background: #fff; padding: 16mm 16mm 18mm; }
.page:last-child { page-break-after: auto; }
h2 { color: var(--navy); font-size: 26pt; font-weight: 800; line-height: 1.1; letter-spacing: -0.015em; margin-bottom: 3mm; }
h2 span { color: var(--orange); }
h3 { color: var(--navy); font-size: 12.5pt; font-weight: 700; line-height: 1.2; }
.kicker { color: var(--orange); font-weight: 700; font-size: 9pt; letter-spacing: .14em; text-transform: uppercase; margin-bottom: 2mm; }
.lead { font-size: 11.5pt; color: var(--grey); max-width: 165mm; margin-bottom: 7mm; }
.top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 9mm; }
.top img { height: 8mm; }
.chip { background: var(--navy); color: #fff; border-radius: 99px; padding: 1.3mm 4mm; font-size: 8pt; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
.foot { position: absolute; left: 16mm; right: 16mm; bottom: 8mm; display: flex; justify-content: space-between; font-size: 7.5pt; color: #8a8a96; border-top: 0.3mm solid var(--line); padding-top: 2.5mm; }
.foot b { color: var(--navy); }
.note { font-size: 9pt; color: var(--grey); background: var(--mist); padding: 4mm 5mm; border-radius: 3mm; margin-top: 6mm; }
.note b { color: var(--navy); }

/* cover */
.cover { padding: 0; background: var(--navy); color: #fff; }
.cover .photo { position: absolute; inset: 0; background: url('assets/photos/cover.jpg') center/cover; }
.cover .shade { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(6,29,37,.1) 0%, rgba(6,29,37,.3) 38%, rgba(6,29,37,.95) 66%, #061D25 100%); }
.cover .inner { position: absolute; inset: 0; padding: 18mm; display: flex; flex-direction: column; }
.cover .logo { height: 13mm; align-self: flex-start; }
.cover .badge { margin-top: auto; background: var(--orange); color: #fff; font-weight: 800; font-size: 10pt; letter-spacing: .14em; text-transform: uppercase; padding: 2mm 5mm; border-radius: 1.5mm; align-self: flex-start; }
.cover h1 { color: #fff; font-size: 54pt; font-weight: 900; line-height: .97; margin: 6mm 0 5mm; letter-spacing: -0.03em; }
.cover h1 span { color: var(--orange); }
.cover .sub { font-size: 14pt; color: #dfe6e8; max-width: 155mm; margin-bottom: 9mm; }
.cover .stats { display: flex; border-top: 0.4mm solid rgba(255,255,255,.25); padding-top: 6mm; }
.cover .stats div { flex: 1; font-size: 8.5pt; color: #b9c6ca; }
.cover .stats b { display: block; font-size: 17pt; color: #fff; font-weight: 800; }
.cover .ed { margin-top: 7mm; font-size: 7.5pt; color: #8fa1a6; }

/* stages */
.stages { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4mm; position: relative; }
.stage { border-radius: 4mm; padding: 6mm 5mm; background: var(--mist); position: relative; }
.stage.s1 { background: var(--orange); color: #fff; }
.stage small { font-size: 7.5pt; font-weight: 800; letter-spacing: .16em; text-transform: uppercase; opacity: .75; }
.stage h3 { font-size: 15pt; margin: 1.5mm 0 1mm; }
.stage.s1 h3 { color: #fff; }
.stage .t { display: inline-block; font-size: 9pt; font-weight: 800; padding: 1mm 3mm; border-radius: 99px; background: var(--navy); color: #fff; margin-bottom: 3mm; }
.stage.s1 .t { background: #fff; color: var(--orange); }
.stage p { font-size: 9.6pt; color: var(--grey); }
.stage.s1 p { color: #fff; }
.photo-strip { height: 92mm; border-radius: 4mm; margin-top: 7mm; background-size: cover; background-position: center; }
.why { display: grid; grid-template-columns: repeat(4, 1fr); gap: 3mm; margin-top: 6mm; }
.why div { border: 0.3mm solid var(--line); border-radius: 3mm; padding: 4mm; font-size: 8.6pt; color: var(--grey); }
.why b { display: block; font-size: 17pt; font-weight: 900; color: var(--orange); line-height: 1.1; }

/* promise + terms */
.needs { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4mm; margin-bottom: 7mm; }
.needs div { background: var(--cream); border-radius: 4mm; padding: 5mm; font-size: 9.4pt; color: var(--grey); }
.needs i { font-style: normal; display: block; width: 8mm; height: 8mm; border-radius: 50%; background: var(--orange); color: #fff; text-align: center; line-height: 8mm; font-weight: 900; margin-bottom: 3mm; }
.needs b { display: block; color: var(--navy); font-size: 11pt; margin-bottom: 1mm; }
.terms { border: 0.4mm solid var(--navy); border-radius: 4mm; padding: 6mm 7mm; }
.terms h3 { margin-bottom: 3mm; }
.terms ol { list-style: none; counter-reset: t; }
.terms li { counter-increment: t; position: relative; padding: 1.6mm 0 1.6mm 8mm; font-size: 9.4pt; color: var(--grey); border-bottom: 0.25mm dashed var(--line); }
.terms li:last-child { border: 0; }
.terms li::before { content: counter(t); position: absolute; left: 0; top: 2mm; width: 5mm; height: 5mm; border-radius: 50%; background: var(--navy); color: #fff; font-size: 7pt; font-weight: 800; text-align: center; line-height: 5mm; }

/* licence day */
.day { position: relative; padding-left: 4mm; }
.day::before { content: ''; position: absolute; left: 11.5mm; top: 8mm; bottom: 12mm; width: 0.8mm; background: var(--peach); }
.step { display: grid; grid-template-columns: 15mm 1fr 38mm; gap: 5mm; align-items: center; padding: 3.2mm 0; position: relative; }
.step .n { width: 15mm; height: 15mm; border-radius: 50%; background: var(--navy); color: #fff; font-size: 15pt; font-weight: 900; display: flex; align-items: center; justify-content: center; position: relative; z-index: 1; }
.step:last-child .n { background: var(--orange); }
.step .b { border: 0.3mm solid var(--line); border-radius: 3.5mm; padding: 4mm 5mm; }
.step:last-child .b { border-color: var(--orange); background: var(--cream); }
.step .b p { font-size: 9.6pt; color: var(--grey); margin-top: 0.8mm; }
.step .who { font-size: 8pt; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; color: var(--orange); }
.done-bar { margin-top: 5mm; background: var(--navy); color: #fff; border-radius: 4mm; padding: 5mm 7mm; display: flex; justify-content: space-between; align-items: center; font-size: 10pt; }
.done-bar b { font-size: 16pt; color: var(--orange); }

/* free zones */
.fzs { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; }
.fz { border: 0.3mm solid var(--line); border-radius: 4mm; padding: 4.5mm 5mm; display: flex; flex-direction: column; }
.fz.fast { border: 0.5mm solid var(--orange); }
.fz .hd { display: flex; justify-content: space-between; align-items: flex-start; }
.fz h3 { font-size: 21pt; font-weight: 900; color: var(--orange); line-height: 1; }
.fz .sp { font-size: 7.8pt; font-weight: 800; padding: 1.2mm 3mm; border-radius: 99px; background: var(--mist); color: var(--navy); white-space: nowrap; }
.fz.fast .sp { background: var(--orange); color: #fff; }
.fz .nm { font-size: 8.6pt; color: var(--grey); margin: 1.5mm 0 3.5mm; }
.fz .pr { font-size: 8.5pt; color: var(--grey); }
.fz .pr b { display: block; font-size: 18pt; color: var(--navy); font-weight: 900; letter-spacing: -0.01em; line-height: 1.1; }
.fz .pr b small { font-size: 9pt; font-weight: 700; color: var(--grey); }
.fz .vs { font-size: 8.6pt; color: var(--navy); background: var(--cream); border-radius: 2mm; padding: 1.8mm 3mm; margin: 2mm 0 2.5mm; font-weight: 600; }
.fz .best { font-size: 8.8pt; margin-bottom: 2mm; } .fz .best b { color: var(--navy); }
.fz ul { list-style: none; }
.fz li { font-size: 8.8pt; color: var(--grey); padding: 0.9mm 0 0.9mm 5mm; position: relative; }
.fz li::before { content: ''; position: absolute; left: 0; top: 2.4mm; width: 2.2mm; height: 2.2mm; border-radius: 50%; background: var(--orange); }

/* checklists */
.cl section { border: 0.3mm solid var(--line); border-radius: 4mm; padding: 5mm 6mm; margin-bottom: 5mm; }
.cl h3 { font-size: 11.5pt; margin-bottom: 2.5mm; padding-bottom: 2mm; border-bottom: 0.6mm solid var(--orange); }
.cl ul { list-style: none; }
.cl li, .tick li { font-size: 9.8pt; color: var(--grey); padding: 1.6mm 0 1.6mm 8mm; position: relative; list-style: none; }
.cl li::before, .tick li::before { content: ''; position: absolute; left: 0; top: 2mm; width: 4.2mm; height: 4.2mm; border: 0.45mm solid var(--navy); border-radius: 1mm; }

/* visa */
.vgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; }
.vstep { border: 0.3mm solid var(--line); border-radius: 4mm; padding: 4.5mm 5mm; display: grid; grid-template-columns: 9mm 1fr; gap: 3mm; }
.vstep .n { width: 9mm; height: 9mm; border-radius: 50%; background: var(--navy); color: #fff; font-weight: 900; text-align: center; line-height: 9mm; }
.vstep p { font-size: 9pt; color: var(--grey); margin: 0.8mm 0 1.5mm; }
.vstep .d { display: inline-block; font-size: 8pt; font-weight: 800; color: var(--orange); background: var(--cream); padding: 0.8mm 2.5mm; border-radius: 99px; }
.visa-photo { height: 58mm; border-radius: 4mm; background: url('assets/photos/flight.jpg') center 60%/cover; margin-bottom: 6mm; }
.tips { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; margin-top: 5mm; }
.tips div { background: var(--navy); color: #dfe6e8; border-radius: 4mm; padding: 5mm; font-size: 9.2pt; }
.tips b { color: var(--orange); display: block; font-size: 8pt; letter-spacing: .14em; text-transform: uppercase; margin-bottom: 1.5mm; }

/* bank */
.bank { display: grid; grid-template-columns: 1.1fr 1fr; gap: 6mm; }
.bank .img { border-radius: 4mm; background: url('assets/photos/handshake.jpg') center/cover; min-height: 100mm; }
.tick { border: 0.3mm solid var(--line); border-radius: 4mm; padding: 5mm 6mm; }
.tick h3 { margin-bottom: 2mm; }

/* tables */
table { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 9.6pt; }
th { text-align: left; background: var(--navy); color: #fff; padding: 3.2mm 4mm; font-weight: 700; }
th:first-child { border-radius: 3mm 0 0 0; } th:last-child { border-radius: 0 3mm 0 0; }
td { padding: 3.4mm 4mm; border-bottom: 0.3mm solid var(--line); vertical-align: top; color: var(--grey); }
td:first-child { font-weight: 700; color: var(--navy); width: 32%; }
tr:nth-child(even) td { background: var(--mist); }
.tax-img { height: 62mm; border-radius: 4mm; background: url('assets/photos/finance.jpg') center 40%/cover; margin-top: 6mm; }

/* faq */
.faq div { padding: 4.2mm 0; border-bottom: 0.3mm solid var(--line); }
.faq h3 { font-size: 11.5pt; margin-bottom: 1.2mm; }
.faq h3::before { content: 'Q. '; color: var(--orange); }
.faq p { font-size: 10pt; color: var(--grey); }
.disc { font-size: 7.8pt; color: #8a8a96; margin-top: 7mm; line-height: 1.5; }

/* back */
.back { background: var(--navy); color: #fff; padding: 0; }
.back .photo { height: 112mm; background: url('assets/photos/celebrate.jpg') center 30%/cover; position: relative; }
.back .photo::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(6,29,37,0) 40%, #061D25 100%); }
.back .inner { padding: 4mm 18mm 0; }
.back h2 { color: #fff; font-size: 34pt; font-weight: 900; }
.back .sub { color: #c6d1d4; font-size: 12pt; margin: 3mm 0 7mm; max-width: 165mm; }
.back .grid { display: grid; grid-template-columns: 1fr 46mm; gap: 8mm; align-items: start; }
.back ul { list-style: none; }
.back li { padding: 2.2mm 0; border-bottom: 0.3mm solid rgba(255,255,255,.12); font-size: 10.5pt; display: flex; gap: 4mm; }
.back li small { width: 24mm; color: var(--orange); font-weight: 800; font-size: 7.5pt; letter-spacing: .14em; text-transform: uppercase; padding-top: 0.8mm; }
.back .qr { background: #fff; border-radius: 4mm; padding: 4mm; text-align: center; color: var(--navy); font-size: 8pt; font-weight: 700; }
.back .qr svg { width: 38mm; height: 38mm; display: block; margin: 0 auto 2mm; }
.back .cta { display: inline-block; background: var(--orange); color: #fff; font-weight: 800; padding: 3.5mm 7mm; border-radius: 99px; font-size: 11pt; margin-top: 7mm; }
.back .logo { position: absolute; bottom: 12mm; left: 18mm; height: 10mm; }
.back .fine { position: absolute; bottom: 12mm; right: 18mm; font-size: 7pt; color: #7f9297; text-align: right; max-width: 110mm; }
"""

pages = []


def page(body, cls="", chip=None, footer=True):
    n = len(pages) + 1
    top = (f'<div class="top"><img src="assets/brand/Logo-Black.png" alt="Startup Zone"><span class="chip">{chip}</span></div>'
           if chip else "")
    foot = (f'<div class="foot"><span>Your UAE Licence in 1 Day · {CONTACT["web"]}</span><b>{n:02d}</b></div>'
            if footer else "")
    pages.append(f'<section class="page {cls}">{top}{body}{foot}</section>')


def ul(items, cls=""):
    return f'<ul class="{cls}">' + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"


page(f"""<div class="photo"></div><div class="shade"></div><div class="inner">
<img class="logo" src="assets/brand/Logo-white.png" alt="Startup Zone">
<span class="badge">For overseas investors</span>
<h1>Your UAE<br>licence in <span>1 day*</span></h1>
<p class="sub">The fast, simple guide to starting your company in a UAE free zone, from your first
call to your residence visa, without leaving home for the licence.</p>
<div class="stats"><div><b>1 day</b>licence issued*</div><div><b>~2 weeks</b>to your residence visa</div>
<div><b>100%</b>foreign ownership</div><div><b>1,000+</b>companies set up</div></div>
<div class="ed">*SHAMS and ANCFZ, for standard activities with complete documents. Terms on page 03. {EDITION} edition.</div>
</div>""", "cover", footer=False)

stages = "".join(f'<div class="stage s{i + 1}"><small>{e(a)}</small><h3>{e(b)}</h3><span class="t">{e(c)}</span><p>{e(d)}</p></div>'
                 for i, (a, b, c, d) in enumerate(STAGES))
page(f"""<div class="kicker">Your journey</div><h2>Three stages to <span>open for business</span></h2>
<p class="lead">Your licence is the fast part. The visa and bank account follow, and we run them side by side so
you're trading as quickly as possible.</p>
<div class="stages">{stages}</div>
<div class="photo-strip" style="background-image:url('assets/photos/burj-khalifa.jpg')"></div>
<div class="why"><div><b>0%</b>personal income tax</div><div><b>9%</b>Corporate Tax, 0% on the first AED 375,000</div>
<div><b>100%</b>ownership, no local partner</div><div><b>Online</b>licence setup from anywhere</div></div>""", chip="Overview")

needs = "".join(f'<div><i>{i + 1}</i><b>{e(a)}</b>{e(b)}</div>' for i, (a, b) in enumerate(ONE_DAY_NEEDS))
page(f"""<div class="kicker">The 1-day promise</div><h2>What makes <span>1 day</span> possible</h2>
<p class="lead">Free zones like SHAMS and ANCFZ run fully digital licensing. With three things in place, your
licence can be issued on the same working day we submit it.</p>
<div class="needs">{needs}</div>
<div class="terms"><h3>* Terms & conditions</h3><ol>{"".join(f"<li>{e(t)}</li>" for t in TERMS)}</ol></div>""", chip="Terms")

steps = "".join(f'<div class="step"><div class="n">{i + 1}</div><div class="b"><h3>{e(a)}</h3><p>{e(b)}</p></div>'
                f'<div class="who">{e(c)}</div></div>' for i, (a, b, c) in enumerate(LICENCE_DAY))
page(f"""<div class="kicker">Stage 1 · Licence</div><h2>Your licence day, <span>step by step</span></h2>
<p class="lead">Six steps, one working day, all online. Here's who does what.</p>
<div class="day">{steps}</div>
<div class="done-bar"><span>You're officially a UAE company owner.<br>Next: your establishment card and visa.</span><b>Day 1 ✓</b></div>""", chip="Stage 1")

fz = ""
for z in FREE_ZONES:
    fz += (f'<div class="fz {"fast" if z["fast"] else ""}"><div class="hd"><h3>{z["code"]}</h3><span class="sp">{e(z["speed"])}</span></div>'
           f'<div class="nm">{e(z["name"])} · {e(z["emirate"])}</div>'
           f'<div class="pr">Licence from<b>AED {z["price"]} <small>/ year</small></b></div>'
           f'<div class="vs">{e(z["visa"])}</div><div class="best"><b>Best for:</b> {e(z["best"])}</div>{ul(z["facts"])}</div>')
page(f"""<div class="kicker">Choose your free zone</div><h2>Four free zones, <span>one partner</span></h2>
<p class="lead">All four offer 100% foreign ownership and remote setup.</p>
<div class="fzs">{fz}</div>
<div class="note"><b>Prices as of {EDITION}</b>, subject to change. SHAMS, ANCFZ and IFZA include our service fee;
RAKEZ shows the RAKEZ package price, service fee quoted separately. Mainland or another free zone? Ask us.</div>""", chip="Free zones")

docs = "".join(f'<section><h3>{e(h)}</h3>{ul(items)}</section>' for h, items in DOCS)
page(f"""<div class="kicker">Get ready</div><h2>Your <span>document</span> checklist</h2>
<p class="lead">Have these ready before your licence day. Clear scans are the single biggest time saver.</p>
<div class="cl">{docs}</div>""", chip="Checklist")

vs = "".join(f'<div class="vstep"><div class="n">{i + 1}</div><div><h3>{e(a)}</h3><p>{e(b)}</p><span class="d">{e(c)}</span></div></div>'
             for i, (a, b, c) in enumerate(VISA_STEPS))
page(f"""<div class="kicker">Stage 2 · Visa</div><h2>Your residence visa <span>in about 2 weeks</span></h2>
<div class="visa-photo"></div>
<div class="vgrid">{vs}</div>
<div class="tips"><div><b>Plan your trip</b>You must be in the UAE for the medical test and Emirates ID biometrics.
Plan about a week here. We book your appointments around your flights.</div>
<div><b>Good to know</b>Health insurance is mandatory for every visa holder. If you have never entered the UAE before, a visit
visa may be needed first. Visa approval is at the discretion of UAE immigration.</div></div>""", chip="Stage 2")

page(f"""<div class="kicker">Stage 3 · Bank</div><h2>Open your <span>corporate bank account</span></h2>
<p class="lead">Banks approve businesses they understand. A complete, clear file is your fastest route to a yes.
Digital banks can open in days; traditional banks often take a few weeks.</p>
<div class="bank"><div class="tick"><h3>Bank readiness checklist</h3>{ul(BANK_LIST)}</div><div class="img"></div></div>
<div class="tips"><div><b>Pro tip</b>Write one page on who your customers are, and where money comes from and goes to.
It answers the bank's main questions before they ask.</div>
<div><b>We help</b>We introduce you to banks that suit your nationality, activity and trading countries,
including fast digital options like Wio and Mashreq Neo.</div></div>""", chip="Stage 3")

rows = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td></tr>" for a, b, c in COMPLIANCE)
page(f"""<div class="kicker">Stage 3 · Tax & compliance</div><h2>Stay <span>compliant</span> from day one</h2>
<p class="lead">The key dates every UAE company owner should know. Put them in your calendar now.</p>
<table><tr><th>What</th><th>When</th><th>Key point</th></tr>{rows}</table>
<div class="tax-img"></div>
<div class="note"><b>Let us handle it:</b> Startup Zone's accounting team takes care of bookkeeping, VAT and Corporate Tax
registrations and returns, and reminds you of every renewal.</div>""", chip="Compliance")

faq = "".join(f"<div><h3>{e(q)}</h3><p>{e(a)}</p></div>" for q, a in FAQ)
page(f"""<div class="kicker">FAQ</div><h2>Questions <span>investors ask us</span></h2><div class="faq">{faq}</div>
<p class="disc"><b>Important:</b> This guide is general information correct as of {EDITION}. It is not legal or tax advice.
Fees, processing times and requirements are set by the free zones and UAE authorities, change regularly and vary by
activity, nationality and bank. Licence and visa approvals are at the authorities' sole discretion. Photos: Unsplash.</p>""", chip="FAQ")

page(f"""<div class="photo"></div><div class="inner">
<h2>Start your licence <span style="color:var(--orange)">today.</span></h2>
<p class="sub">Send us your passport and business idea on WhatsApp. We'll confirm your activity, free zone and price,
and get your licence moving the same day.</p>
<div class="grid"><ul>
<li><small>WhatsApp</small>{CONTACT["phone"]}</li><li><small>Email</small>{CONTACT["email"]}</li>
<li><small>Website</small>{CONTACT["web"]}</li><li><small>Visit us</small>{CONTACT["address"]}</li></ul>
<div class="qr">{QR}Scan to chat on WhatsApp</div></div>
<span class="cta">Book your free consultation →</span></div>
<img class="logo" src="assets/brand/Logo-white.png" alt="Startup Zone">
<div class="fine">1,000+ companies set up · 5.0 on Google<br>© 2026 Startup Zone. General information only, not legal or tax advice.</div>""",
     "back", footer=False)

html = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Your UAE Licence in 1 Day | Startup Zone</title>'
        f'<style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
(HERE / "guide.html").write_text(html)
print(f"guide.html written: {len(pages)} pages")
