"""Content for the Startup Zone 30-Day UAE Business Setup Guide.

Edit the text here, then run `python3 build.py && node render.js` to rebuild the PDF.
Facts reflect UAE rules as understood in November 2026 - review before each reprint.
"""

EDITION = "November 2026 Edition"

CONTACT = {
    "phone": "+971 52 346 9382",
    "whatsapp": "wa.me/971523469382",
    "email": "info@thestartupzone.ae",
    "web": "thestartupzone.ae",
    "address": "Latifa Tower, Suite 801, Sheikh Zayed Road, Dubai, UAE",
}

WEEKS = [
    {
        "num": 1,
        "name": "Plan",
        "headline": "Plan your UAE company",
        "photo": "planning",
        "intro": "This week you'll make the big decisions: what your company will do, "
                 "where it will be registered, who owns it and what it will cost. "
                 "Get these right and the rest of the month goes smoothly.",
        "outcomes": ["Business activities chosen", "Free zone selected",
                     "Trade name with two backups", "Clear year-1 budget and visa plan"],
    },
    {
        "num": 2,
        "name": "License",
        "headline": "Get your trade license",
        "photo": "office",
        "intro": "Now it becomes official. You'll submit your documents, sign your "
                 "company papers and get your trade license. You can do all of this from "
                 "your home country. No trip to the UAE needed yet.",
        "outcomes": ["Trade license and company documents", "Office or flexi-desk agreement",
                     "Establishment card (lets your company sponsor visas)", "UBO register filed"],
    },
    {
        "num": 3,
        "name": "Visas",
        "headline": "Become a UAE resident",
        "photo": "flight",
        "intro": "Time to visit the UAE. Your company sponsors your residence visa, giving "
                 "you an Emirates ID and the right to live, bank and do business here. "
                 "Plan to spend about a week in the country.",
        "outcomes": ["Entry permit and arrival in the UAE", "Medical test and Emirates ID",
                     "Residence visa issued", "UAE Pass set up"],
    },
    {
        "num": 4,
        "name": "Operate",
        "headline": "Open for business",
        "photo": "workspace",
        "intro": "The final week turns your company into a working business: a corporate "
                 "bank account, tax registrations, clean bookkeeping and a compliance "
                 "calendar, so nothing catches you out.",
        "outcomes": ["Corporate bank account application", "Corporate Tax registration",
                     "VAT decision made", "Bookkeeping and compliance calendar set up"],
    },
]

