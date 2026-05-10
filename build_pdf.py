"""
build_pdf.py
============
Reads all chapter markdown files from chapters/ and generates the styled PDF.

Usage:
    python build_pdf.py
    python build_pdf.py --output my_output.pdf
    python build_pdf.py --chapters chapters/ --output dist/book.pdf

Dependencies:
    pip install reportlab

Markdown callout syntax (renders as styled boxes in PDF, blockquotes on GitHub):
    > [KEY]          Key Concept box       (blue)
    > [USED]         You've Already Used This box  (green)
    > [MYTH]         Common Misconception box      (orange)
    > [PRACTICE]     In Practice box               (purple)
    > [TRACE label]  Trace / walkthrough box       (teal)
    > [MENTAL]       Test Your Mental Model box    (amber)
    > [FAILURE]      Failure Mode box              (rose)
"""

import os, re, glob, argparse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib.colors import HexColor

# ── Palette ───────────────────────────────────────────────────────────────────
DARK     = HexColor("#1a1a2e")
ACCENT   = HexColor("#2563eb")
ACCENT2  = HexColor("#1e40af")
LIGHT_BG = HexColor("#f0f4ff")
MID_BG   = HexColor("#dbeafe")
RULE_CLR = HexColor("#bfdbfe")
BODY_CLR = HexColor("#1e293b")
MUTED    = HexColor("#64748b")
WHITE    = colors.white
CODE_BG  = HexColor("#f8fafc")
USED_BG  = HexColor("#f0fdf4"); USED_BDR  = HexColor("#16a34a")
MISC_BG  = HexColor("#fff7ed"); MISC_BDR  = HexColor("#ea580c")
PRAC_BG  = HexColor("#faf5ff"); PRAC_BDR  = HexColor("#7c3aed")
TRACE_BG = HexColor("#f0fdfa"); TRACE_BDR = HexColor("#0d9488")
MIND_BG  = HexColor("#fefce8"); MIND_BDR  = HexColor("#ca8a04")
FAIL_BG  = HexColor("#fff1f2"); FAIL_BDR  = HexColor("#e11d48")

W = 6.5 * inch

# ── Styles ────────────────────────────────────────────────────────────────────
def S(name, **kw): return ParagraphStyle(name, **kw)

BookTitle = S("BT", fontName="Helvetica-Bold",        fontSize=28, leading=34, textColor=WHITE,    alignment=TA_CENTER, spaceAfter=8)
BookSub   = S("BS", fontName="Helvetica",             fontSize=12, leading=16, textColor=HexColor("#bfdbfe"), alignment=TA_CENTER, spaceAfter=6)
BookEd    = S("BE", fontName="Helvetica-Oblique",     fontSize=10,             textColor=HexColor("#93c5fd"), alignment=TA_CENTER)
ChLbl     = S("CL", fontName="Helvetica",             fontSize=10, leading=13, textColor=ACCENT,   spaceBefore=18, spaceAfter=2)
H1st      = S("H1", fontName="Helvetica-Bold",        fontSize=20, leading=26, textColor=DARK,     spaceBefore=4, spaceAfter=8)
H2st      = S("H2", fontName="Helvetica-Bold",        fontSize=13, leading=17, textColor=ACCENT2,  spaceBefore=16, spaceAfter=5)
H3st      = S("H3", fontName="Helvetica-BoldOblique", fontSize=11, leading=15, textColor=DARK,     spaceBefore=10, spaceAfter=3)
Bodyf     = S("Bd", fontName="Helvetica",             fontSize=10, leading=15, textColor=BODY_CLR, alignment=TA_JUSTIFY, spaceBefore=2, spaceAfter=4)
Bulf      = S("Bu", fontName="Helvetica",             fontSize=10, leading=15, textColor=BODY_CLR, leftIndent=16, firstLineIndent=-10, spaceBefore=2, spaceAfter=2)
Codef     = S("Co", fontName="Courier",               fontSize=8,  leading=12, textColor=BODY_CLR, backColor=CODE_BG, leftIndent=10, rightIndent=10, spaceBefore=5, spaceAfter=5, borderPadding=5)
PartNum   = S("PN", fontName="Helvetica",             fontSize=11,             textColor=HexColor("#93c5fd"), alignment=TA_CENTER, spaceAfter=6)
PartTi    = S("PT", fontName="Helvetica-Bold",        fontSize=26, leading=32, textColor=WHITE,    alignment=TA_CENTER)
PartSub   = S("PS", fontName="Helvetica",             fontSize=12, leading=16, textColor=HexColor("#bfdbfe"), alignment=TA_CENTER)
PartCh    = S("PC", fontName="Helvetica",             fontSize=9,  leading=14, textColor=HexColor("#93c5fd"), alignment=TA_CENTER)
TOCPt     = S("TP", fontName="Helvetica-Bold",        fontSize=11, leading=14, textColor=DARK,     spaceBefore=8, spaceAfter=2)
TOCCh     = S("TC", fontName="Helvetica",             fontSize=10, leading=14, textColor=BODY_CLR, leftIndent=14, spaceBefore=1)

