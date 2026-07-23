---
name: substack-drafter
description: >-
  Turn Panos's raw thoughts, notes, or voice-memo-style musings into a polished,
  Substack-ready essay — especially reflective "wisdom / things that matter"
  pieces on meaning, epistemology, building, AI, and how to live and work well.
  Use this whenever Panos shares loose thoughts, a rant, a paragraph of
  half-formed ideas, a journal entry, or says things like "draft this for
  Substack," "turn this into a post," "help me write about X," "clean this up
  for my newsletter," or "I've been thinking about..." and clearly wants it
  shaped into a publishable piece. Trigger even when he doesn't say the word
  "Substack" — if he's handing over reflective thoughts and the intent is to
  publish, this skill applies. Do NOT use it for code, docs, LinkedIn micro-posts,
  or emails.
---

# Substack Drafter

This skill turns Panos's raw thinking into an essay he'd be proud to publish on
Substack. The job is not to *replace* his voice with polished blandness — it's to
find the real idea buried in the notes and give it the clearest, most resonant
form it can have, in a voice that still sounds like him.

Panos is a builder (co-founder of Givelink), a first-principles thinker who reads
widely (Popper, Deutsch, Feynman, Hayek, Ostrom, Shannon), and who cares about
epistemology, meaning, and being genuinely useful in an AI world. His public
writing lives at the intersection of *what he's shipped* and *what it taught him
about how to think and live*. Keep that intersection in mind — it's what makes a
wisdom piece from him land rather than read like generic self-help.

## The prime directive: preserve the insight, don't sand it down

The most common way to ruin this kind of writing is to take a sharp, personal,
slightly-rough thought and buff it into smooth LinkedIn-speak that says nothing.
Do the opposite. The rough edges — the specific example, the contrarian take, the
honest admission, the odd metaphor — are usually the *best* part. Your job is to
keep the edge and remove only the friction: the rambling, the repetition, the
throat-clearing, the places where the idea hasn't found its words yet.

Before writing, find the **spine**: the one idea the piece is actually about. If
Panos's notes wander across three ideas, tell him — and either pick the strongest
for this piece or propose splitting them. A great essay says one true thing well.

## Defaults (override any of these when Panos says so)

- **Voice:** a blend — reflective and meaning-driven at the core, but grounded in
  concrete examples and crisp, load-bearing sentences. Depth without drifting into
  abstraction. When in doubt, get more concrete, not more profound.
- **Length:** let the idea decide its own size. Don't pad to hit a target and don't
  amputate a thought to stay short. Always report the word count and estimated read
  time (≈200 wpm) so he can gauge fit.
- **Furniture generated with every draft:** 2–3 title options, a subtitle/dek, a
  soft subscribe/reply close, and 1–2 flagged pull-quotes. (See "Output format.")

He can override any of these per-post: "make it punchy and short," "no CTA this
time," "keep it purely essayistic," etc. Honor those over the defaults.

## Process

1. **Read his input twice.** First for the idea, second for the phrases worth
   keeping. Lift his actual words and images wherever they're already good —
   don't paraphrase a vivid line into a duller one.
2. **Name the spine** in one sentence (internally, and in your note to him). If the
   input is too thin to carry a piece, say so and ask one or two sharpening
   questions rather than inventing filler to reach length.
3. **Find the shape.** Most of these pieces are one of: a *single-idea essay* (hook
   → develop → turn → land), a *list-with-a-thesis* (numbered lessons under one
   argument), or a *story-to-principle* (a concrete thing he built or lived →
   what it revealed). Pick the one the material wants.
4. **Write the draft** following the structure below.
5. **Stage the file** in the repo (see "Where drafts go") so it's version-controlled
   and syncs back to him. He then pastes the body into Substack and publishes.

## Structure of the essay

- **Opening hook (1–3 sentences).** Start in motion — a concrete scene, a sharp
  claim, a real question he was chewing on. Never open with "In today's world" or a
  dictionary definition. The first line should make the second line inevitable.
- **The turn.** Somewhere early, signal why this matters *now* or why the obvious
  view is incomplete. This is the promise that keeps someone reading.
- **The body.** Develop the one idea. Use his own examples — Givelink, The Crucible,
  Polymath, the ebook, things he's actually built or read. Concrete beats abstract
  every time. Prefer short paragraphs (Substack is read on phones); break with
  subheads only when the piece is long enough to earn them.
