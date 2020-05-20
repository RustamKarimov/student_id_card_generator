import os

# os.getcwd => gets current directory
# os.pardir => system independent function for ../
# os.path.join => gets the parent directory
# os.path.abspath => gets absolute path of a file
BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

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

ID_FIELD = ''
NAME_FIELD = ''
SURNAME_FIELD = ''
GENDER_FIELD = ''
DATE_FIELD = ''
GRADE_FIELD = ''