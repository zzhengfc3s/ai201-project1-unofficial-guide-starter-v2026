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

**Chunk 1** — source: guide_accessibility.md#0 `` — produced by: chunker.py::split_documents ``
```
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.
```

**Chunk 2** - source: guide_corry_vale.md#6 `` — produced by: chunker.py::split_documents ``
```
## When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.
```

**Chunk 3** - source: guide_givens_mill.md#3 `` — produced by: chunker.py::split_documents ``
```
## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.
```

**Chunk 4** - source: guide_kestrelford.md#6 `` — produced by: chunker.py::split_documents ``
```
## When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.
```

**Chunk 5** - source: guide_regional_transport.md#1 `` — produced by: chunker.py::split_documents ``
```
## The railway

The line runs along the river valley, connecting Brightwater to the regional
hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line
north of Brightwater closed in 1963 and everything beyond it is bus or car.

Tickets are cheaper booked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.
```

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
|---|---|---|
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
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. The sampled chunks contains the entire subsection of text, with no single chunk containing content from more than one city or topic.| 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Every answer the system produces accurate information for the requested city without mixing up information from other or surrounding city.| 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
# Run log — before

Criterion 1.
Question 1: Which town is the easiest for walking? — run 1
- Produced by: `app.py::main`

(best distance 0.487, cutoff 0.6)

======================================================================
System instruction sent with the prompt
======================================================================
You answer questions using only the documents provided to you.

Rules:
- Use only the information in the documents below. Do not use anything you know from elsewhere.
- If the documents don't cover the question, say you don't have enough information. Do not guess.
- Name the document your answer came from, using the filename given in each excerpt.
- Be brief. Two or three sentences is usually enough.

======================================================================
The assembled prompt, exactly as sent
======================================================================
Documents:

[from guide_corry_vale.md]
## Getting around

Nothing within the valley is walkable from anything else — the villages are two to four miles apart. There is one taxi, based in the largest village, and it must be booked a day ahead. Most visitors drive between villages and walk the footpaths in between.

[from guide_halden_bay.md]
## Getting there

The coast road is the only approach and it is slow — 40 minutes for 22 miles, with the last stretch cut into the cliff. Buses run four times a day. Parking in the town itself is limited to two small lots that fill by 10am on summer weekends; the overflow lot is a 12-minute walk up a hill.

[from guide_walking.md]
# Walking in the region

[from guide_brightwater.md]
## Getting around

The town is walkable end to end in about 35 minutes. The local bus runs two routes on a 30-minute headway until 7pm and stops entirely on Sundays. Cycling is easy along the river path and unpleasant on Mill Road, which has no shoulder. Taxis exist but must be phoned; they do not circulate looking for fares.

[from guide_elder_ness.md]
## Getting around

On foot. The village is one street. The lighthouse is a 25-minute walk along the shingle, which is harder going than the distance suggests. There is one car park at the village and parking anywhere else on the headland is prohibited and enforced.

---

Question: Which town is the easiest for walking?

Answer using only the documents above, and name the file you used.
======================================================================

Based on the provided documents, there is not enough information to determine which town is the *easiest* for walking.

Sources retrieved: guide_brightwater.md, guide_corry_vale.md, guide_elder_ness.md, guide_halden_bay.md, guide_walking.md

0 model calls this session, 1 served from cache

Criterion 2:
Question 3: Which town's market has been running the longest? — run 3
- Produced by: `run_eval.py::main`

- Best distance: 0.4465 (passed the gate)
- Sources retrieved: guide_eating.md, guide_kestrelford.md, guide_thornby_wells.md

```
Kestrelford's market has been running the longest, as it has operated since the 1400s (whereas Marchwood's covered market has operated since 1863). 

Source: `guide_eating.md` and `guide_kestrelford.md`
```

Criterion 3:
Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.754 | refused |
| How do I change the oil in a diesel engine? | 0.892 | refused |
| Who won the 1994 World Cup? | 0.899 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.846 | refused |
| How do I write a for loop in Rust? | 0.813 | refused |

Criterion 4:
Question 2: When do the restaurants close? — run 2
- Produced by: `app.py::main`
(best distance 0.338, cutoff 0.6)

======================================================================
System instruction sent with the prompt
======================================================================
You answer questions using only the documents provided to you.

Rules:
- Use only the information in the documents below. Do not use anything you know from elsewhere.
- If the documents don't cover the question, say you don't have enough information. Do not guess.
- Name the document your answer came from, using the filename given in each excerpt.
- Be brief. Two or three sentences is usually enough.

======================================================================
The assembled prompt, exactly as sent
======================================================================
Documents:

[from guide_elder_ness.md]
## Eat and drink

One pub, serving food 12 to 2 and 6 to 8, closed Mondays. A shop that sells basics and closes at 5pm and all day Sunday. That is the complete list. Visitors staying more than a night bring food with them.

