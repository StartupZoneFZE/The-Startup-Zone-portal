# WhatsApp lead follow-up sequence (draft)

Drafted 14 Nov 2026 for review. Nothing has been set up in Respond.io or sent to anyone.

## What this fixes

From the audit of Respond.io:

- The bot replies in 18 seconds, but a person takes 3.8 hours (median).
- 73% of leads get no chaser after going quiet.
- Only 19% are given a price.
- Staff only receive a chat once the AI marks it "Qualified".
- The top questions are price and extra costs, getting a visa, and documents.

## Rules for the sequence

1. **Price in the first message.** Every lead sees a real figure before being asked anything.
2. **A named person within 5 minutes** in working hours, whether or not the bot has finished qualifying.
3. **Seven touches over 14 days**, then one a month later. The sequence stops the moment the lead replies.
4. **WhatsApp's 24-hour rule.** You can send free-text messages only within 24 hours of the lead's last message. After that, WhatsApp only allows pre-approved template messages. Messages 5 to 8 below must be submitted in Respond.io as templates (category: Marketing) and approved by Meta before use. Each template send is charged by Meta.
5. **Respect "WhatsApp only, no calls".** If a lead says this, skip the call steps.
6. **Opt-out.** If a lead replies STOP, tag them and send nothing further.

## Prices used in this draft: please confirm

These come from your pricing page. Your current ad and one email quote AED 3,888 for the licence, and the bot used to quote "from AED 7,888". Pick one set and use it everywhere.

| Placeholder | Value used here | Source |
|---|---|---|
| `[LICENCE_PRICE]` | AED 4,888 | Pricing page, ANCFZ, no visa |
| `[VISA_PACKAGE_PRICE]` | AED 10,800 | Pricing page, ANCFZ, 1 visa, all-in year 1 |
| `[RENEWAL_PRICE]` | AED 4,888 | Email quote, year 2 renewal |
| `[AGENT_NAME]` | The adviser's first name | |
| `[NAME]` | The lead's first name | |

## The sequence

| # | When | Sent by | Type | Purpose |
|---|---|---|---|---|
| 1 | Instantly | Bot | Free text | Price and one question |
| 2 | Within 5 min (working hours) or 9:00 next working day | Person | Free text | Personal introduction, answer, next step |
| 3 | 2 hours after message 2, no reply | Automated | Free text | Light nudge |
| 4 | 20 to 22 hours after the lead's last message | Person | Free text | Written quote and document list before the window closes |
| - | Day 1 and day 3 | Person | Phone call | One call attempt each, unless "no calls" |
| 5 | Day 3 | Automated | Template | Answer the "extra costs" worry |
| 6 | Day 7 | Automated | Template | Instalments and proof |
| 7 | Day 14 | Automated | Template | Polite last message |
| 8 | Day 45 | Automated | Template | One re-open |

### Message 1: instant reply (bot)

> Hi [NAME], thanks for messaging Startup Zone.
>
> Quick answer on cost: a UAE business licence starts from [LICENCE_PRICE], and licence + 1 residence visa is from [VISA_PACKAGE_PRICE] for the first year. Our service fee is already included.
>
> So I can give you the exact figure, which do you need?
> 1. Licence only
> 2. Licence + visa
> 3. Not sure yet

Taglish version:

> Hi [NAME], salamat sa pag-message sa Startup Zone.
>
> Para sa presyo: ang UAE business licence ay nagsisimula sa [LICENCE_PRICE], at ang licence + 1 residence visa ay mula [VISA_PACKAGE_PRICE] para sa unang taon. Kasama na dito ang service fee namin.
>
> Para maibigay ko ang eksaktong presyo, alin po ang kailangan ninyo?
> 1. Licence lang
> 2. Licence + visa
> 3. Hindi pa sigurado

### Message 2: personal introduction (person, within 5 minutes)

> Hi [NAME], this is [AGENT_NAME] from Startup Zone. I'll be your adviser from here.
>
> Based on what you chose, your first-year total would be about [QUOTED_PRICE]. That covers the licence, [the visa,] and our fee. I'll confirm the exact amount once I know two things:
>
> 1. What will the business do?
> 2. Are you in the UAE now, and on what visa?
>
> You can answer here, or I can call you for 5 minutes. Which do you prefer?

Taglish version:

> Hi [NAME], si [AGENT_NAME] po ito ng Startup Zone. Ako na po ang adviser ninyo.
>
> Base sa pinili ninyo, ang total para sa unang taon ay humigit-kumulang [QUOTED_PRICE]. Kasama na ang licence, [visa,] at ang fee namin. Iko-confirm ko ang eksaktong halaga kapag nalaman ko ang dalawang bagay:
>
> 1. Ano po ang magiging negosyo?
> 2. Nasa UAE na po ba kayo ngayon, at anong visa?
>
> Pwede po kayong sumagot dito, o tatawagan ko kayo ng 5 minuto. Alin po ang mas gusto ninyo?

