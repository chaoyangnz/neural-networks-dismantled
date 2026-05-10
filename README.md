# Neural Networks Dismantled
### A Unified Framework for Semantics, Mathematics, and Execution
**Second Edition Draft — 2026**

---

## Overview

This repository contains the full manuscript of *Neural Networks Dismantled* as
individually editable markdown files, plus a Python script that compiles them into
a styled PDF.

The book's core thesis: every neural-network architecture can be decoded with three
questions — **What** information is being represented? **How** does math implement it?
**Where** does hardware execute it? — and one framework: **Entity → Interaction → Update**.

---

## Repository Structure

```
neural_networks_dismantled/
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── build_pdf.py               # Compiles chapters/ → PDF
├── generate_chapters.py       # Re-generates chapter files from source (run once)
├── parts.yml                  # Part divider configuration
└── chapters/
    ├── 00_preface.md
    ├── 01_transparency_gap.md
    ├── 02_three_layer_map.md
    ├── 03_universal_loop.md
    ├── 04_tokenization.md
    ├── 05_tensors_shapes.md
    ├── 06_representations.md
    ├── 07_layers.md
    ├── 08_training.md
    ├── 09_autograd.md
    ├── 10_training_vs_inference.md
    ├── 11_data.md
    ├── 12_eiu_framework.md
    ├── 13_structure_spectrum.md
    ├── 14_motivation_layer.md
    ├── 15_composition_patterns.md
    ├── 16_mlps.md
    ├── 17_cnns.md
    ├── 18_rnns.md
    ├── 19_transformers.md
    ├── 20_domain_crosswalk.md
    ├── 21_multimodal.md
    ├── 22_scale.md
    ├── 23_pretraining.md
    ├── 24_sampling_decoding.md
    ├── 25_execution.md
    ├── 26_runtime.md
    ├── 27_rag.md
    ├── 28_how_to_read.md
    ├── 29_glossary.md
    ├── 30_practice_maps.md
    └── 31_references.md
```

---

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Build the PDF

```bash
python build_pdf.py
# Output: neural_networks_dismantled.pdf
```

Custom output path:

```bash
python build_pdf.py --output dist/book.pdf
```

---

## Editing Content

Every chapter is a standalone markdown file in `chapters/`. Edit any file directly —
the next `python build_pdf.py` run picks up all changes automatically.

Chapter files use standard markdown plus a small set of callout box types that render
as styled boxes in the PDF and as blockquotes on GitHub:

| Syntax | PDF Box | Colour |
|---|---|---|
| `> [KEY] text` | Key Concept | Blue |
| `> [USED] text` | You've Already Used This | Green |
| `> [MYTH] text` | Common Misconception | Orange |
| `> [PRACTICE] text` | In Practice | Purple |
| `> [TRACE label] text` | Trace / Walkthrough | Teal |
| `> [MENTAL] text` | Test Your Mental Model | Amber |
| `> [FAILURE] text` | Failure Mode | Rose |

### Adding a New Chapter

1. Create `chapters/32_my_chapter.md`
2. Add frontmatter at the top:
   ```
   ---
   chapter: 32
   title: "My New Chapter"
   ---
   ```
3. Write content in standard markdown
4. Run `python build_pdf.py`

### Adding a New Part Divider

Edit the `PARTS` dict in `build_pdf.py`:

```python
PARTS = {
    32: (7, "My New Part", "Description here.", "Chapters 32 – 33"),
    ...
}
```

---

## Book Structure

| Part | Chapters | Topic |
|---|---|---|
| I | 1–2 | The Orientation |
| II | 3–11 | Foundations |
| III | 12–13 | The Framework (EIU + Structure Spectrum) |
| IV | 14–21 | Architectures |
| V | 22–27 | Systems and Scale |
| VI | 28–31 | Reference |

---

## Contributing / Version Control Workflow

Because each chapter is a separate file, git diffs are clean and meaningful:

```bash
git diff chapters/19_transformers.md   # see exactly what changed in the transformers chapter
git log --oneline chapters/            # chapter-level history
git blame chapters/12_eiu_framework.md # line-level authorship
```

Suggested branch naming: `chapter/19-transformer-walkthrough`, `fix/glossary-confusion-pairs`.
