import os

from reportlab.lib.units import mm

# __file__ => gets current file
# os.pardir => system independent function for ../
# os.path.join => gets the parent directory
# os.path.abspath => gets absolute path of a file
BASE_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))

IMAGES_DIR = os.path.join(BASE_DIR, 'images')
QR_IMAGE_PATH = os.path.join(IMAGES_DIR, 'qr_image.png')

# the directory containing templates
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
# filename of a template
TEMPLATE_FILE_NAME = 'student_card.pdf'
# path to a template file
TEMPLATE_FILE_PATH = os.path.join(TEMPLATES_DIR, TEMPLATE_FILE_NAME)

# the directory containing data files
DATA_DIR = os.path.join(BASE_DIR, 'data')
# the file name of a data file
DATA_FILE_NAME = 'student_list.xlsx'
# path to a data file
DATA_FILE_PATH = os.path.join(DATA_DIR, DATA_FILE_NAME)

FIELDS = {
    'ID': 'School ID',
    'NAME': 'Name',
    'SURNAME': 'Surname',
    'GENDER': 'Gender',
    'DATE': 'Date of Birth',
    'GRADE': 'Grade'
}

POSITIONS = {
    'ID': (41*mm, 41.18*mm),
    'NAME': (38*mm, 35.3*mm),
    'SURNAME': (41*mm, 29.41*mm),
    'GENDER': (40*mm, 23.70*mm),
    'DATE': (44*mm, 17.8*mm),
    'IMAGE': (3.2*mm, 17.3*mm),
    'QR': (65*mm, 5*mm)
}

PAGE_WIDTH = 85.59*mm
PAGE_HEIGHT = 53.98*mm
PAGESIZE = (PAGE_WIDTH, PAGE_HEIGHT)

IMAGE_WIDTH = 25.9*mm
IMAGE_HEIGHT = 25.9*mm

FONT = 'Calibri'
FONT_SIZE = 6

FONT_COLOR = (0, 0, 0)