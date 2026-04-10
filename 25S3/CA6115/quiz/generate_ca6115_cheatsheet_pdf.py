from pathlib import Path
from html import escape
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak

BASE = Path(__file__).resolve().parent
SRC = BASE / 'CA6115_A4_CheatSheet_Source_v2.md'
OUT = BASE / 'CA6115_A4_CheatSheet.pdf'

PAGE_W, PAGE_H = A4
MARGIN = 3.9 * mm
TOP_SPACE = 4.8 * mm
BOTTOM_SPACE = 4.0 * mm
GUTTER = 1.4 * mm
COLS = 3
COL_W = (PAGE_W - 2 * MARGIN - (COLS - 1) * GUTTER) / COLS

frames = []
for i in range(COLS):
    x = MARGIN + i * (COL_W + GUTTER)
    frames.append(
        Frame(
            x,
            BOTTOM_SPACE,
            COL_W,
            PAGE_H - TOP_SPACE - BOTTOM_SPACE,
            leftPadding=0.45,
            rightPadding=0.45,
            topPadding=0.35,
            bottomPadding=0.35,
            id=f'col{i+1}',
            showBoundary=0,
        )
    )

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#d0d7e2'))
    canvas.setLineWidth(0.25)
    y0 = BOTTOM_SPACE
    y1 = PAGE_H - TOP_SPACE
    for i in range(1, COLS):
        x = MARGIN + i * COL_W + (i - 0.5) * GUTTER
        canvas.line(x, y0, x, y1)
    canvas.setFont('Helvetica', 5.2)
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 3.4 * mm, f'{doc.page}')
    canvas.restoreState()

styles = getSampleStyleSheet()
TITLE = ParagraphStyle(
    'CheatTitle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=11.1,
    leading=11.2, alignment=TA_CENTER, spaceAfter=0.75, textColor=colors.HexColor('#111111')
)
H2 = ParagraphStyle(
    'H2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=8.9,
    leading=9.0, spaceBefore=0.14, spaceAfter=0.1, textColor=colors.HexColor('#184e96')
)
BODY = ParagraphStyle(
    'Body', parent=styles['BodyText'], fontName='Helvetica', fontSize=7.35,
    leading=7.4, spaceBefore=0.0, spaceAfter=0.0, allowWidows=1, allowOrphans=1
)
BULLET = ParagraphStyle(
    'Bullet', parent=BODY, leftIndent=4.45, firstLineIndent=-2.35, bulletIndent=0,
)
SMALL = ParagraphStyle(
    'Small', parent=BODY, fontSize=7.1, leading=7.2
)


def fmt_inline(text: str) -> str:
    text = escape(text)
    parts = text.split('`')
    for i in range(len(parts)):
        if i % 2 == 1:
            parts[i] = f'<font name="Courier">{parts[i]}</font>'
        else:
            seg = parts[i]
            seg = re.sub(r'\[\[(.+?)\]\]', r'<font color="#b22222"><b>\1</b></font>', seg)
            seg = re.sub(r'\{\{(Ans.*?)\}\}', r'<font color="#1b7f3b"><b>\1</b></font>', seg, flags=re.I)
            seg = re.sub(r'\{\{(Q.*?)\}\}', r'<font color="#0f2f53"><b>\1</b></font>', seg, flags=re.I)
            seg = re.sub(r'\{\{(.+?)\}\}', r'<font color="#0f2f53"><b>\1</b></font>', seg)
            seg = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', seg)
            parts[i] = seg
    return ''.join(parts)

story = []
for raw_line in SRC.read_text(encoding='utf-8').splitlines():
    line = raw_line.strip()
    if not line:
        continue
    if line == '<!--PAGEBREAK-->':
        story.append(PageBreak())
        continue
    if line.startswith('# '):
        story.append(Paragraph(fmt_inline(line[2:]), TITLE))
        continue
    if line.startswith('## '):
        story.append(Paragraph(fmt_inline(line[3:]), H2))
        continue
    if line.startswith('- '):
        story.append(Paragraph(fmt_inline(line[2:]), BULLET, bulletText='•'))
        continue
    story.append(Paragraph(fmt_inline(line), SMALL))


doc = BaseDocTemplate(
    str(OUT),
    pagesize=A4,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
    topMargin=TOP_SPACE,
    bottomMargin=BOTTOM_SPACE,
    pageTemplates=[PageTemplate(id='ThreeCol', frames=frames, onPage=on_page)],
)

doc.build(story)
print(f'Created: {OUT}')
try:
    from pypdf import PdfReader
    pages = len(PdfReader(str(OUT)).pages)
    print(f'Pages: {pages}')
except Exception as exc:
    print(f'Page count unavailable: {exc}')
print(f'Size bytes: {OUT.stat().st_size}')
