==================================================
Criteria Acceptance Tests
==================================================

# Criteria 1:

**Run 1**
--- Criteria 1: Malformed & Invalid POST Payloads ---
[PASS] Payload: JSON Array Payload
       Status: 400, Body: {"error":"bad_request","message":"Request must be a valid JSON object"}
[PASS] Payload: Missing Question Field
       Status: 400, Body: {"error":"bad_request","message":"Send JSON with a non-empty 'question' string field."}
[PASS] Payload: Empty Whitespace Question
       Status: 400, Body: {"error":"bad_request","message":"Send JSON with a non-empty 'question' string field."}
[PASS] Payload: Control Characters
       Status: 400, Body: {"error":"bad_request","message":"Question contains invalid control characters."}
[PASS] Payload: No Meaningful Words
       Status: 400, Body: {"error":"bad_request","message":"Question must contain words."}
[PASS] Criteria 1 Overall Result
```json
{"timestamp": "2026-11-17T17:49:04+00:00", "status_code": 400, "question": "", "error": "bad_request", "message": "Request must be a valid JSON object"}
{"timestamp": "2026-11-17T17:49:06+00:00", "status_code": 400, "question": null, "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:49:08+00:00", "status_code": 400, "question": "    ", "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:49:10+00:00", "status_code": 400, "question": "Hello\u0000World", "error": "bad_request", "message": "Question contains invalid control characters."}
{"timestamp": "2026-11-17T17:49:12+00:00", "status_code": 400, "question": "???!!!", "error": "bad_request", "message": "Question must contain words."}
```

**Run 2**
--- Criteria 1: Malformed & Invalid POST Payloads ---
[PASS] Payload: JSON Array Payload
       Status: 400, Body: {"error":"bad_request","message":"Request must be a valid JSON object"}
[PASS] Payload: Missing Question Field
       Status: 400, Body: {"error":"bad_request","message":"Send JSON with a non-empty 'question' string field."}
[PASS] Payload: Empty Whitespace Question
       Status: 400, Body: {"error":"bad_request","message":"Send JSON with a non-empty 'question' string field."}
[PASS] Payload: Control Characters
       Status: 400, Body: {"error":"bad_request","message":"Question contains invalid control characters."}
[PASS] Payload: No Meaningful Words
       Status: 400, Body: {"error":"bad_request","message":"Question must contain words."}
[PASS] Criteria 1 Overall Result
```json
{"timestamp": "2026-11-17T17:49:14+00:00", "status_code": 400, "question": "", "error": "bad_request", "message": "Request must be a valid JSON object"}
{"timestamp": "2026-11-17T17:49:16+00:00", "status_code": 400, "question": null, "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:49:18+00:00", "status_code": 400, "question": "    ", "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:49:20+00:00", "status_code": 400, "question": "Hello\u0000World", "error": "bad_request", "message": "Question contains invalid control characters."}
{"timestamp": "2026-11-17T17:49:22+00:00", "status_code": 400, "question": "???!!!", "error": "bad_request", "message": "Question must contain words."}

```

**Run 3**
--- Criteria 1: Malformed & Invalid POST Payloads ---
[PASS] Payload: JSON Array Payload
       Status: 400, Body: {"error":"bad_request","message":"Request must be a valid JSON object"}
[PASS] Payload: Missing Question Field
       Status: 400, Body: {"error":"bad_request","message":"Send JSON with a non-empty 'question' string field."}
[PASS] Payload: Empty Whitespace Question
       Status: 400, Body: {"error":"bad_request","message":"Send JSON with a non-empty 'question' string field."}
[PASS] Payload: Control Characters
       Status: 400, Body: {"error":"bad_request","message":"Question contains invalid control characters."}
[PASS] Payload: No Meaningful Words
       Status: 400, Body: {"error":"bad_request","message":"Question must contain words."}
