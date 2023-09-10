from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
doc = SimpleDocTemplate("patient_report.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

def create_patient_pdf(data_dict, photo_filename, pdf_filename):
    page=[]
    

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
    add_image(photo_filename)
    add_text(time.ctime())
    add_text(["""Disease Diagnosed: {}""".format(
    data_dict['Name'])])
    
    add_text(data_dict['prompt'])
    add_text(data_dict['Diagnosis'])

    # ===========================================================

    doc.build(page)

def create_qr_code_pdf(user_input, assistant_response, p_prompt):
    data_dict = {
        "Name": user_input,
        "prompt": p_prompt,
        "Diagnosis": assistant_response,
    }

    photo_filename = "uploaded_image.png"  # Provide the path to the student's photo
    pdf_filename = "patient_report.pdf"
    print('photo_filename', photo_filename)

    create_patient_pdf(data_dict, photo_filename, pdf_filename)
    file = print(f"PDF created: {pdf_filename}")

    pdf_file_path = pdf_filename
    curl_command = f'curl -X POST --data-binary "@{pdf_file_path}" --header "Content-Type: application/pdf" "https://www.filestackapi.com/api/store/S3?key=AyrO9dFikQqGulVwIp7TQz"'
    file_URL = os.popen(curl_command).read().strip()
    file_URL = file_URL.split('"')[3]
    print("Uploaded file URL:", str(file_URL))
    print(file)
    print(file_URL)
    return str(str(file_URL))
