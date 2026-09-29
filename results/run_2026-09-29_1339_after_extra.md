# Run log — after_extra

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-29 13:39

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Which town is the easiest for walking? |   |   |   |
| When do the restaurants close? |   |   |   |
| Which town's market has been running the longest? |   |   |   |
| How many tram lines does Marchwood have? |   |   |   |
| What to see at Givens Mills? |   |   |   |

> The Run columns are blank because `scorer.py` doesn't exist yet.
> Judge each question yourself by reading the output below, or build
> the scorer first and re-run.

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.803 | refused |
| How do I change the oil in a diesel engine? | 0.889 | refused |
| Who won the 1994 World Cup? | 0.975 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.826 | refused |
| How do I write a for loop in Rust? | 0.813 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### Which town is the easiest for walking? — run 1

- Best distance: 0.5078 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
Based on the documents, Thornby Wells is the region's most accessible town on foot, featuring flat, formal gardens and level streets (*guide_walking.md*).
```

### Which town is the easiest for walking? — run 2

- Best distance: 0.5078 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
According to **guide_walking.md**, **Thornby Wells** is the region's most accessible town on foot, featuring flat, formal gardens and level streets.
```

### Which town is the easiest for walking? — run 3

- Best distance: 0.5078 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
**Thornby Wells** has flat, formal gardens and level streets, making it the region's most accessible town on foot (guide_walking.md).
```

### When do the restaurants close? — run 1

- Best distance: 0.4639 (passed the gate)
- Sources retrieved: guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md

```
Based on the provided documents:

* In Halden Bay, everything closes by 9pm (and much of it closes entirely from November to February) (*guide_halden_bay.md*).
* Across the region (outside Marchwood), kitchens stop serving at 9pm and often earlier (*guide_eating.md*).
```

### When do the restaurants close? — run 2

- Best distance: 0.4639 (passed the gate)
- Sources retrieved: guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md

```
Based on the provided documents:

* In Halden Bay, everything closes by 9pm (guide_halden_bay.md).
* Across the region (outside Marchwood), kitchens stop serving at 9pm and often earlier (guide_eating.md).
```

### When do the restaurants close? — run 3

- Best distance: 0.4639 (passed the gate)
- Sources retrieved: guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md

```
Based on `guide_halden_bay.md`, everything in Halden Bay closes by 9pm. Additionally, `guide_eating.md` states that outside of Marchwood, kitchens across the region stop serving at 9pm and often earlier.
```

### Which town's market has been running the longest? — run 1

- Best distance: 0.4608 (passed the gate)
- Sources retrieved: guide_eating.md, guide_kestrelford.md, guide_thornby_wells.md

```
Kestrelford's market has been running the longest, as it has run continuously since the 1400s (source: `guide_eating.md` and `guide_kestrelford.md`).
```

### Which town's market has been running the longest? — run 2

- Best distance: 0.4608 (passed the gate)
- Sources retrieved: guide_eating.md, guide_kestrelford.md, guide_thornby_wells.md

```
Kestrelford's market has been running the longest, as it has run continuously since the 1400s (guide_eating.md and guide_kestrelford.md).
```

### Which town's market has been running the longest? — run 3

- Best distance: 0.4608 (passed the gate)
- Sources retrieved: guide_eating.md, guide_kestrelford.md, guide_thornby_wells.md

```
Based on the provided documents, Kestrelford's market has been running the longest, since the 1400s (source: `guide_eating.md` and `guide_kestrelford.md`).
```

### How many tram lines does Marchwood have? — run 1

- Best distance: 0.1898 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_marchwood.md

```
Marchwood has four tram lines (guide_marchwood.md and guide_accessibility.md).
```

### How many tram lines does Marchwood have? — run 2

- Best distance: 0.1898 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_marchwood.md

```
Marchwood has a tram network of four lines. 

This information comes from *guide_marchwood.md* and *guide_accessibility.md*.
```

### How many tram lines does Marchwood have? — run 3

- Best distance: 0.1898 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_marchwood.md

```
Marchwood has a tram network of four lines. 

Source: `guide_marchwood.md` (and also mentioned in `guide_accessibility.md`).
```

### What to see at Givens Mills? — run 1

- Best distance: 0.4368 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_givens_mill.md

```
Based on `guide_givens_mill.md`, visitors can see the working watermill, which runs tours on the hour from 11 to 3 with operating machinery, and the church, which features a Saxon doorway.
```

### What to see at Givens Mills? — run 2

- Best distance: 0.4368 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_givens_mill.md

```
Based on **guide_givens_mill.md**, visitors can see the working watermill, which runs tours on the hour from 11 to 3 with operating machinery. Additionally, visitors can see the church with its Saxon doorway and take a river walk downstream that reaches Brightwater in about three hours.
```

### What to see at Givens Mills? — run 3

- Best distance: 0.4368 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_givens_mill.md

```
According to `guide_givens_mill.md`, visitors to Givens Mill can see the working watermill (which offers tours on the hour from 11 to 3 with operating machinery), the church with its Saxon doorway, and the river walk downstream that reaches Brightwater in about three hours.
```