[PASS] Criteria 1 Overall Result
```json
{"timestamp": "2026-11-17T17:49:24+00:00", "status_code": 400, "question": "", "error": "bad_request", "message": "Request must be a valid JSON object"}
{"timestamp": "2026-11-17T17:49:26+00:00", "status_code": 400, "question": null, "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:49:28+00:00", "status_code": 400, "question": "    ", "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:49:30+00:00", "status_code": 400, "question": "Hello\u0000World", "error": "bad_request", "message": "Question contains invalid control characters."}
{"timestamp": "2026-11-17T17:49:32+00:00", "status_code": 400, "question": "???!!!", "error": "bad_request", "message": "Question must contain words."}
```

# Criteria 2:

**Run 1**
--- Criteria 2: Request Logging Verification ---
[PASS] Criteria 2 Overall Result
       Logged requests: 5/5 (Initial: 85, Final: 90)
```json
{"timestamp": "2026-11-17T17:49:36+00:00", "status_code": 200, "question": "Which town is the easiest for walking?", "answer": "Based on the documents, Thornby Wells has flat, formal gardens and level streets, making it the region's most accessible town on foot. \n\nSource: `guide_walking.md`", "refused": "Based on the documents, Thornby Wells has flat, formal gardens and level streets, making it the region's most accessible town on foot. \n\nSource: `guide_walking.md`", "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_regional_transport.md", "guide_walking.md"], "best_distance": 0.5078, "threshold": 0.6, "prompt_tokens": 3739, "output_tokens": 300, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:49:38+00:00", "status_code": 400, "question": "    ", "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:49:41+00:00", "status_code": 200, "question": "When do the restaurants close?", "answer": "According to *guide_halden_bay.md*, everything in Halden Bay closes by 9pm. Additionally, *guide_eating.md* states that outside of Marchwood, kitchens across the region stop serving at 9pm and often earlier.", "refused": "According to *guide_halden_bay.md*, everything in Halden Bay closes by 9pm. Additionally, *guide_eating.md* states that outside of Marchwood, kitchens across the region stop serving at 9pm and often earlier.", "sources": ["guide_eating.md", "guide_elder_ness.md", "guide_givens_mill.md", "guide_halden_bay.md", "guide_kestrelford.md"], "best_distance": 0.4639, "threshold": 0.6, "prompt_tokens": 4290, "output_tokens": 353, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:49:43+00:00", "status_code": 400, "question": null, "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:49:48+00:00", "status_code": 200, "question": "What to see at Givens Mills?", "answer": "Based on the documents, at Givens Mill you can see the working watermill, which offers tours on the hour from 11 to 3 with operating machinery, and the church, which features a Saxon doorway. You can also take the river walk downstream that reaches Brightwater in about three hours. \n\nSource: `guide_givens_mill.md`", "refused": "Based on the documents, at Givens Mill you can see the working watermill, which offers tours on the hour from 11 to 3 with operating machinery, and the church, which features a Saxon doorway. You can also take the river walk downstream that reaches Brightwater in about three hours. \n\nSource: `guide_givens_mill.md`", "sources": ["guide_accessibility.md", "guide_givens_mill.md"], "best_distance": 0.4368, "threshold": 0.6, "prompt_tokens": 4817, "output_tokens": 428, "corpus": "city_guides"}
```

**Run 2**
--- Criteria 2: Request Logging Verification ---
[PASS] Criteria 2 Overall Result
       Logged requests: 5/5 (Initial: 90, Final: 95)
