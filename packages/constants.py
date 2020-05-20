import os

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATE_FILE_NAME = 'student_card.pdf'
TEMPLATE_FILE_PATH = os.path.join(TEMPLATES_DIR, TEMPLATE_FILE_NAME)

DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_FILE_NAME = 'student_list.xlsx'
DATA_FILE_PATH = os.path.join(DATA_DIR, DATA_FILE_NAME)

ID_FIELD = ''
NAME_FIELD = ''
SURNAME_FIELD = ''
GENDER_FIELD = ''
DATE_FIELD = ''
GRADE_FIELD = ''