from packages import data_readers as dr
from packages import constants as cn
from packages import pdf_proccessors as pp


def create_student_cards():
    data = dr.get_data_file()
    for learner in data.iterrows():
        pp.create_student_card(learner)


if __name__ == '__main__':
    create_student_cards()