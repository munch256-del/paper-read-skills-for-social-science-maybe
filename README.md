# paper-reader

A skill that reads academic papers, technical articles, and patents, then produces structured Obsidian-compatible markdown notes.
> I created this skill with WorkBuddy.

## What it does

Given a PDF, arXiv link, DOI, or pasted text, this skill:

1. Extracts and reads the full paper text
2. Applies a structured three-pass reading method
3. Generates a well-organized markdown note with theoretical positioning, key concepts, and critical evaluation
4. Writes the note directly to your Obsidian vault

## Methodology

The skill is built on three proven paper-reading frameworks:

- **S. Keshav — Three-Pass Method**: Skim → careful read → virtual reconstruction
- **JHU (Jason Eisner) — Critical Reading**: Annotate with questions, distill after reading, identify unstated assumptions
- **Heilmeier's Catechism**: Structured assessment framework

## Output Structure

Each note includes:

- One-sentence summary
- Pass 1 skimming notes (the 5 Cs: Category, Context, Correctness, Contributions, Clarity)
- Pass 2 detailed read: research motivation, theory map, key concepts glossary, method/model, results
- Pass 3 deep reconstruction (optional)
- Critical evaluation (5-question framework)
- Limitations & future work
- Selected references grouped by theoretical thread

## Installation

1. Download `paper-reader.zip`
2. In WorkBuddy, go to Skills management page
3. Upload the zip file
4. On first use, you will be prompted to set your Obsidian vault path

## Configuration

After installation, edit `config.json` in the skill folder (`~/.workbuddy/skills/paper-reader/config.json`):

```json
{
  "obsidian_vault_path": "/path/to/your/obsidian/vault",
  "output_folder": "Papers",
  "default_language": "en"
}
```

- `obsidian_vault_path`: Your local Obsidian vault path. If empty, you will be prompted on first use.
- `output_folder`: Subfolder inside your vault where notes are saved (default: `Papers`)
- `default_language`: `en` or `zh`. The skill auto-detects paper language but this sets the fallback.

## Templates

The skill includes two note templates:

- `assets/note-template-en.md` — for English papers
- `assets/note-template.md` — for Chinese papers

The skill auto-selects the template based on the paper's language.

## Requirements

- WorkBuddy (with skill support)
- Python 3 with `pdfplumber` (for PDF input): `pip install pdfplumber`

## License

MIT
