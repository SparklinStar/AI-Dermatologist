import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
import os


page=[]
magName = "Pythonista"
issueNum = 12
subPrice = "99.00"
limitedDate = "03/05/2010"
freeGift = "tin foil hat"

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))


def add_image(img):
    im = Image(img, 2*inch, 2*inch)
    page.append(im)


def add_space():
    page.append(Spacer(1, 12))


def add_text(text, space=0):
    if type(text)==list:
        for f in text:
            add_text(f)
    else:
        ptext = f'<font size="12">{text}</font>'
        page.append(Paragraph(ptext, styles["Normal"]))
        if space==1:
            add_space()
        add_space()


# =============================== The content =======================
# ============================== of the document ====================
add_image("uploaded_image.png")
add_text(time.ctime())
add_text([
"""Giovanni Gatto
Via Leonardo Da Vinci""".splitlines()])


add_text(["""We would like to welcome
you to our subscriber base for {} Magazine!
You will receive {} issues at the excellent
introductory price of ${}.
Please respond by
{} to start receiving 
your subscription and get the
following free gift: {}.""".format(
    magName,
    issueNum,
    subPrice,
    limitedDate,
    freeGift),
    "Thank you very much and we look forward to serving you.",
])

# ===========================================================

doc.build(page)