```json
{"timestamp": "2026-11-17T17:49:51+00:00", "status_code": 200, "question": "Which town is the easiest for walking?", "answer": "According to `guide_walking.md`, Thornby Wells has flat, formal gardens and level streets, making it the region's most accessible town on foot.", "refused": "According to `guide_walking.md`, Thornby Wells has flat, formal gardens and level streets, making it the region's most accessible town on foot.", "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_regional_transport.md", "guide_walking.md"], "best_distance": 0.5078, "threshold": 0.6, "prompt_tokens": 5555, "output_tokens": 461, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:49:54+00:00", "status_code": 400, "question": "    ", "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:49:56+00:00", "status_code": 200, "question": "When do the restaurants close?", "answer": "Based on the provided documents:\n\n* In Halden Bay, everything closes by 9pm (guide_halden_bay.md).\n* Across the region (outside of Marchwood), kitchens stop serving at 9pm and often earlier (guide_eating.md).", "refused": "Based on the provided documents:\n\n* In Halden Bay, everything closes by 9pm (guide_halden_bay.md).\n* Across the region (outside of Marchwood), kitchens stop serving at 9pm and often earlier (guide_eating.md).", "sources": ["guide_eating.md", "guide_elder_ness.md", "guide_givens_mill.md", "guide_halden_bay.md", "guide_kestrelford.md"], "best_distance": 0.4639, "threshold": 0.6, "prompt_tokens": 6106, "output_tokens": 518, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:49:58+00:00", "status_code": 400, "question": null, "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:50:01+00:00", "status_code": 200, "question": "What to see at Givens Mills?", "answer": "Based on the provided documents, at Givens Mill you can see the working watermill (which offers tours on the hour from 11 to 3 with operating machinery) and the church, which features a Saxon doorway. You can also take a river walk downstream that reaches Brightwater in about three hours (guide_givens_mill.md).", "refused": "Based on the provided documents, at Givens Mill you can see the working watermill (which offers tours on the hour from 11 to 3 with operating machinery) and the church, which features a Saxon doorway. You can also take a river walk downstream that reaches Brightwater in about three hours (guide_givens_mill.md).", "sources": ["guide_accessibility.md", "guide_givens_mill.md"], "best_distance": 0.4368, "threshold": 0.6, "prompt_tokens": 6633, "output_tokens": 589, "corpus": "city_guides"}

```

**Run 3**
--- Criteria 2: Request Logging Verification ---
[PASS] Criteria 2 Overall Result
       Logged requests: 5/5 (Initial: 95, Final: 100)
```json
{"timestamp": "2026-11-17T17:50:09+00:00", "status_code": 200, "question": "Which town is the easiest for walking?", "answer": "Based on the provided documents, **Thornby Wells** is described as the region's most accessible town on foot, featuring flat, formal gardens and level streets. \n\nSource: `guide_walking.md`", "refused": "Based on the provided documents, **Thornby Wells** is described as the region's most accessible town on foot, featuring flat, formal gardens and level streets. \n\nSource: `guide_walking.md`", "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_regional_transport.md", "guide_walking.md"], "best_distance": 0.5078, "threshold": 0.6, "prompt_tokens": 7371, "output_tokens": 634, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:50:11+00:00", "status_code": 400, "question": "    ", "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:50:17+00:00", "status_code": 200, "question": "When do the restaurants close?", "answer": "Based on the provided documents:\n\n* In Halden Bay, everything closes by 9pm (guide_halden_bay.md).\n* Across the region outside Marchwood, kitchens stop serving at 9pm and often earlier (guide_eating.md).", "refused": "Based on the provided documents:\n\n* In Halden Bay, everything closes by 9pm (guide_halden_bay.md).\n* Across the region outside Marchwood, kitchens stop serving at 9pm and often earlier (guide_eating.md).", "sources": ["guide_eating.md", "guide_elder_ness.md", "guide_givens_mill.md", "guide_halden_bay.md", "guide_kestrelford.md"], "best_distance": 0.4639, "threshold": 0.6, "prompt_tokens": 7922, "output_tokens": 689, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:50:19+00:00", "status_code": 400, "question": null, "error": "bad_request", "message": "Send JSON with a non-empty 'question' string field."}
{"timestamp": "2026-11-17T17:50:24+00:00", "status_code": 200, "question": "What to see at Givens Mills?", "answer": "Based on `guide_givens_mill.md`, visitors to Givens Mill can see a working watermill that offers tours on the hour from 11 to 3 with operating machinery, a church with a Saxon doorway, and a river walk downstream that reaches Brightwater in about three hours.", "refused": "Based on `guide_givens_mill.md`, visitors to Givens Mill can see a working watermill that offers tours on the hour from 11 to 3 with operating machinery, a church with a Saxon doorway, and a river walk downstream that reaches Brightwater in about three hours.", "sources": ["guide_accessibility.md", "guide_givens_mill.md"], "best_distance": 0.4368, "threshold": 0.6, "prompt_tokens": 8449, "output_tokens": 750, "corpus": "city_guides"}

```

