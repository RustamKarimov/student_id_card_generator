from packages import data_readers as dr
from packages import pdf_proccessors as pp


def create_student_cards():
    """
    Creates id cards for all of the learners
    :return: None
    """
    data = dr.get_data_file()  # gets the list of the learner info
    for index, learner in data.head(3).iterrows():  # iterates over each learner
        template = pp.get_template_pdf()  # gets template card
        pp.create_student_card(learner, template)  # create card for specific learner


if __name__ == '__main__':
    create_student_cards()  # create id cards for all the learners
