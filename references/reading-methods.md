# Reading Methodologies Reference

This document consolidates three paper-reading methodologies that the `paper-reader` skill draws upon. Consult this when structuring analysis or explaining the reading process to the user.

---

## 1. S. Keshav — The Three-Pass Method

**Source**: "How to Read a Paper", ACM SIGCOMM Computer Communication Review, 2007.

### Pass 1 — Skim (5-10 minutes)

Read: title, abstract, introduction, section/first paragraph of each section, conclusion, references (glance only).

Answer the five Cs:
1. **Category**: What type of paper? (measurement, analysis, research prototype, survey...)
2. **Context**: Which papers is it related to? What theoretical bases?
3. **Correctness**: Do the assumptions appear valid?
4. **Contributions**: What are the main contributions?
5. **Clarity**: Is the paper well written?

**Decision**: Continue to Pass 2, or stop here.

### Pass 2 — Read Carefully (1 hour)

Read the paper carefully but without getting stuck on every detail. Take notes in the margins.

- Grasp the content and argument
- Identify the key assumptions
- Note the limitations of experiments or analysis
- Understand the mathematical / technical core

At the end, be able to summarize the main idea with supporting evidence.

### Pass 3 — Virtual Reconstruction (4-5 hours for beginners, ~1 hour for experienced)

Reproduce the work from memory:
- Virtually re-implement the paper
- Compare your reconstruction with the actual paper
- Identify the author's hidden assumptions
- Identify missing citations to relevant work
- Identify potential issues with experimental or analytical techniques

### Doing a Literature Survey with Three-Pass

1. Use Google Scholar / CiteSeer with well-chosen keywords to find 3-5 recent papers
2. Do Pass 1 on each to get a sense of the work; read their "Related Work" sections
3. Find shared citations and repeated author names — these are the key papers and researchers
4. Download the key papers; also check key researchers' websites for recent publications
5. Go to the websites of the key conferences in the area to find top-tier recent papers

---

## 2. JHU (Jason Eisner) — Critical Reading Advice

**Source**: "How to Read a Technical Paper", Johns Hopkins University, 2009 (updated 2018).

### Reading Strategies

- **Read actively, not passively**: Annotate with your own words, not just highlight
- **Multiple passes**: First pass = skip hard parts, get the gist. Second pass = read carefully if the paper is worth it
- **Force reading speed**: Set a time limit per page; use PDF auto-scroll to avoid getting stuck
- **Read backwards**: For difficult papers, read a later paper that cites this one — later work often explains the method more clearly

### Note-Taking

**Low-level notes** (while reading, on printed copy or PDF):
- Restate unclear points in your own words
- Fill in skipped details (assumptions, algebra, pseudocode)
- Annotate types of mathematical objects
- Give examples that confirm or counterexample the author's claims
- Relate to known similar methods or problems
- Record questions and logical gaps
- Brainstorm follow-up research directions

**High-level notes** (after reading, distilled):
- Restate the core idea in your own words
- Compare with other work in the same area
- Record your questions and follow-up ideas
- Note the corresponding figures, formulas, section numbers for quick recall
- Attach the original paper link

### When Stuck

- **Don't understand the background**: Read textbooks, tutorials, review articles, or Wikipedia first
- **Paper is too hard**: Read a later paper that cites this one; the explanation is often clearer
- **New to the field**: Thoroughly understand one foundational paper — this dramatically speeds up reading all subsequent papers in the area

### Literature Search Tips

- Try different search keywords; think from the author's perspective
- Use backward search (references) and forward search (who cited this paper)
- Use curated reading lists: review articles, course syllabi, reading group pages, textbook chapters
- Breadth-first exploration: read many abstracts first, then select the most relevant papers for deep reading

---

## 3. Heilmeier's Catechism (Adapted for Paper Reading)

Originally a set of questions for evaluating research proposals. Adapted here as a structured assessment framework.

1. **What are you trying to do?** (Articulate in plain language, no jargon)
2. **What is the problem, how is it done today, and what are the limits of current practice?**
3. **What is new in the approach, including core idea, math, and method?**
4. **Who cares?** If successful, what difference does it make?
5. **What are the risks?**
6. **How much will it cost?** (Compute, data, engineering effort, or deployment cost)
7. **What are the experiments and results?**

In the adapted framework for paper reading, separate "paper's claims" from "your own analysis" explicitly.

---

## 4. Critical Questions Framework

Use these questions to move from "summarizing the paper" to "evaluating the paper":

| Question | Purpose |
|----------|---------|
| What can and cannot be concluded from the methods and results alone? | Expose over-claiming |
| What does the study NOT measure? | Identify unstated assumptions |
| How would results change in different populations/contexts? | Test generalizability |
| Which academic debate does this paper participate in? | Locate the paper in scholarly conversation |
| Which key citation is missing? | Identify blind spots |

---

## 5. Tips for Using These Methodologies Together

- **Pass 1** (Keshav) → decide whether to continue
- **Pass 2** (Keshav) + **Eisner note-taking** → extract structure, theory, terms
- **Pass 3** (Keshav) → deep virtual reconstruction (optional)
- **Heilmeier + Critical Questions** → structure the final note's critical assessment section
- **Theory mapping** → always ask: where does this theory sit in the broader theoretical family tree?