# Criteria 3:
**Run 1-3**
--- Criteria 3: Unindexed Corpus Guard ---
[PASS] Criteria 3 Overall Result
       Status: 500, Body: {"error":"index_not_ready","message":"No index for this corpus - Run python app.py index before serve.py"}
```json
{"timestamp": "2026-11-17T18:34:50+00:00", "status_code": 500, "question": "Which town is the easiest for walking?", "error": "index_not_ready", "message": "No index for this corpus - Run python app.py index before serve.py"}
```

# Criteria 4:

**Run 1-3**
--- Criteria 4: Quota Limit Enforcement ---
[PASS] Criteria 4 Overall Result
       4th Request Status: 500, Body: {"error":"quota_guard_error","message":"QuotaGuard: This session has made 3 requests, which is the budget set in config.py (SESSION_REQUEST_BUDGET).\nThat usually means a loop is running away rather than that you've done 3 requests' worth of real work.\nStop the program and look for the loop. If you really do need more, raise the number in config.py \u2014 but look first."}
```json
{"timestamp": "2026-11-17T18:03:13+00:00", "status_code": 200, "question": "Which town is the easiest for walking? 1", "answer": "**Thornby Wells** is described as the region's most accessible town on foot and the easiest town in the region. \n\n*(Source: guide_walking.md and guide_accessibility.md)*", "refused": "**Thornby Wells** is described as the region's most accessible town on foot and the easiest town in the region. \n\n*(Source: guide_walking.md and guide_accessibility.md)*", "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_walking.md"], "best_distance": 0.5045, "threshold": 0.6, "prompt_tokens": 800, "output_tokens": 43, "corpus": "city_guides"}
{"timestamp": "2026-11-17T18:03:21+00:00", "status_code": 200, "question": "Which town is the easiest for walking? 2", "answer": "**Thornby Wells** is described as the easiest town in the region for walking, featuring flat, formal gardens and level streets. \n\nSource: `guide_walking.md` and `guide_accessibility.md`", "refused": "**Thornby Wells** is described as the easiest town in the region for walking, featuring flat, formal gardens and level streets. \n\nSource: `guide_walking.md` and `guide_accessibility.md`", "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_walking.md"], "best_distance": 0.5043, "threshold": 0.6, "prompt_tokens": 1600, "output_tokens": 89, "corpus": "city_guides"}
{"timestamp": "2026-11-17T18:03:26+00:00", "status_code": 200, "question": "Which town is the easiest for walking? 3", "answer": "Based on the documents, Thornby Wells is the region's most accessible town on foot, featuring flat, formal gardens and level streets. \n\nSource: `guide_walking.md`", "refused": "Based on the documents, Thornby Wells is the region's most accessible town on foot, featuring flat, formal gardens and level streets. \n\nSource: `guide_walking.md`", "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_walking.md"], "best_distance": 0.4995, "threshold": 0.6, "prompt_tokens": 2331, "output_tokens": 128, "corpus": "city_guides"}
{"timestamp": "2026-11-17T18:03:28+00:00", "status_code": 500, "question": "4th request exceeding quota budget. Which town is the easiest for walking?", "error": "quota_guard_error", "message": "QuotaGuard: This session has made 3 requests, which is the budget set in config.py (SESSION_REQUEST_BUDGET).\nThat usually means a loop is running away rather than that you've done 3 requests' worth of real work.\nStop the program and look for the loop. If you really do need more, raise the number in config.py — but look first."}{"timestamp": "2026-11-17T18:05:32+00:00", "status_code": 500, "question": "Which town is the easiest for walking? 1", "error": "quota_guard_error", "message": "QuotaGuard: This session has made 3 requests, which is the budget set in config.py (SESSION_REQUEST_BUDGET).\nThat usually means a loop is running away rather than that you've done 3 requests' worth of real work.\nStop the program and look for the loop. If you really do need more, raise the number in config.py — but look first."}
{"timestamp": "2026-11-17T18:05:34+00:00", "status_code": 500, "question": "Which town is the easiest for walking? 2", "error": "quota_guard_error", "message": "QuotaGuard: This session has made 3 requests, which is the budget set in config.py (SESSION_REQUEST_BUDGET).\nThat usually means a loop is running away rather than that you've done 3 requests' worth of real work.\nStop the program and look for the loop. If you really do need more, raise the number in config.py — but look first."}
{"timestamp": "2026-11-17T18:05:36+00:00", "status_code": 500, "question": "Which town is the easiest for walking? 3", "error": "quota_guard_error", "message": "QuotaGuard: This session has made 3 requests, which is the budget set in config.py (SESSION_REQUEST_BUDGET).\nThat usually means a loop is running away rather than that you've done 3 requests' worth of real work.\nStop the program and look for the loop. If you really do need more, raise the number in config.py — but look first."}
{"timestamp": "2026-11-17T18:05:38+00:00", "status_code": 500, "question": "4th request exceeding quota budget. Which town is the easiest for walking?", "error": "quota_guard_error", "message": "QuotaGuard: This session has made 3 requests, which is the budget set in config.py (SESSION_REQUEST_BUDGET).\nThat usually means a loop is running away rather than that you've done 3 requests' worth of real work.\nStop the program and look for the loop. If you really do need more, raise the number in config.py — but look first."}
```