# Each day: title, goal, two actions (title + numbered steps), pro tip, documents.
DAYS = [
    # ---------------- WEEK 1: PLAN ----------------
    dict(day=1, week=1, title="Define your business idea",
         goal="Get clear on what you will sell, who you will sell to, and why the UAE.",
         a1=("Write your one-page business snapshot", [
             "Describe what you sell in one simple sentence.",
             "List your target customers: UAE, GCC or worldwide.",
             "Note where you will work from: inside the UAE or abroad.",
             "Write down your revenue goal for the first 12 months."]),
         a2=("Decide what you need from your company", [
             "Do you want to live in the UAE (residence visa)?",
             "Will you sell to UAE customers locally, or online and abroad?",
             "How many staff will you hire in year one?",
             "Do you need a shop, office or warehouse, or just a desk?"]),
         tip="Your answers decide everything else: activity, free zone, visas and office "
             "type. Send your snapshot to us on WhatsApp and we'll shortlist the best "
             "options for you in one call.",
         docs=["A notebook (or this guide!)", "Passport copy, keep it handy"]),

    dict(day=2, week=1, title="Choose your business activities",
         goal="Pick licensed activities that match exactly what your company will do.",
         a1=("Find your activities", [
             "List every service or product you plan to offer.",
             "Match each one to an official activity on the free zone's list.",
             "Check that your activities can be combined on one license.",
             "Shortlist your core activities, plus any you'll add within 2 years."]),
         a2=("Check for special approvals", [
             "Flag regulated areas: finance, health, education, food, legal, crypto.",
             "Ask whether an outside approval is needed (e.g. a ministry).",
             "Note any extra time and cost those approvals add."]),
         tip="Banks check that your payments match your licensed activities. Choose "
             "activities that clearly describe your real business. We search thousands of "
             "activities across free zones for you in minutes.",
         docs=["Business snapshot from Day 1", "Website or company profile (if any)"]),

    dict(day=3, week=1, title="Mainland or free zone?",
         goal="Choose the right type of company for how and where you'll trade.",
         a1=("Answer three key questions", [
             "Will most customers be shops, people or government bodies inside the UAE? Mainland may suit you.",
             "Will you serve clients worldwide, online or as a consultant? A free zone is usually simpler and cheaper.",
             "Do you need many visas or a large office? Compare both options."]),
         a2=("Use the comparison table", [
             "Read the Mainland vs Free Zone table at the front of this guide.",
             "Tick the column that matches more of your needs.",
             "Write down any questions for your consultant."]),
         tip="100% foreign ownership is available in free zones and for most mainland "
             "activities. For overseas founders running an international or online "
             "business, a free zone is usually the fastest, lowest-cost start.",
         docs=["Mainland vs Free Zone table (this guide)"]),

    dict(day=4, week=1, title="Pick your free zone",
         goal="Choose between SHAMS, IFZA, RAKEZ and ANCFZ with confidence.",
         a1=("Compare the four free zones", [
             "Read the free zone comparison at the front of this guide.",
             "Decide whether a Dubai address matters to your clients.",
             "Match the number of visas you need to each package.",
             "Choose your office type: flexi-desk, office or warehouse."]),
         a2=("Get two all-in quotes", [
             "Ask for a quote for your top two free zones.",
             "Compare year-1 and renewal costs, not just year 1.",
             "Check what's included: license, establishment card, visa, insurance."]),
         tip="Always compare the renewal cost. A cheap first year with an expensive "
             "renewal is not a bargain. Our quotes show both, with our service fee "
             "already included.",
         docs=["Activity shortlist (Day 2)", "Your visa needs (Day 1)"]),

    dict(day=5, week=1, title="Decide owners and structure",
         goal="Agree who owns the company, in what shares, and who manages it.",
         a1=("Set up ownership", [
             "One owner or several partners? This decides your company type.",
             "Agree share percentages in writing before you apply.",
             "Choose the manager/director and who will sign for the bank."]),
         a2=("Individual or company as shareholder?", [
             "Individual shareholder: passport-based and the simplest option.",
             "Corporate shareholder (your company abroad owns it): needs parent company documents.",
             "Parent company documents must usually be notarised and attested for the UAE. Allow extra weeks."]),
         tip="If speed matters, start with yourself as an individual shareholder. "
             "Company names like FZE, FZCO or FZ-LLC vary by free zone. We'll explain "
             "which one fits you.",
         docs=["Passports of all shareholders",
               "Corporate shareholder: incorporation certificate, MOA, board resolution (attested)"]),

    dict(day=6, week=1, title="Choose your trade name",
         goal="Pick a name that's approved first time, with two backups ready.",
         a1=("Brainstorm your names", [
             "Write three name options in order of preference.",
             "Check that the .ae domain and social media handles are free.",
             "Keep it easy to spell and pronounce in English."]),
         a2=("Check the naming rules", [
             "No offensive words or words against public morals or religion.",
             "No names of governments, famous brands or organisations without permission.",
             "Using a person's name usually means that person must be a shareholder.",
             "Add the legal ending (e.g. FZE or FZ-LLC). We confirm the right one."]),
         tip="Always submit three names at once. If your first choice is taken, your "
             "application keeps moving instead of losing a day.",
         docs=["Three name options", "Activity list (Day 2)"]),

    dict(day=7, week=1, title="Build your budget and visa plan",
         goal="Know your full year-1 cost and how many visas you need.",
         a1=("Plan your visas", [
             "Count yourself and partners who need residence visas.",
             "Add employees you plan to hire in year one.",
             "Note family members you may sponsor later.",
             "Choose a package with enough visa quota, plus room to grow."]),
         a2=("Build your budget", [
             "License and registration (your package price).",
             "Establishment card and visa costs per person.",
             "Health insurance for each visa holder.",
             "Bank minimum balance, bookkeeping and renewal savings."]),
         tip="Keep a 10–15% buffer for extras like courier, translation or document "
             "attestation. We give you a fixed price upfront, so there are no surprises.",
         docs=["Quotes from Day 4", "Visa plan"]),

    # ---------------- WEEK 2: LICENSE ----------------
    dict(day=8, week=2, title="Prepare your document pack",
         goal="Have clear, correct scans of every document ready to submit.",
         a1=("Scan your documents", [
             "Passport: colour scan, all corners visible, 6+ months validity.",
             "Passport-size photo with a white background.",
             "Proof of home address (utility bill or bank statement, last 3 months).",
             "UAE visa or entry stamp page, if you have one."]),
         a2=("Check the quality", [
             "Save as clear PDF or JPG. Not cropped, no glare.",
             "Name files clearly, e.g. Passport_JohnSmith.pdf.",
             "Check your name is spelled the same on every document."]),
         tip="Blurry scans are the number one cause of delays. Use a phone scanner app "
             "in daylight instead of a quick photo. It takes two minutes and saves days.",
         docs=["Passport", "Photo", "Proof of address", "CV (for some activities)"]),

    dict(day=9, week=2, title="Submit your application",
         goal="Send a complete application to your chosen free zone.",
         a1=("Complete the application", [
             "Confirm activities, name, shareholders and package.",
             "Review the application forms we prepare for you.",
             "Sign the declarations and compliance (KYC) forms."]),
         a2=("Verify your identity", [
             "Some free zones ask for a short video call or online ID check.",
             "Keep your original passport with you for the call.",
             "Answer any compliance questions quickly and fully."]),
         tip="Be clear and honest about your business model and where your funds come "
             "from. Complete answers keep your file moving; vague ones trigger more "
             "questions.",
         docs=["Document pack (Day 8)", "Signed application forms"]),

    dict(day=10, week=2, title="Receive your initial approval",
         goal="Get the free zone's initial approval and reserve your name.",
         a1=("Check your approval", [
             "The free zone reviews your activities, name and shareholders.",
             "You receive the initial approval and name reservation.",
             "Check every detail: name spelling, activities, shareholder names."]),
         a2=("Pay your fees", [
             "Review the invoice for license and registration fees.",
             "Pay by bank transfer or card.",
             "Save the payment receipt in your company folder."]),
         tip="Check every letter of your company name now. Fixing a spelling mistake after "
             "the license is issued means an amendment, which costs extra time and money.",
         docs=["Initial approval", "Payment receipt"]),

    dict(day=11, week=2, title="Sign your company documents",
         goal="Sign your Memorandum and Articles of Association (MOA/AOA).",
         a1=("Review before you sign", [
             "Check shareholders, share split, manager and activities.",
             "Check the share capital amount and whether it must be deposited.",
             "Ask us anything you're unsure about before signing."]),
         a2=("Sign and save", [
             "Sign electronically or in person, as the free zone requires.",
             "Make sure every shareholder signs.",
             "Save signed copies in your company folder."]),
         tip="The MOA is your company's rulebook, and banks will read it. Make sure the "
             "manager named in it is the person who will run the bank account.",
         docs=["MOA / AOA", "Shareholder resolutions", "Specimen signatures (if required)"]),

    dict(day=12, week=2, title="Choose your office space",
         goal="Pick the workspace your package and visa plan need.",
         a1=("Know your options", [
             "Flexi-desk: lowest cost, ideal for founders working remotely.",
             "Private office: needed for larger visa numbers in some free zones.",
             "Warehouse or industrial unit: for trading and manufacturing (a RAKEZ strength)."]),
         a2=("Confirm the details", [
             "Check the visa quota linked to your office type.",
             "Sign the lease or desk agreement in the company's name.",
             "Note your official address for invoices and the bank."]),
         tip="Start small. Most founders begin with a flexi-desk and upgrade when the team "
             "grows. There's no need to pay for empty desks in year one.",
         docs=["Lease or flexi-desk agreement"]),

    dict(day=13, week=2, title="Receive your trade license",
         goal="Get your license and company documents. You're officially in business!",
         a1=("Collect your documents", [
             "Trade license, certificate of incorporation, share certificate, MOA.",
             "Check every detail is correct.",
             "Save all PDFs in one 'Company Documents' folder."]),
         a2=("Put your license to work", [
             "Send copies to your accountant and to us.",
             "Add the license expiry date to your calendar.",
             "Add license details to your website and email signature."]),
         tip="Set a reminder 60 days before your license expires. Renewing on time avoids "
             "late fines and keeps your visas and bank account running smoothly.",
         docs=["Trade license", "Certificate of incorporation", "Share certificate", "MOA"]),

    dict(day=14, week=2, title="Get your establishment card",
         goal="Get the immigration card that lets your company sponsor visas.",
         a1=("Apply for the card", [
             "Submit the application with your license and manager's passport.",
             "Pay the establishment card fee.",
             "Receive the card (usually electronic)."]),
         a2=("Plan your visas", [
             "Confirm how many visas your company can sponsor.",
             "Decide who applies first (usually the investor or partner).",
             "Note the card's expiry date. It renews with your license."]),
         tip="No establishment card, no visas. It's quick but often forgotten. We apply "
             "for it right after your license is issued, so your visa can start straight away.",
         docs=["Trade license", "Manager's passport copy"]),

    dict(day=15, week=2, title="File your UBO register",
         goal="Declare your company's real owners and organise your records.",
         a1=("Complete your UBO filing", [
             "Identify the Ultimate Beneficial Owners: people who own or control 25%+.",
             "Complete the UBO, shareholder and director registers.",
             "Submit them to the free zone within its deadline."]),
         a2=("Organise company records", [
             "Create a folder for licenses, MOA, certificates and resolutions.",
             "Keep the registers of shareholders and directors up to date.",
             "Keep company records for at least 7 years."]),
         tip="UBO filing is mandatory and missing it can mean fines. Any change in "
             "ownership must be updated within 15 days. We prepare the forms for you.",
         docs=["UBO register", "Shareholder and director registers"]),

    # ---------------- WEEK 3: VISAS ----------------
    dict(day=16, week=3, title="Understand your visa journey",
         goal="Know which visa you need and the five steps to get it.",
         a1=("Know the visa types", [
             "Investor / partner visa: for shareholders of the company.",
             "Employment visa: for staff your company hires.",
             "Residence visas are typically valid for 2 years and renewable."]),
         a2=("Learn the five steps", [
             "Entry permit (issued before you travel).",
             "Enter the UAE, or change status if already here.",
             "Medical fitness test.",
             "Emirates ID biometrics.",
             "Residence visa issued, linked to your Emirates ID."]),
         tip="You must be in the UAE for the medical test and biometrics. Plan a trip of "
             "about a week, and we'll book your appointments so every day counts.",
         docs=["Passport (6+ months valid)", "Passport photo"]),

    dict(day=17, week=3, title="Apply for your entry permit",
         goal="Get the entry permit that lets you enter the UAE to become a resident.",
         a1=("Submit the application", [
             "We submit your passport, photo and establishment card.",
             "Pay the entry permit fee.",
             "Receive your e-entry permit, usually within a few working days."]),
         a2=("Plan your trip", [
             "Check the permit's validity. You must enter before it expires.",
             "Book flexible flights.",
             "Book a hotel close to your medical centre."]),
         tip="Don't book non-refundable flights until your entry permit is issued. Once "
             "it's in hand, book. We'll line up your medical appointment for your arrival.",
         docs=["Passport copy", "Photo", "Establishment card"]),

    dict(day=18, week=3, title="Travel to the UAE",
         goal="Arrive in the UAE on your entry permit, or change status here.",
         a1=("Arriving from abroad", [
             "Carry your printed entry permit and passport.",
             "Get your entry stamp at immigration.",
             "Send us a photo of your entry stamp page."]),
         a2=("Already in the UAE?", [
             "If you're here on a visit visa, we can change your status inside the country.",
             "Don't leave the UAE while the change of status is processing.",
             "Keep the change of status receipt safe."]),
         tip="Buy a UAE mobile SIM on arrival. You'll need a local number for UAE Pass, "
             "banking and government text updates.",
         docs=["Entry permit", "Passport"]),

    dict(day=19, week=3, title="Complete your medical test",
         goal="Pass the medical fitness test required for your residence visa.",
         a1=("Attend your appointment", [
             "We book your appointment at an approved medical centre.",
             "Bring your passport, entry permit and a photo.",
             "A quick blood test and chest X-ray. Usually under an hour."]),
         a2=("Get your results", [
             "Results usually arrive within 1–3 working days.",
             "They are sent electronically to the visa system.",
             "Keep your receipt until the visa is issued."]),
         tip="On a tight schedule? Choose an express or VIP medical service. It costs a "
             "little more but can save you days in the UAE.",
         docs=["Passport", "Entry permit", "Photo"]),

    dict(day=20, week=3, title="Emirates ID biometrics",
         goal="Give your fingerprints and photo for your Emirates ID.",
         a1=("Apply and attend", [
             "We submit your Emirates ID application.",
             "Attend your biometrics appointment, if one is required.",
             "Bring your original passport."]),
         a2=("Track and collect", [
             "Track your application through SMS updates.",
             "Your card is delivered by courier or collected.",
             "Add your digital ID in the UAE Pass app."]),
         tip="Set up UAE Pass as soon as your Emirates ID is ready. It's your digital "
             "identity for almost every government service, and lets you sign documents "
             "online.",
         docs=["Original passport", "Emirates ID application receipt"]),

    dict(day=21, week=3, title="Insurance and your residence visa",
         goal="Get health insurance and receive your UAE residence visa.",
         a1=("Arrange health insurance", [
             "Buy a policy that meets your emirate's requirements.",
             "Share the policy certificate with us.",
             "Add the renewal date to your calendar."]),
         a2=("Receive your visa", [
             "Your residence visa is issued digitally. No passport sticker.",
             "Download your e-visa copy.",
             "Check your name, passport number, sponsor and job title."]),
         tip="Congratulations, you're a UAE resident! Remember: most residence visas can "
             "be cancelled if you stay outside the UAE for more than 6 months in a row.",
         docs=["Insurance certificate", "E-visa", "Emirates ID"]),

    dict(day=22, week=3, title="Family and settling in",
         goal="Plan family sponsorship and sort out everyday life admin.",
         a1=("Plan family sponsorship", [
             "Check the minimum income needed to sponsor your family.",
             "Collect your marriage certificate and children's birth certificates.",
             "Attest these in your home country and in the UAE."]),
         a2=("Settle in", [
             "Rent a home with a registered tenancy contract (Ejari in Dubai).",
             "Open a personal bank account.",
             "Check if you can convert your driving licence directly."]),
         tip="Start attesting family documents early. It's often the slowest step, taking "
             "2–4 weeks from abroad. We can guide you through each stage.",
         docs=["Marriage certificate (attested)", "Birth certificates (attested)", "Tenancy contract"]),

    # ---------------- WEEK 4: OPERATE ----------------
    dict(day=23, week=4, title="Choose your bank",
         goal="Shortlist the banks that best fit your business profile.",
         a1=("Compare your options", [
             "Traditional banks: full service and branches, often higher minimum balances.",
             "Digital banks: fast online opening and lower fees, fewer services.",
             "Compare minimum balance, monthly fees, multi-currency and payment gateways."]),
         a2=("Find your best fit", [
             "Check which banks suit your nationality, activity and trading countries.",
             "Apply to the best-matched bank first.",
             "Consider a digital account for speed, plus a traditional bank for growth."]),
         tip="Bank choice depends on your profile: nationality, activity and where your "
             "money comes from. We introduce you to the banks most likely to say yes.",
         docs=["License pack", "Passport, visa and Emirates ID"]),

    dict(day=24, week=4, title="Prepare your bank KYC pack",
         goal="Build a complete, convincing file for the bank.",
         a1=("Company documents", [
             "Trade license, incorporation certificate, MOA, share certificate.",
             "Lease agreement and establishment card.",
             "A 1–2 page business plan with expected turnover."]),
         a2=("Personal documents", [
             "Passport, visa and Emirates ID of all shareholders and signatories.",
             "CV or profile showing your experience.",
             "Proof of source of funds and 6 months of personal bank statements.",
             "Contracts, invoices or letters of intent from clients or suppliers."]),
         tip="Banks approve businesses they understand. A one-page summary of who your "
             "customers are, and where money comes from and goes to, is the best thing you "
             "can add.",
         docs=["Bank readiness checklist (this guide)"]),

    dict(day=25, week=4, title="Open your bank account",
         goal="Complete your bank meeting and get your account opened.",
         a1=("Ace the meeting", [
             "Attend in person or by video, as the bank requires.",
             "Explain your business simply, with examples of first clients.",
             "Show your experience in this field."]),
         a2=("Follow up fast", [
             "Answer bank questions within 24 hours.",
             "Sign the account opening forms.",
             "Activate online banking and fund the account."]),
         tip="Corporate accounts can take 2–6 weeks. Start the moment you have your "
             "license and Emirates ID, and keep running the rest of your setup in parallel.",
         docs=["KYC pack (Day 24)"]),

    dict(day=26, week=4, title="Register for Corporate Tax",
         goal="Register your company for Corporate Tax and get your tax number.",
         a1=("Know the rules", [
             "Every UAE company, including free zone companies, must register.",
             "9% Corporate Tax on taxable profit above AED 375,000; 0% up to that.",
             "Qualifying Free Zone Persons can pay 0% on qualifying income (conditions apply)."]),
         a2=("Register on EmaraTax", [
             "Create an EmaraTax account on the Federal Tax Authority portal.",
             "Submit your license, MOA, and the manager's passport and Emirates ID.",
             "Receive your Corporate Tax registration number."]),
         tip="Register on time. The late registration penalty is AED 10,000. Our tax "
             "team handles your registration from start to finish.",
         docs=["Trade license", "MOA", "Owners' passports and Emirates IDs"]),

    dict(day=27, week=4, title="Decide on VAT",
         goal="Find out whether you must register for VAT, or should choose to.",
         a1=("Check the thresholds", [
             "Mandatory: taxable sales over AED 375,000 in the last 12 months, or expected in the next 30 days.",
             "Voluntary: sales or expenses over AED 187,500.",
             "The standard VAT rate is 5%."]),
         a2=("If you register", [
             "Register on EmaraTax and receive your Tax Registration Number (TRN).",
             "Show your TRN on every tax invoice.",
             "File VAT returns (usually quarterly) within 28 days of each period end."]),
         tip="Track your sales every month from day one. Registering late after crossing "
             "the threshold leads to penalties. We'll tell you exactly when you need to register.",
         docs=["Trade license", "Sales records or forecast", "Bank details"]),

    dict(day=28, week=4, title="Set up your bookkeeping",
         goal="Keep clean, accurate books from your very first transaction.",
         a1=("Set up your system", [
             "Choose cloud accounting software (e.g. Zoho Books).",
             "Connect your business bank feed.",
             "Set up your chart of accounts."]),
         a2=("Build good habits", [
             "Keep business and personal spending fully separate.",
             "Save every invoice and receipt digitally.",
             "Reconcile your bank account every month."]),
         tip="Free zone companies claiming 0% Corporate Tax need audited financial "
             "statements. Clean monthly books make your audit faster and cheaper.",
         docs=["Bank statements", "Sales invoices", "Purchase receipts"]),

    dict(day=29, week=4, title="Start trading the right way",
         goal="Get paid professionally and stay within the rules.",
         a1=("Set up invoicing", [
             "Create an invoice with your company name, license number and address.",
             "If VAT-registered, title it 'Tax Invoice' and show your TRN.",
             "Add payment terms and your company IBAN."]),
         a2=("Go live", [
             "Register your .ae domain and business email.",
             "Set up your Google Business Profile and LinkedIn page.",
             "Use written contracts with every client."]),
         tip="Only trade within your licensed activities, and always use your full legal "
             "company name on invoices and contracts. It protects you and keeps your bank happy.",
         docs=["Trade license", "Bank IBAN letter", "Your logo"]),

    dict(day=30, week=4, title="Lock in your compliance calendar",
         goal="Add every key date to your calendar so nothing is ever missed.",
         a1=("Add these dates", [
             "Trade license renewal (every year).",
             "Visa, Emirates ID and health insurance expiry dates.",
             "VAT returns and your Corporate Tax return (within 9 months of year end).",
             "UBO updates within 15 days of any ownership change."]),
         a2=("Celebrate and plan ahead", [
             "Tick off your 30-day progress tracker.",
             "Set your 90-day business goals.",
             "Book a quarterly review with your accountant."]),
         tip="Let us carry the calendar for you. Our compliance team sends reminders for "
             "renewals and tax deadlines, so you can focus on growing your business.",
         docs=["Compliance calendar (this guide)"]),
]

