# SOQ & Professional Writing Guide

A reference for writing Statements of Qualifications (SOQs) and other professional writing in my voice — clear, professional, and human, not AI-sounding. Use this whenever drafting anything I'll submit under my name.

## The core idea

The thing that makes writing "scream AI" isn't bad grammar — it's writing that's too smooth, vague, and padded. Good professional writing reads as a specific, competent person who did specific things. The fix is almost always **specificity**: real numbers, real tools, the actual situation, what I actually did, and how it turned out. AI can't invent my specifics — only I have them. So the process is: I supply the raw facts, Claude shapes them into plain, professional prose.

## My target voice

- **Plain and direct.** Short, clear sentences. Say the thing.
- **Concrete over abstract.** "I automated our nightly backups with a Bash script on a cron job" beats "I leveraged automation to improve operational efficiency."
- **Professional, not stiff.** Clear and competent — not corporate buzzword soup, not casual either. No "leverage," "synergy," "passionate about," "in today's fast-paced world."
- **Confident, not boastful.** State what I did and the result. Let the facts carry it; don't oversell with adjectives.
- **First person, active voice.** "I built," "I led," "I fixed" — not "responsibilities included" or passive constructions.
- **Use contractions by default.** Write "can't," "wasn't," "didn't," "haven't," "shouldn't," "I'm" — not "cannot," "was not," "did not," "have not," "should not," "I am." That's how I actually write. Only use the spelled-out form when I deliberately want to emphasize the negation.

## The anti-AI checklist

Before any SOQ or professional draft is final, check it against these. These are the tells that make writing read as machine-generated:

- **Em-dash overload.** AI loves em-dashes. Use them sparingly; prefer periods.
- **No mid-sentence colons.** Never use a colon mid-sentence before a single explanatory word, clause, or example. A colon may ONLY introduce a real list or a short inline series. If you are about to write "X: Y" where Y explains or expands X, rewrite with a period or comma. Example of the violation: "I administer Active Directory directly: creating users and groups." Fix: "I administer Active Directory directly. I create users and groups." This is a zero-tolerance rule and applies to everything written under my name, including chat. Scan every colon before calling a draft done.
- **Rule-of-three everywhere.** Constant "X, Y, and Z" triads and symmetrical sentence structures. Vary the rhythm. Real writing is lumpy.
- **Hollow buzzwords.** "Leverage," "utilize," "robust," "seamless," "passionate," "dynamic," "impactful," "drive results," "spearhead." Cut them or replace with the plain word ("use," "strong," "led").
- **Throat-clearing openers.** "In today's fast-paced world," "In an era of," "As a dedicated professional." Delete and start with the substance.
- **Vague value claims.** "I bring a proven track record of excellence." Says nothing. Replace with the actual track record: what, how much, when.
- **Over-hedging.** "I believe I would potentially be able to contribute." Just say "I can do X."
- **Too-perfect symmetry.** Every paragraph the same length, every sentence the same shape. Break it up.
- **Restating the prompt _inside the answer_.** Don't echo the question back as throat-clearing in the body of the answer. Just answer it. (This is about the answer prose only. The numbered **heading** above each answer is a separate thing and MUST be the full verbatim question — see Formatting requirements below.)
- **Empty conclusions.** "In conclusion, I am confident I would be a valuable asset." Cut. End on a concrete point.

If a sentence could appear in anyone's application for any job, it's too generic — make it specific to me or cut it.

## Formatting requirements (non-negotiable)

- **Restate each full question verbatim as the heading.** Every answer is headed by the complete, word-for-word question from the posting, numbered in order, then the answer below it. Do not paraphrase or shorten the question into a topic label. Pull the exact text from the posting's SOQ instructions.
- **Follow the posting's stated SOQ format exactly.** Page limit, font, font size, spacing, and numbering as the posting specifies. Failing the format can disqualify the application, so check the posting every time and verify the built PDF against it (page count especially) before calling it done.
- **Font size applies to EVERY character — title and header included.** If the posting says "12-point font," then the title ("Statement of Qualifications"), the name/JC/position line, the question headings, and the body are ALL exactly 12-point. No larger title, no smaller header line. After building, verify the docx contains only the one required size (no stray larger/smaller runs) before calling it done. Do the same for the required font family — one font everywhere, no exceptions.
- **Header.** Name and contact at the top, titled "Statement of Qualifications," per the posting's instructions.

## How a strong SOQ is built (the STAR backbone)

Most CA state SOQ prompts are really asking for a story with evidence. The reliable structure:

- **Situation** — the context, briefly. What was going on.
- **Task** — what needed to happen, and why it mattered.
- **Action** — what *I* specifically did. This is the heart; be concrete about tools, decisions, and steps.
- **Result** — how it turned out, with numbers or a clear outcome where possible.

Lead with a direct answer to the prompt, then support it with one or two real examples in this shape. Tie it back to the qualification the prompt is asking about.

## The process when writing a real SOQ

1. Paste the actual SOQ prompt(s) and any word/page limit.
2. Claude pulls the real specifics from PRIMARY SOURCES first — my GitHub repos (github.com/umraffer32, fetch a README via the /blob/main/README.md URL), the submitted SOQs in the JC-* folders, Employment_History_STD678.md, and MEMORIES — then asks me targeted questions only for what those don't cover. Working from summary memory alone produces a generic draft. The named control IDs, numbers, and tool details that make a draft specific live in the source material, not in a paraphrase.
3. Claude drafts in the voice above, structured with STAR where it fits.
4. Before showing me the draft, Claude runs an adversarial self-audit on it. Claude scores it against the posting's rubric the way a screener would, checks every claim against the source material for accuracy, flags any prompt it answers weakly, and runs the anti-AI checklist. Claude does this BY DEFAULT, not only when I ask. (Lesson from JC-521525, where the first draft was honest but generic until I pushed for the self-audit.)
5. We iterate on word count and emphasis until it sounds like me.

## My background to draw from

Infrastructure/DevOps and automation. Day-to-day: Bash and Python scripting, AWS, Terraform/IaC, Linux and Windows, Git/GitHub. Strengths to surface in SOQs where relevant: automating manual/repetitive work, debugging and root-causing failures, infrastructure provisioning, and cleaning up or refactoring existing systems. (Keep this updated as my experience grows — see [[about-me]].)

## Quick reminder

I don't need to be a good writer to produce a strong SOQ. I need to bring the real specifics; Claude turns them into clear, professional, human-sounding prose and strips anything that smells like AI.