# Criteria 5:

**Run 1**
--- Criteria 5: Token Usage Cap on 5th Request ---
[PASS] Criteria 5 Overall Result
       5th Request Token Sum: 3229 (Prompt: 3001, Output: 228) < 6,000
```json
{"timestamp": "2026-11-17T17:30:54+00:00", "status_code": 200, "question": "Which town is the easiest for walking?", "answer": "Based on the documents, Thornby Wells is described as the region's most accessible town on foot, featuring flat, formal gardens and level streets (*guide_walking.md*).", "refused": "Based on the documents, Thornby Wells is described as the region's most accessible town on foot, featuring flat, formal gardens and level streets (*guide_walking.md*).", "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_regional_transport.md", "guide_walking.md"], "best_distance": 0.5078, "threshold": 0.6, "prompt_tokens": 738, "output_tokens": 37, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:31:01+00:00", "status_code": 200, "question": "When do the restaurants close?", "answer": "In Halden Bay, everything closes by 9pm (guide_halden_bay.md). Across the region, kitchens stop serving at 9pm and often earlier (guide_eating.md).", "refused": "In Halden Bay, everything closes by 9pm (guide_halden_bay.md). Across the region, kitchens stop serving at 9pm and often earlier (guide_eating.md).", "sources": ["guide_eating.md", "guide_elder_ness.md", "guide_givens_mill.md", "guide_halden_bay.md", "guide_kestrelford.md"], "best_distance": 0.4639, "threshold": 0.6, "prompt_tokens": 1289, "output_tokens": 79, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:31:09+00:00", "status_code": 200, "question": "Which town's market has been running the longest?", "answer": "Kestrelford's market has been running since the 1400s, which is longer than Marchwood's market, which has operated since 1863. \n\nSources: `guide_eating.md` and `guide_kestrelford.md`", "refused": "Kestrelford's market has been running since the 1400s, which is longer than Marchwood's market, which has operated since 1863. \n\nSources: `guide_eating.md` and `guide_kestrelford.md`", "sources": ["guide_eating.md", "guide_kestrelford.md", "guide_thornby_wells.md"], "best_distance": 0.4608, "threshold": 0.6, "prompt_tokens": 1841, "output_tokens": 138, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:31:16+00:00", "status_code": 200, "question": "How many tram lines does Marchwood have?", "answer": "Marchwood has four tram lines, according to **guide_marchwood.md** and **guide_accessibility.md**.", "refused": "Marchwood has four tram lines, according to **guide_marchwood.md** and **guide_accessibility.md**.", "sources": ["guide_accessibility.md", "guide_marchwood.md"], "best_distance": 0.1898, "threshold": 0.6, "prompt_tokens": 2474, "output_tokens": 163, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:31:24+00:00", "status_code": 200, "question": "What to see at Givens Mills?", "answer": "Based on the provided documents, at Givens Mill you can see the working watermill (which offers tours on the hour from 11 to 3 with operating machinery), the church with its Saxon doorway, and the river walk downstream that reaches Brightwater in about three hours (guide_givens_mill.md).", "refused": "Based on the provided documents, at Givens Mill you can see the working watermill (which offers tours on the hour from 11 to 3 with operating machinery), the church with its Saxon doorway, and the river walk downstream that reaches Brightwater in about three hours (guide_givens_mill.md).", "sources": ["guide_accessibility.md", "guide_givens_mill.md"], "best_distance": 0.4368, "threshold": 0.6, "prompt_tokens": 3001, "output_tokens": 228, "corpus": "city_guides"}
```