WHY_UAE = [
    ("0%", "Personal income tax", "Keep what you earn. There is no tax on salaries or personal income."),
    ("100%", "Foreign ownership", "Own your company outright, with no local partner needed in free zones."),
    ("9%", "Corporate Tax", "One of the world's most competitive rates, with 0% on the first AED 375,000 of profit."),
    ("8 hrs", "To two-thirds of the world", "A global hub connecting Europe, Asia and Africa."),
    ("Remote", "Setup", "Get your license without travelling. Visit only for your visa."),
    ("Family", "Residency", "Live in the UAE and sponsor your spouse and children."),
]

MAINLAND_VS_FZ = [
    ("Ownership", "100% foreign ownership for most activities", "100% foreign ownership"),
    ("Where you can trade", "Anywhere in the UAE, including government contracts",
     "Inside the free zone and internationally; UAE mainland trade usually via a distributor or extra permit"),
    ("Licensing authority", "Department of Economy of the emirate", "The free zone authority"),
    ("Office", "Physical office with registered lease usually required", "Flexi-desk options available"),
    ("Visas", "Linked to office size", "Linked to package and office type"),
    ("Corporate Tax", "9% above AED 375,000 profit", "0% on qualifying income for Qualifying Free Zone Persons; otherwise 9%"),
    ("Setup time", "Typically 1–3 weeks", "Often within a week"),
    ("Remote setup", "Possible for some steps", "Fully remote license in most free zones"),
    ("Best for", "Retail, restaurants, local services, government work",
     "Consulting, e-commerce, international trade, remote founders"),
]