# ── Low-level helpers ─────────────────────────────────────────────────────────
def _rule(): return HRFlowable(width="100%", thickness=0.5, color=RULE_CLR, spaceAfter=8, spaceBefore=2)
def _sp(n=6): return Spacer(1, n)

def _box(label, body_text, bg, bdr):
    inner = Paragraph(f"<b>{label}</b><br/>{body_text}",
        S("BI", fontName="Helvetica", fontSize=9.5, leading=14, textColor=DARK))
    t = Table([[inner]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0,0),(-1,-1), bg),
        ("BOX",          (0,0),(-1,-1), 1.5, bdr),
        ("LEFTPADDING",  (0,0),(-1,-1), 10),
        ("RIGHTPADDING", (0,0),(-1,-1), 10),
        ("TOPPADDING",   (0,0),(-1,-1), 7),
        ("BOTTOMPADDING",(0,0),(-1,-1), 7),
    ]))
    return t

BOX_MAP = {
    "KEY":      ("Key Concept",                MID_BG,  ACCENT),
    "USED":     ("You\u2019ve Already Used This", USED_BG, USED_BDR),
    "MYTH":     ("Common Misconception",        MISC_BG, MISC_BDR),
    "PRACTICE": ("In Practice",                 PRAC_BG, PRAC_BDR),
    "MENTAL":   ("Test Your Mental Model",      MIND_BG, MIND_BDR),
    "FAILURE":  ("Failure Mode",                FAIL_BG, FAIL_BDR),
}

def _make_table(headers, rows):
    col_w = W / max(len(headers), 1)
    data = [[Paragraph(f"<b>{h}</b>", S("TH", fontName="Helvetica-Bold", fontSize=9,
             leading=12, textColor=WHITE)) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c).strip(), S("TD", fontName="Helvetica", fontSize=9,
                     leading=13, textColor=BODY_CLR)) for c in row])
    t = Table(data, colWidths=[col_w]*len(headers), repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",     (0,0),(-1,0),  ACCENT),
        ("ROWBACKGROUNDS", (0,1),(-1,-1), [WHITE, LIGHT_BG]),
        ("GRID",           (0,0),(-1,-1), 0.4, RULE_CLR),
        ("LEFTPADDING",    (0,0),(-1,-1), 5),
        ("RIGHTPADDING",   (0,0),(-1,-1), 5),
        ("TOPPADDING",     (0,0),(-1,-1), 4),
        ("BOTTOMPADDING",  (0,0),(-1,-1), 4),
        ("VALIGN",         (0,0),(-1,-1), "TOP"),
    ]))
    return t

def _part_page(num, title, desc, ch_list):
    rows = [[Paragraph(f"PART {num}", PartNum)],
            [Paragraph(title, PartTi)],
            [_sp(10)],
            [Paragraph(desc, PartSub)],
            [_sp(16)],
            [Paragraph(ch_list, PartCh)]]
    outer = Table(rows, colWidths=[W])
    outer.setStyle(TableStyle([
        ("BACKGROUND",   (0,0),(-1,-1), DARK),
        ("TOPPADDING",   (0,0),(-1,-1), 16),
        ("BOTTOMPADDING",(0,0),(-1,-1), 16),
        ("LEFTPADDING",  (0,0),(-1,-1), 32),
        ("RIGHTPADDING", (0,0),(-1,-1), 32),
    ]))
    return [Spacer(1, 1.2*inch), outer, PageBreak()]