[from guide_halden_bay.md]
## Eat and drink

Seafood, unsurprisingly, and it is genuinely fresh — the boats land in the early morning and the two harbour restaurants buy directly. Prices on the harbour front are roughly double those on Fell Street, one level up, for comparable food. Everything closes by 9pm and much of it closes entirely from November to February.

[from guide_kestrelford.md]
## Eat and drink

Four pubs, two cafés, and a bakery that sells out by 11am. The pubs serve food between 12 and 2 and again between 6 and 8:30, and outside those windows there is nowhere to eat at all. The bakery is the reason most people come back.

[from guide_eating.md]
## Opening hours

This catches visitors out more than anything else. Outside Marchwood, kitchens
across the region stop serving at 9pm and often earlier. Kestrelford's pubs
serve 12 to 2 and 6 to 8:30 and there is nowhere to eat at all outside those
windows. Elder Ness has one pub, closed Mondays.

Sunday evening is the hardest meal to find anywhere except Marchwood and
Thornby Wells.

[from guide_brightwater.md]
## Eat and drink

The riverside strip has six or seven places aimed squarely at visitors and priced accordingly. Two streets back, on Corry Lane, the same food costs about a third less. The Tuesday market sets up in the square from 7am and is finished by 1pm. Most kitchens in town stop serving at 9pm, earlier than visitors expect, and on Sundays many close entirely.

---

Question: When do the restaurants close?

Answer using only the documents above, and name the file you used.
======================================================================

Based on the provided documents:

* In Halden Bay, everything closes by 9pm, and much of it closes entirely from November to February (`guide_halden_bay.md`).
* Across the region (outside Marchwood), kitchens stop serving at 9pm and often earlier (`guide_eating.md`). 
* In Brightwater, most kitchens stop serving at 9pm, and on Sundays many close entirely (`guide_brightwater.md`).

Sources retrieved: guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_halden_bay.md, guide_kestrelford.md

0 model calls this session, 1 served from cache

Criterion 5:
Question 4: How many tram lines does Marchwood have? — run 2
- Produced by: `run_eval.py::main`

- Best distance: 0.3920 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_marchwood.md, guide_thornby_wells.md

```
Marchwood has four tram lines. 

Source: `guide_marchwood.md` and `guide_accessibility.md`
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MISS | Even though we hit the target 4 of 5, it failed to correctly answer Question 1 for all 3 runs. I think is this a miss, and the target should be stricter at 5 of 5. Question 1 ended up being a good edge case question for my corpus. I was not expecting it to fail when I originally thought of the question, but it makes a bit of sense now after looking at the retrieved chunks. The answer were not in the retrieved chunks but it is in the corpus. So this is either a chunk ranking issue, the question is not grounded or the wording used in my question vs the corpus |
| 2 | Every answer names a source | MET | All answers contained at least one source for all 5 questions and 3 runs. Even though it did not give the expected answer for Question 1, it names the sources that it looked at and came the to conclusion that none of the sources/retrieved chunk contains the correct answer. |
| 3 | Gate stops out-of-corpus questions | MET | The gate rejected all obvious questions not related to my corpus. The closest best distance is 0.754, a good distance away from my selected cutoff of 0.6 |
| 4 | The sampled chunks contains the entire subsection of text, with no single chunk containing content from more than one city or topic. | MET | I used app.py ask question with --show-prompt which allowed me to look at the retrieved chunk and check and it contains only the subsection of headers and the answers did not mix unrelated information from a different chunk |
| 5 | Every answer the system produces accurate information for the requested city without mixing up information from other or surrounding city. | MET | Even though the answers for Question 1 was not the expected answer, it did not mix up information from the other cities based on the chunks it retrieved. For example, Question 5's retrieved source included guide_thornby_wells which contains information about Marchwood train but did not mix the information up or used that information. |

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

Diagnosis: Question 1 failed to provide correct answers. I think the issue is with the chunking. Looking at the retrieved chunk, there is a chunk with just the header and no context. The subsection should tied/link itself to the header during the chunking stage.

## The Improvement

**What I changed:**

The chunker now walks the heading matches keeping a stack of open ancestors by level, so each subsection knows its full parent trail (e.g. Walking in the region > Easy, on good surfaces) and prepends it as breadcrumbs before the heading line and body.

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

I only have 1 diagnosis, so it's to fix the chunking issue by linking subsections with its parent header. I'm hoping this will fix the issue by improving the ranking of the chunks now that it will have headers along with its context body.

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | 5/5 |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. The sampled chunks contains the entire subsection of text, with no single chunk containing content from more than one city or topic.| 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Every answer the system produces accurate information for the requested city without mixing up information from other or surrounding city.| 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

Yes, it was able to correctly answer Question 1 in all 3 runs. This fixes my revised target for Criterion 1 and MET the target. I also checked the chunk using --show-prompt and it contained the correct context body with correct header.

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