FREE_ZONES = [
    dict(code="SHAMS", name="Sharjah Media City", emirate="Sharjah",
         best="Media, creative, consulting, e-commerce and budget-conscious founders",
         strengths=["Very competitive pricing", "Fully online setup", "Wide range of activities",
                    "Short drive from Dubai"],
         office="Flexi-desk to private office", vibe="Best value"),
    dict(code="IFZA", name="International Free Zone Authority", emirate="Dubai",
         best="Consultancy, trading, tech and professional services wanting a Dubai address",
         strengths=["Dubai address and prestige", "Fast, digital setup", "Flexible visa packages",
                    "Popular with banks and clients"],
         office="Flexi-desk to private office", vibe="Dubai address"),
    dict(code="RAKEZ", name="Ras Al Khaimah Economic Zone", emirate="Ras Al Khaimah",
         best="Manufacturing, industrial, trading and logistics businesses",
         strengths=["Warehouses, factories and land", "Free zone and non-free-zone licenses",
                    "Lower operating costs", "Strong industrial ecosystem"],
         office="Flexi-desk to warehouse and land", vibe="Industry & trade"),
    dict(code="ANCFZ", name="Ajman Nuventure Centre Free Zone", emirate="Ajman",
         best="Startups, freelancers, e-commerce and digital businesses",
         strengths=["Low-cost startup packages", "Modern, digital-first process",
                    "Startup-friendly community", "Close to Dubai and Sharjah"],
         office="Flexi-desk and shared workspace", vibe="Startup friendly"),
]