def _hf(canvas, doc):
    canvas.saveState()
    PW, PH = letter
    canvas.setFillColor(DARK)
    canvas.rect(0, PH-36, PW, 36, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 9); canvas.setFillColor(WHITE)
    canvas.drawString(inch*0.75, PH-22, "Neural Networks Dismantled")
    canvas.setFont("Helvetica", 9); canvas.setFillColor(HexColor("#93c5fd"))
    canvas.drawRightString(PW-inch*0.75, PH-22, "Second Edition \u2014 2026")
    canvas.setStrokeColor(RULE_CLR); canvas.setLineWidth(0.5)
    canvas.line(inch*0.75, 42, PW-inch*0.75, 42)
    canvas.setFont("Helvetica", 8); canvas.setFillColor(MUTED)
    canvas.drawCentredString(PW/2, 28, str(doc.page))
    canvas.restoreState()

# ── Inline markdown → ReportLab XML ──────────────────────────────────────────
def _inline(text):
    """Convert **bold**, *italic*, and `code` inline markdown to ReportLab XML."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*',     r'<i>\1</i>', text)
    text = re.sub(r'`(.+?)`',       r'<font face="Courier">\1</font>', text)
    return text

# ── Markdown parser → flowables ───────────────────────────────────────────────
def parse_frontmatter(text):
    """Extract YAML-style frontmatter and return (meta_dict, body_text)."""
    meta = {}
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            fm = text[3:end].strip()
            for line in fm.splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip().strip('"')
            text = text[end+3:].strip()
    return meta, text

def _flush_paragraph(buf, flowables):
    if buf:
        flowables.append(Paragraph(_inline(" ".join(buf)), Bodyf))
        flowables.append(_sp(2))
        buf.clear()

def _flush_bullet(buf, flowables):
    if buf:
        flowables.append(Paragraph("&#8226;&#160;&#160;" + _inline(" ".join(buf)), Bulf))
        buf.clear()

def markdown_to_flowables(text, chapter_num, chapter_title):
    """Parse markdown body text and return a list of ReportLab flowables."""
    flowables = []

    # Chapter heading
    flowables.append(Paragraph(f"Chapter {chapter_num}", ChLbl))
    flowables.append(Paragraph(chapter_title, H1st))
    flowables.append(_rule())

    lines = text.splitlines()
    i = 0
    para_buf = []
    bullet_buf = []
    in_code = False
    code_buf = []

    while i < len(lines):
        line = lines[i]

        # ── fenced code block ─────────────────────────────────────────────────
        if line.strip().startswith("```"):
            _flush_paragraph(para_buf, flowables)
            _flush_bullet(bullet_buf, flowables)
            if in_code:
                raw = "\n".join(code_buf)
                raw = raw.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
                flowables.append(Paragraph(raw, Codef))
                flowables.append(_sp(4))
                code_buf = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        # ── callout blockquote  > [TYPE label] text ───────────────────────────
        if line.startswith("> "):
            _flush_paragraph(para_buf, flowables)
            _flush_bullet(bullet_buf, flowables)
            # collect multiline blockquote
            bq_lines = []
            while i < len(lines) and (lines[i].startswith("> ") or lines[i].strip() == ">"):
                bq_lines.append(lines[i][2:] if lines[i].startswith("> ") else "")
                i += 1
            bq_text = " ".join(bq_lines).strip()
            # parse [TYPE] or [TYPE label]
            m = re.match(r'\[([A-Z]+)(?:\s+([^\]]+))?\]\s*(.*)', bq_text, re.DOTALL)
            if m:
                btype = m.group(1)
                blabel = m.group(2)
                bcontent = m.group(3).strip().replace("\n", " ")
                if btype == "TRACE":
                    label = blabel if blabel else "Trace"
                    flowables.append(_box(label, _inline(bcontent), TRACE_BG, TRACE_BDR))
                elif btype in BOX_MAP:
                    label, bg, bdr = BOX_MAP[btype]
                    flowables.append(_box(label, _inline(bcontent), bg, bdr))
                else:
                    flowables.append(Paragraph(_inline(bq_text), Bodyf))
            else:
                flowables.append(Paragraph(_inline(bq_text), Bodyf))
            flowables.append(_sp(4))
            continue

        # ── headings ──────────────────────────────────────────────────────────
        if line.startswith("### "):
            _flush_paragraph(para_buf, flowables)
            _flush_bullet(bullet_buf, flowables)
            flowables.append(Paragraph(_inline(line[4:]), H3st))
            i += 1
            continue
        if line.startswith("## "):
            _flush_paragraph(para_buf, flowables)
            _flush_bullet(bullet_buf, flowables)
            flowables.append(Paragraph(_inline(line[3:]), H2st))
            i += 1
            continue
        if line.startswith("# "):
            # Skip top-level heading — already emitted from frontmatter title
            i += 1
            continue

        # ── markdown table ────────────────────────────────────────────────────
        if line.startswith("|"):
            _flush_paragraph(para_buf, flowables)
            _flush_bullet(bullet_buf, flowables)
            tbl_lines = []
            while i < len(lines) and lines[i].startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            headers, rows = [], []
            for j, tl in enumerate(tbl_lines):
                cells = [c.strip() for c in tl.strip("|").split("|")]
                if j == 0:
                    headers = cells
                elif re.match(r'^[\s\-|:]+$', tl):
                    continue  # separator row
                else:
                    rows.append(cells)
            if headers:
                flowables.append(_make_table(headers, rows))
                flowables.append(_sp(4))
            continue

        # ── bullet list ───────────────────────────────────────────────────────
        if re.match(r'^[-*]\s', line):
            _flush_paragraph(para_buf, flowables)
            item_text = line[2:].strip()
            # Check for continuation lines
            i += 1
            while i < len(lines) and lines[i].startswith("  "):
                item_text += " " + lines[i].strip()
                i += 1
            flowables.append(Paragraph("&#8226;&#160;&#160;" + _inline(item_text), Bulf))
            continue

        # ── blank line ────────────────────────────────────────────────────────
        if line.strip() == "":
            _flush_paragraph(para_buf, flowables)
            i += 1
            continue

        # ── normal paragraph text ─────────────────────────────────────────────
        para_buf.append(line.strip())
        i += 1

    _flush_paragraph(para_buf, flowables)
    _flush_bullet(bullet_buf, flowables)
    return flowables

# ── Part configuration ────────────────────────────────────────────────────────
PARTS = {
    0:  (0, "Preface", "", ""),
    1:  (1, "The Orientation",
         "Why the field feels difficult, and the two lenses that make it navigable.",
         "Chapter 1: The Transparency Gap  \u2022  Chapter 2: The Three-Layer Map"),
    3:  (2, "Foundations: The Anatomy of a Transformation",
         "The vocabulary every architecture is built from.",
         "Chapters 3 \u2013 11"),
    12: (3, "The Framework",
         "The two analytical tools that unlock any architecture.",
         "Chapter 12: EIU Framework  \u2022  Chapter 13: The Structure Spectrum"),
    14: (4, "Architectures",
         "Applying the framework to the canonical families.",
         "Chapters 14 \u2013 21"),
    22: (5, "Systems and Scale",
         "How models grow, how knowledge transfers, and how computation executes.",
         "Chapters 22 \u2013 27"),
    28: (6, "Reference",
         "Tools for applying the framework, glossary, practice maps, and reading.",
         "Chapters 28 \u2013 31"),
}

# ── Cover page ────────────────────────────────────────────────────────────────
def _cover():
    cover = Table([
        [Paragraph("Neural Networks Dismantled", BookTitle)],
        [Paragraph("A Unified Framework for Semantics, Mathematics, and Execution", BookSub)],
        [_sp(6)],
        [Paragraph("Second Edition Draft \u2014 2026", BookEd)],
    ], colWidths=[W])
    cover.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), DARK),
        ("TOPPADDING",(0,0),(-1,-1), 20),
        ("BOTTOMPADDING",(0,0),(-1,-1), 20),
        ("LEFTPADDING",(0,0),(-1,-1), 30),
        ("RIGHTPADDING",(0,0),(-1,-1), 30),
    ]))
    promise_inner = Paragraph(
        "<b>Book Promise</b><br/>After reading this book, a beginner should be able to look at any "
        "unfamiliar neural-network architecture and ask the right questions: What are the entities? "
        "How do they interact? What trains them? How does hardware execute it? And \u2014 crucially "
        "\u2014 <i>why was it designed this way?</i>",
        S("PI", fontName="Helvetica", fontSize=9.5, leading=14, textColor=DARK))
    promise = Table([[promise_inner]], colWidths=[W])
    promise.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), MID_BG),
        ("BOX",(0,0),(-1,-1), 1.5, ACCENT),
        ("LEFTPADDING",(0,0),(-1,-1), 10),("RIGHTPADDING",(0,0),(-1,-1), 10),
        ("TOPPADDING",(0,0),(-1,-1), 7),("BOTTOMPADDING",(0,0),(-1,-1), 7),
    ]))
    return [Spacer(1, 0.9*inch), cover, _sp(22), promise, PageBreak()]

# ── TOC page ──────────────────────────────────────────────────────────────────
def _toc(chapter_meta):
    flowables = [Paragraph("Contents", H1st), _rule()]
    part_seen = set()
    for ch_num in sorted(chapter_meta.keys()):
        if ch_num in PARTS:
            pnum, ptitle, _, _ = PARTS[ch_num]
            if pnum > 0 and pnum not in part_seen:
                flowables.append(Paragraph(f"Part {pnum} \u2014 {ptitle}", TOCPt))
                part_seen.add(pnum)
        meta = chapter_meta[ch_num]
        title = meta.get("title", f"Chapter {ch_num}")
        flowables.append(Paragraph(
            f"<font color='#2563eb'><b>{ch_num}</b></font>&#160;&#160;{title}", TOCCh))
    flowables.append(PageBreak())
    return flowables

# ── Main build function ───────────────────────────────────────────────────────
def build(chapters_dir, output_path):
    # Discover and sort chapter files
    pattern = os.path.join(chapters_dir, "*.md")
    files = sorted(glob.glob(pattern))
    if not files:
        print(f"No markdown files found in {chapters_dir}")
        return

    # Parse all files
    chapter_data = {}  # ch_num -> (meta, body)
    for f in files:
        with open(f) as fh:
            text = fh.read()
        meta, body = parse_frontmatter(text)
        try:
            ch_num = int(meta.get("chapter", -1))
        except ValueError:
            continue
        if ch_num >= 0:
            chapter_data[ch_num] = (meta, body)

    chapter_meta = {k: v[0] for k, v in chapter_data.items()}

    # Build story
    story = []
    story.extend(_cover())
    story.extend(_toc(chapter_meta))

    for ch_num in sorted(chapter_data.keys()):
        meta, body = chapter_data[ch_num]
        title = meta.get("title", f"Chapter {ch_num}")

        # Inject part divider before first chapter of each part
        if ch_num in PARTS:
            pnum, ptitle, pdesc, pchlist = PARTS[ch_num]
            if pnum > 0:
                story.extend(_part_page(pnum, ptitle, pdesc, pchlist))

        # Convert chapter markdown to flowables
        flowables = markdown_to_flowables(body, ch_num, title)
        story.extend(flowables)
        story.append(PageBreak())

    # Build PDF
    doc = SimpleDocTemplate(output_path, pagesize=letter,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.75*inch,  bottomMargin=0.65*inch)
    doc.build(story, onFirstPage=_hf, onLaterPages=_hf)
    print(f"PDF written to: {output_path}")

# ── CLI ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build Neural Networks Dismantled PDF from markdown chapters.")
    parser.add_argument("--chapters", default="chapters", help="Directory containing chapter .md files (default: chapters/)")
    parser.add_argument("--output",   default="neural_networks_dismantled.pdf", help="Output PDF path (default: neural_networks_dismantled.pdf)")
    args = parser.parse_args()

    base = os.path.dirname(os.path.abspath(__file__))
    chapters_dir = os.path.join(base, args.chapters)
    output_path  = os.path.join(base, args.output)

    build(chapters_dir, output_path)