### Message 3: nudge (2 hours later, no reply)

> Hi [NAME], no rush. Whenever you have a minute, just send me what the business will do and I'll reply with your exact cost and the documents needed.

Taglish version:

> Hi [NAME], walang problema kung busy po kayo. Kapag may oras na, i-send lang po kung ano ang magiging negosyo at ibibigay ko ang eksaktong presyo at listahan ng documents.

### Message 4: written quote before the window closes (20 to 22 hours)

> Hi [NAME], so you have everything in one place:
>
> **Licence only:** from [LICENCE_PRICE] for year 1
> **Licence + 1 visa:** from [VISA_PACKAGE_PRICE] for year 1, all-in
> **Renewal from year 2:** from [RENEWAL_PRICE]
>
> To start we only need:
> - Passport copy
> - Passport photo
> - Current visa or entry stamp (if you are in the UAE)
> - 3 name options for the company
>
> Reply START and I'll send the application link. If the price is the concern, tell me your budget and I'll show you what fits.

### Message 5: day 3 template, "no hidden costs"

Template name: `followup_d3_total_cost`

> Hi {{1}}, this is {{2}} from Startup Zone. The question we hear most is "what are the extra costs?". Your quote already includes the licence and our service fee. The only other costs are government visa steps such as the medical test and Emirates ID, and I can list those for you in writing. Would you like the full breakdown?

Buttons: `Send breakdown` / `Not now`

### Message 6: day 7 template, instalments and proof

Template name: `followup_d7_instalments`

> Hi {{1}}, a quick note from Startup Zone. You can pay for your licence in instalments, so you don't need the full amount upfront. We have helped more than 1,000 business owners set up, with 200+ Google reviews. Shall I send you the instalment options?

Buttons: `Send options` / `Call me` / `Not now`

### Message 7: day 14 template, last message

Template name: `followup_d14_close`

> Hi {{1}}, I don't want to keep messaging if the timing isn't right, so this is my last note for now. Your quote stays valid until {{2}}. If you'd like to go ahead later, reply here any time and I'll pick it up straight away.

Buttons: `I'm still interested` / `Stop messages`

### Message 8: day 45 template, one re-open

Template name: `followup_d45_reopen`

> Hi {{1}}, {{2}} from Startup Zone here. Are you still planning to set up your UAE business this year? If yes, reply YES and I'll send today's price and the steps.

Buttons: `Yes` / `Stop messages`

## Quick replies for the common questions

Save these in Respond.io so advisers answer in seconds.

**"Can I get the visa without running a business?"**

> The visa comes through a real company licence that you own, so you will have a registered business with its own obligations: yearly renewal, and corporate tax registration and filing. I can explain exactly what that involves and what it costs each year, so you can decide if it suits you.

**"What documents do I need?"**

> Just four things to start: passport copy, passport photo, your current visa or entry stamp if you're in the UAE, and 3 name options for the company.

**"Can I pay in instalments?"**

> Yes. We can split the payment through Tabby or Tamara. Tell me which package you want and I'll send the instalment amounts.

**"Where are you located? Are you legitimate?"**

> We are an authorised free zone partner with 200+ Google reviews. Here is our office location and review page: [LINK]. You're welcome to visit or call before paying anything.

**"I'll decide later."**

> Of course. So I follow up at the right time, when are you hoping to have the licence: this month, in 1 to 3 months, or later?

## Rules to set up in Respond.io

- **Stop on reply:** any inbound message ends the sequence and assigns the chat to the adviser.
- **Assign immediately:** give every new chat a named adviser at message 1; do not wait for the AI to mark "Qualified".
- **Out of hours:** message 1 still goes instantly; message 2 goes at 9:00 the next working day.
- **Lifecycle stages:** New Lead at message 1, In Progress on first reply, Proposal Sent after message 4, Cold after message 7 with no reply.
- **Stop messages button:** tag as opted out and exclude from all templates.
- **Language:** if the lead writes in Tagalog or Taglish, use the Taglish versions and assign a Tagalog-speaking adviser.
- **Weekly check:** count of leads at each step, replies per message, and leads with no person assigned.

## Before going live

1. Confirm the three prices and the quote validity period.
2. Have a Tagalog-speaking team member check the Taglish wording.
3. Confirm the instalment offer and the "1,000+ clients, 200+ reviews" claims are current.
4. Submit the four templates for Meta approval, in English and Taglish.
5. Test the whole sequence on a staff phone number first.