TIMELINE = [  # (step, min days, max days, week colour index) - typical working days
    ("Activity & name selection", 1, 2, 0),
    ("Initial approval", 1, 3, 1),
    ("Trade license issued", 2, 7, 1),
    ("Establishment card", 1, 5, 1),
    ("Entry permit", 3, 7, 2),
    ("Medical test results", 1, 3, 2),
    ("Emirates ID & residence visa", 5, 10, 2),
    ("Corporate Tax registration", 5, 20, 3),
    ("Corporate bank account", 10, 30, 3),
]

DOC_CHECKLIST = [
    ("For your license", [
        "Passport copy of every shareholder (6+ months valid)",
        "Passport-size photo (white background)",
        "Proof of home address (last 3 months)",
        "UAE visa or entry stamp page (if any)",
        "CV / profile (for some activities)",
        "Three trade name options",
        "Signed application and KYC forms",
    ]),
    ("Corporate shareholder (extra)", [
        "Certificate of incorporation (attested)",
        "Memorandum & Articles of the parent company (attested)",
        "Board resolution to set up the UAE company (attested)",
        "Register of shareholders and directors",
        "Passport of the authorised signatory",
    ]),
    ("For your visa", [
        "Original passport",
        "Digital passport photo",
        "Entry permit / change of status",
        "Medical fitness test",
        "Emirates ID biometrics",
        "Health insurance certificate",
    ]),
    ("Company documents you receive", [
        "Trade license",
        "Certificate of incorporation",
        "Memorandum / Articles of Association",
        "Share certificate",
        "Lease / flexi-desk agreement",
        "Establishment card",
        "UBO register",
    ]),
]

