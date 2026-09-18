# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

I picked city_guides as my corpus. It answers general questions like where to stay, eat, see, etc... for the towns, but not very specific questions like is there a pizza restaurant?

## Chunking Strategy

**Chunk size:**
**Overlap:**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

My strategy is to just chunk each subsection using pattern matching for the subsection title.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

======================================================================
Chunk 2  |  source: guide_corry_vale.md#6  |  produced by: chunker.py::split_documents
======================================================================
## When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.

======================================================================
Chunk 3  |  source: guide_givens_mill.md#3  |  produced by: chunker.py::split_documents
======================================================================
## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.

======================================================================
Chunk 4  |  source: guide_kestrelford.md#6  |  produced by: chunker.py::split_documents
======================================================================
## When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.

======================================================================
Chunk 5  |  source: guide_regional_transport.md#1  |  produced by: chunker.py::split_documents
======================================================================
## The railway

The line runs along the river valley, connecting Brightwater to the regional
hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line
north of Brightwater closed in 1963 and everything beyond it is bus or car.

Tickets are cheaper booked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**

Using the guides_accessibility.md, which town is the easiest for walking?

**Answer:**

According to `guide_accessibility.md`, Thornby Wells is described as the easiest town in the region because it is flat, compact, and everything is within a three-minute walk of everything else.

Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_elder_ness.md, guide_halden_bay.md, guide_kestrelford.md

Note: When I ask just "Which town is the easiest for walking?", I actually got "Based on the provided documents, there is not enough information to determine which town is the *easiest* for walking." After grounding the question with a specific guide, it correctly
answers the question. Grounded question best distance: 0.518, cutoff: 0.6.

**My relevance cutoff:**

Cutoff: 0.6

In-scope question ranges from 0.338 to 0.487, out-of-scope ranges from 0.754 to 0.899.
We would want the range to be between 0.487 and 0.754 based on the 10 questions.
Mid-point is 0.62, so I think the default 0.6 is good for city_guide corpus
because five question is still a small sample size, I don't want to lower the cutoff
and potentially reduce its accuracy.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
| Which town is the easiest for walking? | yes | 0.487 |
| When do the restaurants close? | yes | 0.338 |
| Which town's market has been running the longest? | yes | 0.446 |
| How many tram lines does Marchwood have? | yes | 0.392 |
| What to see at Givens Mills? | yes | 0.437 |
| What is the capital of Mongolia? | no | 0.754 |
| How do I change the oil in a diesel engine? | no | 0.892 |
| Who won the 1994 World Cup? | no | 0.899 |
| What is the recommended dosage of ibuprofen for a headache? | no | 0.846 |
| How do I write a for loop in Rust? | no | 0.813 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I asked GPT-5.6 Luna to write my chunking function:
"replacement split_documents() with a new chunking strategry that chunks each subsection of texts for my corpus documents.

Example:
"## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings."

should be 1 chunk."

After the AI generated the chunking function, I asked it to explain each part of the code because I'm still new to Python syntax.

**2.**
The other 2 times I used AI is for the Talk this through section for Milestone 3 and 4:
Note: I used VS Code AI chat, and it autorouted to GPT-5.6 Luna.

Milestone 3:
Q: Here are five chunks from my documents. For each one, tell me what question it could answer on its own. If it can't answer anything on its own, say so and tell me what's missing. (pasted the long answer I got from the running python app.py chunks.)

A:
Chunk 1: It cannot answer a useful question on its own. It only says the region may be difficult for people with limited mobility. It is missing specific accessibility information about roads, paths, buildings, and transport.
Chunk 2: When is the best time to visit Corry Vale, and what seasonal problems should visitors expect?
Chunk 3: Where can visitors eat and drink at Givens Mill, and when are those places open?
Chunk 4: When is the best time to visit Kestrelford, and what seasonal travel difficulties should visitors expect?
Chunk 5: How can visitors travel by train from Brightwater, and what should they know about schedules, tickets, and onward transport?

My thought: Based on the chunks and the AI's answer. My chunking strategy should work correctly for city_guide corpus.

Milestone 4:
Not including the 
Q: Here are the best distances for five questions my documents cover, and five they don't. Where would you put the cutoff, and what would I get wrong at that number? (pasted the best distance list)

A:
I’d set the cutoff at 0.6. Lower distances are more relevant, and this sits comfortably between the closest in-corpus result (0.487) and the closest out-of-corpus result (0.754).

At 0.6, these ten examples would all be classified correctly:

5/5 in-corpus questions accepted
5/5 out-of-corpus questions rejected
0 false positives
0 false negatives
The main risk is that this is a small sample. A covered question with a distance above 0.6 would be incorrectly rejected, while an unrelated question unusually close to the corpus could still be accepted.

My thought: I also picked 0.6 cutoff before asking AI this question, it's good that AI confirms my 0.6 cutoff is a good and reasonable cutoff.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