**Run 2**
--- Criteria 5: Token Usage Cap on 5th Request ---
[PASS] Criteria 5 Overall Result
       5th Request Token Sum: 3217 (Prompt: 3001, Output: 216) < 6,000
```json
{"timestamp": "2026-11-17T17:36:17+00:00", "status_code": 200, "question": "Which town is the easiest for walking?", "answer": "According to *guide_walking.md*, **Thornby Wells** is the region's most accessible town on foot, featuring flat, formal gardens and level streets.", "refused": "According to *guide_walking.md*, **Thornby Wells** is the region's most accessible town on foot, featuring flat, formal gardens and level streets.", "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_regional_transport.md", "guide_walking.md"], "best_distance": 0.5078, "threshold": 0.6, "prompt_tokens": 738, "output_tokens": 35, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:36:25+00:00", "status_code": 200, "question": "When do the restaurants close?", "answer": "In Halden Bay, everything closes by 9pm (guide_halden_bay.md). Across the region (outside Marchwood), kitchens stop serving at 9pm and often earlier (guide_eating.md).", "refused": "In Halden Bay, everything closes by 9pm (guide_halden_bay.md). Across the region (outside Marchwood), kitchens stop serving at 9pm and often earlier (guide_eating.md).", "sources": ["guide_eating.md", "guide_elder_ness.md", "guide_givens_mill.md", "guide_halden_bay.md", "guide_kestrelford.md"], "best_distance": 0.4639, "threshold": 0.6, "prompt_tokens": 1289, "output_tokens": 81, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:36:33+00:00", "status_code": 200, "question": "Which town's market has been running the longest?", "answer": "Kestrelford's market has been running the longest, since the 1400s (mentioned in both **guide_eating.md** and **guide_kestrelford.md**).", "refused": "Kestrelford's market has been running the longest, since the 1400s (mentioned in both **guide_eating.md** and **guide_kestrelford.md**).", "sources": ["guide_eating.md", "guide_kestrelford.md", "guide_thornby_wells.md"], "best_distance": 0.4608, "threshold": 0.6, "prompt_tokens": 1841, "output_tokens": 123, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:36:43+00:00", "status_code": 200, "question": "How many tram lines does Marchwood have?", "answer": "Marchwood has four tram lines, according to **guide_marchwood.md** and **guide_accessibility.md**.", "refused": "Marchwood has four tram lines, according to **guide_marchwood.md** and **guide_accessibility.md**.", "sources": ["guide_accessibility.md", "guide_marchwood.md"], "best_distance": 0.1898, "threshold": 0.6, "prompt_tokens": 2474, "output_tokens": 148, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:36:52+00:00", "status_code": 200, "question": "What to see at Givens Mills?", "answer": "According to `guide_givens_mill.md`, visitors to Givens Mill can see the working watermill (which offers tours on the hour from 11 to 3 with operating machinery) and the church, which features a Saxon doorway. Additionally, there is a river walk downstream that reaches Brightwater in about three hours.", "refused": "According to `guide_givens_mill.md`, visitors to Givens Mill can see the working watermill (which offers tours on the hour from 11 to 3 with operating machinery) and the church, which features a Saxon doorway. Additionally, there is a river walk downstream that reaches Brightwater in about three hours.", "sources": ["guide_accessibility.md", "guide_givens_mill.md"], "best_distance": 0.4368, "threshold": 0.6, "prompt_tokens": 3001, "output_tokens": 216, "corpus": "city_guides"}
```
**Run 3**
--- Criteria 5: Token Usage Cap on 5th Request ---
[PASS] Criteria 5 Overall Result
       5th Request Token Sum: 3261 (Prompt: 3001, Output: 260) < 6,000