BANK_CHECKLIST = [
    ("Company", [
        "Trade license and certificate of incorporation",
        "MOA / AOA and share certificate",
        "Lease or flexi-desk agreement",
        "Establishment card",
        "Board resolution naming the account signatory",
    ]),
    ("Shareholders & signatories", [
        "Passport, residence visa and Emirates ID",
        "CV / LinkedIn profile showing relevant experience",
        "Proof of residential address",
        "Personal bank statements (6 months)",
    ]),
    ("Your business story", [
        "1–2 page business plan",
        "Expected monthly turnover and transaction volume",
        "Main countries you'll send money to and receive it from",
        "Key clients and suppliers (names, countries)",
        "Contracts, invoices or letters of intent",
        "Proof of source of funds / initial capital",
        "Company website and email on your own domain",
    ]),
]

COMPLIANCE = [
    ("Trade license renewal", "Every 12 months", "Start 30–60 days before expiry"),
    ("Establishment card", "Renews with your license", "Needed to keep sponsoring visas"),
    ("Residence visa & Emirates ID", "Typically every 2 years", "Avoid more than 6 months in a row outside the UAE"),
    ("Health insurance", "Every 12 months", "Must stay active for every visa holder"),
    ("Office / flexi-desk lease", "Every 12 months", "Usually renewed with the license"),
    ("VAT return", "Usually quarterly", "Due within 28 days after each tax period"),
    ("Corporate Tax return", "Once a year", "Due within 9 months of financial year end"),
    ("Audited financial statements", "Once a year", "Required for Qualifying Free Zone Persons; many free zones require them too"),
    ("UBO register update", "When ownership changes", "Update within 15 days of any change"),
    ("Bookkeeping & bank reconciliation", "Every month", "Keep records for at least 7 years"),
]