- **The landing.** End on something that resonates and resolves — a reframe, a
  small imperative, an image that closes the loop opened by the hook. Earn it;
  don't tack on a moral.

## Formatting for Substack

Substack's editor pastes Markdown cleanly. Use:

- `##` and `###` for section headers (skip `#` — the title is set separately).
- `**bold**` sparingly for genuine emphasis, `*italics*` for asides and titles.
- `>` blockquotes for quoted thinkers and for the pull-quotes.
- Plain `-` or `1.` lists.
- `[text](url)` links.

Avoid the two things Substack's paste handles badly: **tables** (convert to a list
or prose) and **footnotes** (inline them as parentheticals or "(see note)" lines,
and flag any you couldn't preserve). Keep raw HTML out.

## Images, buttons, and pull-quotes

Substack reading is mostly on phones, so visual rhythm matters. Add placement
markers directly in the body as HTML comments so Panos has a paste-and-fill
checklist (the comments won't render if pasted, and are easy to delete). Don't
overdo it: aim for roughly one image every 250–300 words.

- `<!-- [IMAGE · HEADER]: ... -->` right below the paste line. The header/cover
  image is set in Substack's own slot above the title, but note it here because it
  drives the email preview and social share. Describe a fitting visual.
- `<!-- [IMAGE · PRODUCT]: ... -->` wherever he references something he built. Push
  for a real screenshot over stock art, it earns clicks and justifies the mention.
- `<!-- [IMAGE · optional]: ... -->` for a mood beat between sections, marked
  skippable so he doesn't feel obligated.
- `<!-- [PULL-QUOTE]: <line> -->` at the spot where a flagged pull-quote line
  appears, so he can promote it to a styled block in place.
- `<!-- [BUTTON · primary]: Subscribe -->` at the very end, the "just finished, now
  act" spot. Never put a subscribe button at the top; it interrupts the hook.
- `<!-- [BUTTON · secondary]: <label> → <url> -->` for a product/CTA link inline
  with its paragraph, kept visually smaller than Subscribe so it doesn't compete
  with the primary goal (usually subscribers).

## Output format

Produce the staged file with this exact layout so it's consistent and scannable:

```
---
status: draft
created: <YYYY-MM-DD>
read_time: <N> min (~<word count> words)
---

# TITLE OPTIONS
1. <title A>
2. <title B>
3. <title C>

**Subtitle:** <one-line dek that earns the click without clickbait>

# PULL-QUOTES
> <line 1 worth pulling>
> <line 2 worth pulling>

---

<!-- PASTE EVERYTHING BELOW THIS LINE INTO SUBSTACK -->

<the essay body in clean Markdown, no H1 — the title goes in Substack's title field>

<soft close: an invitation to subscribe or reply, in his voice, only if CTA is on>
```

Then, in chat (not in the file), give him a 2–3 line editor's note: the spine you
found, anything you cut or flagged, and one honest suggestion for making it stronger.

## Where drafts go

Stage each piece as a Markdown file in the repo:

- Work in progress → `substack/drafts/<yyyy-mm-dd>-<slug>.md`
- Once he's published it → move to `substack/published/` and set `status: published`
  in the frontmatter.

Use a short, readable slug from the title (e.g. `2026-07-23-the-cost-of-being-useful.md`).
Committing the file is what gives him a version-controlled "upload" — the closest
thing to automation Substack allows, since it has no public publishing API.

## Voice guardrails

- **Never use dashes as punctuation.** This is a hard rule from Panos. No em dashes
  (—) and no en dashes (–) standing in for a pause, aside, or break. Use a comma, a
  colon, a period, or split into a short new paragraph instead. (Hyphens inside
  genuine compound words like "well-posed" or "first-principles" are fine, those
  aren't dashed pauses.) When you feel the urge to reach for a dash, that's usually
  a signal the sentence wants to become two.
- **Be honest, not preachy.** He's earned his views by building; let the writing
  show the work rather than lecture.
- **Cut the LinkedIn tics:** no "Here's the thing," no "Let that sink in," no
  manufactured suspense, no emoji-bulleted inspiration, no "game-changer."
- **One idea, well.** Resist cramming. If a second idea is fighting for space, note
  it as a possible next post.
- **Specific > grand.** "The North Star Pace Engine taught me that a metric you
  can't feel daily is a metric you'll drift from" beats "measurement is important."
- **Keep his fingerprints.** If he wrote a phrase that's a little weird and a little
  his, keep it. Personality is the point.
