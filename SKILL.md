---
name: paper-reader
description: Read and structurally summarize academic papers, technical articles, and patents. Output Obsidian-compatible markdown notes with clear section structure, terminology explanations, and theoretical positioning. Use this skill when the user uploads a PDF, shares an arXiv link / URL / DOI, or pastes paper text and asks to "read this paper", "summarize this paper", "analyze this paper", or drops a paper into the chat. Trigger on any request to digest, summarize, critique, or structurally analyze an academic or technical article.
---

# Paper Reader

This skill reads papers and produces structured Obsidian markdown notes following proven paper-reading methodologies (Keshav's three-pass method + JHU critical reading framework).

## Overview

To produce a structured note for Obsidian, follow this workflow:

1. Acquire the paper text
2. Read following the three-pass method
3. Generate output using the note template
4. Write the note to the user's Obsidian vault

## Step 1: Acquire the Paper

Always read the paper fresh. Never rely on memory.

| Input Type | Action |
|---|---|
| PDF file | Use `scripts/parse_pdf.py` to extract text, or read directly if readable |
| arXiv link / arXiv ID | Use `web_fetch` on the abstract page, then fetch the PDF or HTML full text |
| DOI / publisher URL | Use `web_fetch` to retrieve the page, extract text from available HTML or PDF link |
| Pasted text | Use directly |
| Title only, no link | Ask the user for a link or file before proceeding |

If the paper is long, prioritize: title, abstract, introduction, method/theory, experiments/results, conclusion. Skim related work only if useful for theoretical positioning.

## Step 2: Three-Pass Reading

Follow S. Keshav's three-pass method during analysis:

### Pass 1 — Skim (5-10 minutes)
Answer the five Cs to decide whether to continue:
- **Category**: What type of paper is this?
- **Context**: Which other papers / theories is it related to?
- **Correctness**: Do the assumptions appear valid?
- **Contributions**: What are the main contributions?
- **Clarity**: Is the paper well written?

### Pass 2 — Read Carefully (1 hour)
Understand content and argument without getting stuck on every detail. Extract:
- Research motivation and problem statement
- Theoretical positioning (which theory family, rivals, dialogue partners)
- Core concepts and terminology
- Method / research model
- Key results

### Pass 3 — Deep Reconstruction (optional, 4-5 hours)
Virtually reconstruct the work. Compare your approach with the author's. Identify unstated assumptions and boundary conditions.

## Step 3: Generate the Note

Determine output language based on the paper's language and user preference. Default to the language of the paper.

| Output Language | Template to Use |
|---|---|
| Chinese (论文为中文或用户偏好中文) | `assets/note-template.md` |
| English (paper is in English) | `assets/note-template-en.md` |

Fill in all sections using the selected template:

- **Theoretical Positioning** (`🗺️ 理论定位`): Identify the theory used, its place in the broader theoretical family tree, rival theories, and the academic debate this paper joins.
- **Terminology** (`🧠 核心概念与名词解释`): Extract key terms, provide the paper's definition and your own restatement.
- **Critical Assessment**: Apply the 5-question framework from `references/reading-methods.md`:
  1. Paper's actual claims vs. author's stated claims
  2. What the study did NOT measure
  3. Generalizability across populations/contexts
  4. Which academic debate this paper participates in
  5. Missing key citations

## Step 4: Output to Obsidian Vault

1. Read the user's Obsidian vault path from `config.json` (located in the skill root directory)
2. If `config.json` does not exist or `obsidian_vault_path` is empty, ask the user for their Obsidian vault path and create/update the config file
3. Determine output filename: use the paper's English title if available; otherwise use the Chinese title. Save as `{{paper_title}}.md`
4. Write the note to the vault's `Papers/` folder (create it if needed). If a file with the same name exists, append a numeric suffix rather than overwriting
5. Confirm the file path to the user

## Reading Methodologies

The skill draws on three methodologies stored in `references/reading-methods.md`:

1. **S. Keshav — Three-Pass Method**: Skim → careful read → virtual reconstruction
2. **JHU (Jason Eisner) — Critical Reading**: Annotate with questions, distill after reading, identify unstated assumptions
3. **Heilmeier's Catechism**: Structured assessment framework (what are you trying to do, who cares, what are the risks, etc.)

Consult `references/reading-methods.md` for detailed methodology descriptions when needed.

## PDF Text Extraction

When the input is a PDF, use `scripts/parse_pdf.py` for text extraction:

```bash
python scripts/parse_pdf.py <pdf_path>
```

The script uses pdfplumber and outputs extracted text with page markers. Page markers can be used for citation purposes even though inline citation tags are not inserted automatically.

If pdfplumber is not installed, install it first:
```bash
pip install pdfplumber
```
