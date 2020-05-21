import io

from .constants import TEMPLATE_FILE_PATH
from .constants import FIELDS


def get_template_pdf(template=TEMPLATE_FILE_PATH):
    pass


def create_info_pdf(learner):
    pass


def create_pdf_file(template, info_pdf):
    pass


def create_student_card(learner, template):
    info_pdf = create_info_pdf(learner)
    
    create_pdf_file(template, info_pdf)
