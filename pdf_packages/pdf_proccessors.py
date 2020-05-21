import io
import os
import pyqrcode  # pypng module also must be installed

from PyPDF2 import PdfFileReader, PdfFileWriter

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from .constants import TEMPLATE_FILE_PATH, IMAGES_DIR, QR_IMAGE_PATH
from .constants import FIELDS, PAGESIZE, POSITIONS, IMAGE_HEIGHT, IMAGE_WIDTH
from .constants import FONT, FONT_SIZE, FONT_COLOR


def get_template_pdf(template=TEMPLATE_FILE_PATH):
    """:returns template pdf for id card"""
    return PdfFileReader(open(TEMPLATE_FILE_PATH, "rb"))


def get_canvas(packet):
    can = canvas.Canvas(packet, pagesize=PAGESIZE)

    can.setFont(FONT, FONT_SIZE)
    can.setFillColor(FONT_COLOR)

    return can


def get_qr_code(school_id, name, surname):
    data = f"{school_id} - {name} {surname.upper()}"
    qr_image = pyqrcode.create(data)
    qr_image.png(QR_IMAGE_PATH)


def write_info_on_canvas(can, learner):
    school_id = learner[FIELDS['ID']]
    name = learner[FIELDS['NAME']]
    surname = learner[FIELDS['SURNAME']]
    gender = learner[FIELDS['GENDER']]
    dob = learner[FIELDS['DATE']]
    image_file = f"{school_id}.png"
    image_file_path = os.path.join(IMAGES_DIR, image_file)

    can.drawString(*POSITIONS['ID'], school_id)
    can.drawString(*POSITIONS['NAME'], name)
    can.drawString(*POSITIONS['SURNAME'], surname)
    can.drawString(*POSITIONS['GENDER'], gender)
    can.drawString(*POSITIONS['DATE'], dob)
    if os.path.exists(image_file_path):
        can.drawImage(image_file_path, *POSITIONS['IMAGE'], IMAGE_WIDTH, IMAGE_WIDTH)

    get_qr_code(school_id, name, surname)
    can.drawImage(QR_IMAGE_PATH, *POSITIONS['QR'])


def create_info_pdf(learner):
    packet = io.BytesIO()

    can = get_canvas(packet)
    write_info_on_canvas(can, learner)
    can.save()

    packet.seek(0)

    return PdfFileReader(packet)


def create_pdf_file(template, info_pdf, learner):
    """
    Merges template card and card with info and creates new id card.
    File name of the new id card is the id of the learner.
    :param template: template for id card
    :param info_pdf: card of same size with template with learner info
    :param learner: learner for whom id card is being created
    :return: None
    """
    output = PdfFileWriter()  # container for new id card

    page = template.getPage(0)  # get first page of the template
    page.mergePage(info_pdf.getPage(0))  # merge it with first page of info card
    output.addPage(page)  # add the merged page into container

    page = template.getPage(1)  # get second page of the template
    output.addPage(page)  # add it to the container

    file_name = f"{learner[FIELDS['ID']]}.pdf"  # name of new id card consists of id of the learner
    with open(file_name, 'wb') as file:  # open new file to write information
        output.write(file)  # write contents of the container into new file


def create_student_card(learner, template):
    """
    Creates a student id card for the learner by using the template card
    :param learner: learner for whom card will be created for
    :param template: template to be used for id card
    :return: None
    """
    info_pdf = create_info_pdf(learner)  # creates a pdf file with learner info
    
    create_pdf_file(template, info_pdf, learner)  # creates pdf id card


pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))