```json
{"timestamp": "2026-11-17T17:45:51+00:00", "status_code": 200, "question": "Which town is the easiest for walking?", "answer": "According to **guide_walking.md**, **Thornby Wells** is the region's most accessible town on foot, featuring flat, formal gardens and level streets.", "refused": "According to **guide_walking.md**, **Thornby Wells** is the region's most accessible town on foot, featuring flat, formal gardens and level streets.", "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_regional_transport.md", "guide_walking.md"], "best_distance": 0.5078, "threshold": 0.6, "prompt_tokens": 738, "output_tokens": 35, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:45:54+00:00", "status_code": 200, "question": "When do the restaurants close?", "answer": "Based on the provided documents:\n- In Halden Bay, everything closes by 9pm (guide_halden_bay.md).\n- Across the region (outside Marchwood), kitchens stop serving at 9pm and often earlier, with Kestrelford's pubs specifically serving only between 12 to 2 and 6 to 8:30 (guide_eating.md).", "refused": "Based on the provided documents:\n- In Halden Bay, everything closes by 9pm (guide_halden_bay.md).\n- Across the region (outside Marchwood), kitchens stop serving at 9pm and often earlier, with Kestrelford's pubs specifically serving only between 12 to 2 and 6 to 8:30 (guide_eating.md).", "sources": ["guide_eating.md", "guide_elder_ness.md", "guide_givens_mill.md", "guide_halden_bay.md", "guide_kestrelford.md"], "best_distance": 0.4639, "threshold": 0.6, "prompt_tokens": 1289, "output_tokens": 118, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:45:57+00:00", "status_code": 200, "question": "Which town's market has been running the longest?", "answer": "Based on the provided documents, Kestrelford's market has been running the longest, since the 1400s (mentioned in both `guide_eating.md` and `guide_kestrelford.md`).", "refused": "Based on the provided documents, Kestrelford's market has been running the longest, since the 1400s (mentioned in both `guide_eating.md` and `guide_kestrelford.md`).", "sources": ["guide_eating.md", "guide_kestrelford.md", "guide_thornby_wells.md"], "best_distance": 0.4608, "threshold": 0.6, "prompt_tokens": 1841, "output_tokens": 165, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:46:00+00:00", "status_code": 200, "question": "How many tram lines does Marchwood have?", "answer": "Marchwood has four tram lines, according to `guide_marchwood.md` and `guide_accessibility.md`.", "refused": "Marchwood has four tram lines, according to `guide_marchwood.md` and `guide_accessibility.md`.", "sources": ["guide_accessibility.md", "guide_marchwood.md"], "best_distance": 0.1898, "threshold": 0.6, "prompt_tokens": 2474, "output_tokens": 190, "corpus": "city_guides"}
{"timestamp": "2026-11-17T17:46:03+00:00", "status_code": 200, "question": "What to see at Givens Mills?", "answer": "At Givens Mill, you can see the working watermill (which offers tours with operating machinery on the hour from 11 to 3) and the church, which features a Saxon doorway. There is also a river walk downstream that reaches Brightwater in about three hours. \n\nSource: `guide_givens_mill.md`", "refused": "At Givens Mill, you can see the working watermill (which offers tours with operating machinery on the hour from 11 to 3) and the church, which features a Saxon doorway. There is also a river walk downstream that reaches Brightwater in about three hours. \n\nSource: `guide_givens_mill.md`", "sources": ["guide_accessibility.md", "guide_givens_mill.md"], "best_distance": 0.4368, "threshold": 0.6, "prompt_tokens": 3001, "output_tokens": 260, "corpus": "city_guides"}
```