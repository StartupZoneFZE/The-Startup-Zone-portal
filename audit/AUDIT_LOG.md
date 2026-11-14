# Startup Zone business audit: running log

Started 2026-11-14. All steps are read-only unless stated.

| # | Step | Result |
|---|------|--------|
| 1 | Mapped portal repo (95 files) | Next.js + Supabase client portal, early stage. Reading docs next. |
| 2 | Read portal status docs | Portal is internal staff tool, last updated Oct 2025, not deployed, auth not built. Live Supabase DB password and service-role key are committed in `SUPABASE_CREDENTIALS.md` and `PROJECT_STATUS.md` (security risk). |
| 3 | Launched website audit + competitor research (background) | Running. |
| 4 | Zoho Books totals | 2026 YTD: 1,074 invoices, AED 7,264,093.70 invoiced, AED 243,984.65 unpaid. Overdue (all dates): 93 invoices, AED 275,421.66 outstanding. |
| 5 | Zoho CRM deals | All-time: 7,703 Closed Lost in Sales pipeline vs ~57 Closed Won (many are TEST records or 2023-24 imports). Loss reasons all-time: Missed Follow Ups 5,673; Unqualified 1,592; Lack of response 438. All 7,703 lost deals were bulk-modified on 2 Nov 2026 18:22. Lead_Source blank on every 2026 deal. No deal created after 14 Jul 2026. |
| 6 | Zoho CRM leads | 173 open leads; 55 created since 15 Jul still "Not Contacted" (43 arrived in one batch 22 Sep). Website-form lead of 7 Nov still Not Contacted on 14 Nov. Only 3 leads created since 1 Oct. UTM / Ad_Name fields empty. Compliance_Trackers module: 0 records. Accounts: 5,429. |
| 7 | Meta Ads 2026 YTD | Main account (…5314): ~AED 34.5K across top 12 campaigns; ~1,339 form leads (AED 11-25 each) and ~2,440 WhatsApp conversations (AED 5-8 each). Only 1 campaign active ("3888_Lic Only_PH"). Second account (…1174): AED 726. Other accounts: zero spend. |
| 8 | Zoho Desk | Not readable: token lacks scope (SCOPE_MISMATCH). Respond.io connector not authorised. |
| 9 | Books YoY | Same period 2025: 623 invoices, AED 4,099,501.79. 2026 is +77% by value, +72% by invoice count. |
| 10 | Books overdue aging | 93 overdue invoices, AED 275,422 across 79 customers. >365 days: 56 invoices, AED 212,741. 31-90 days: 13, AED 32,728. 0-30 days: 8, AED 13,468. Reminders sent on overdue invoices: 0 of 93. Viewed by client: 0 of 93. Top 10 customers owe AED 158,908. |
| 11 | Books estimates (2 Oct-13 Nov 2026, latest 200) | 125 invoiced (AED 646,131); 75 still Draft (AED 657,465), of which 60 are older than 7 days (AED 552,645) and 38 older than 14 days. No estimate marked sent/accepted/declined. |
| 12 | Books items | First 200 catalogue items all have rate 0 (no standard price list). "Accounting & Bookkeeping Services" item: 2 invoices, AED 8,358 in 2026. "Vat Filing": 0. Line-item sampling delegated (running). |
| 13 | Gmail (ops mailbox) sent, last 30 days | 8 threads, 6 of them mailbox tests. Company mail moved to Zoho Mail on 27 Oct 2026, so client email is not visible from this connector. |
| 14 | Competitor research, round 1 | Done via search summaries (competitor sites are blocked from this environment). Covered Shuraa, Riz & Mona, Avyanco, Virtuzone, BCL. Owner then named: Virtuzone, Creative Zone, Avyanco, A&A, RAKEZ. Round 2 launched for the missing three. |
| 15 | Site defects spotted during competitor round | /pricing/ shows two different sets of figures per card; VAT page has "[Company Name]" placeholder and "The UAE Startup" name; /cost-calculator shows "Preview: form not connected yet."; footer address is Dubai, not Sharjah. To be confirmed by the website audit. |
| 16 | Gmail inbox (ops mailbox), last 21 days | ~200 threads, almost all automated free-zone notifications (SHAMS, Meydan, payment gateway). No client conversations here. Client email quality and reply times could NOT be audited: no Zoho Mail connector, Zoho Desk scope missing, Respond.io not authorised. |
| 17 | CRM client base (Accounts with a licence expiry date) | 612 accounts: 406 Active, 96 Expired (73 + 23 flagged "About to Expire" but company status Expired), 100 Cancelled, rest blank. |
| 18 | CRM renewals | 110 licences expire 14 Nov 2026-14 Feb 2027: 39 flagged "Due 30 days", 2 "Due 60 days", 62 still "Active", 7 blank. None marked "Renewal In Progress". Of 129 licences that expired in the past 12 months and were not moved forward: 74 Expired, 55 Cancelled. |
| 19 | CRM tax cross-sell data | Corporate tax: 194 accounts "Registered" + 6 "CT Reg Done"; 43 "Filing By Client"; 308 blank; CT return status filled on 1 account. VAT: 3 accounts where "Return filed by Us"; 496 blank. VAT_Filings and Corporate_Tax_Filings modules: 0 records each. Service_Requests: 178. |
| 20 | CRM account classification | 5,379 of 5,429 accounts have no Primary Service Line or Relationship Type. |
| 21 | CRM follow-up activity | Contacted_Date filled on 0 leads. Calls logged since 1 Aug: 14. Tasks since 1 Aug: 35 completed, 25 not started. 246 deals were created 15 Apr-14 Jul 2026, then deal creation stopped. |
| 22 | CRM upcoming renewals pricing | Agreed_Renewal_Price is empty on all 110 licences expiring in the next 3 months. Active licences by zone: ANCFZ 224, SRTIP 51, SHAMS 48, AFZ 29, Meydan 22, IFZA 12, RAKEZ 11, SPC 9. |
| 23 | Waiting on | Website audit, Books line-item sample, competitor round 2 (Creative Zone, A&A, RAKEZ). |