GLOSSARY = [
    ("AOA / MOA", "Articles / Memorandum of Association: your company's founding rulebook."),
    ("Corporate Tax (CT)", "UAE tax on business profits: 9% above AED 375,000."),
    ("Emirates ID", "Your UAE identity card, issued to every resident."),
    ("EmaraTax", "The Federal Tax Authority's online portal for VAT and Corporate Tax."),
    ("Ejari", "Dubai's official system for registering tenancy contracts."),
    ("Entry permit", "Permission to enter the UAE to complete your residence visa."),
    ("Establishment card", "Immigration file that lets your company sponsor visas."),
    ("FTA", "Federal Tax Authority, which runs VAT and Corporate Tax."),
    ("FZE / FZCO / FZ-LLC", "Free zone company types. Names vary by free zone."),
    ("Flexi-desk", "Shared desk space that meets free zone office requirements."),
    ("Initial approval", "First green light from the authority for your name and activities."),
    ("KYC", "'Know Your Customer': identity and background checks."),
    ("Mainland", "Companies licensed by an emirate's Department of Economy."),
    ("QFZP", "Qualifying Free Zone Person: can pay 0% CT on qualifying income."),
    ("Share capital", "The value of shares stated in your MOA."),
    ("TRN", "Tax Registration Number, shown on tax invoices."),
    ("UAE Pass", "The national digital ID app for government services."),
    ("UBO", "Ultimate Beneficial Owner: a person owning or controlling 25%+."),
    ("VAT", "Value Added Tax, charged at 5% in the UAE."),
]

FAQ = [
    ("Do I need to be in the UAE to set up my company?",
     "No. Your license can be issued fully remotely. You only need to visit for your visa "
     "medical test and Emirates ID, and often for your bank meeting."),
    ("Can I own 100% of my company?",
     "Yes. Free zone companies are 100% foreign-owned, and so are most mainland activities."),
    ("How long does it take?",
     "A free zone license is often ready within a week. With your visa, plan for about "
     "3–4 weeks. Bank accounts vary and can take 2–6 weeks."),
    ("Do I have to deposit share capital?",
     "In most free zones you don't need to deposit it upfront, but rules vary. We'll confirm for your free zone."),
    ("Can I keep living abroad?",
     "Yes, but to keep your residence visa you should generally not stay outside the UAE "
     "for more than 6 months in a row."),
    ("Will I pay tax?",
     "There's no personal income tax. Your company may pay 9% Corporate Tax on profit above "
     "AED 375,000, or 0% on qualifying free zone income. VAT is 5% once registered."),
]
