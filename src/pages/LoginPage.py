import random

from appium.webdriver.common.mobileby import MobileBy

from functions.Functions import Functions


# ELEMENTS NOMENCLATURE REFERENCE
# LABEL = LBL
# BUTTONS = BTN
# CHECK_BUTTON = CHK
# OPTION_BUTTON = OPT
# DROPDOWN = DPW

class Login(object):
    title_lbl = (MobileBy.ID, 'marcostudios.Login:id/imageView')
    phone_txt = (MobileBy.ID, '00000000-0000-0009-ffff-ffff00000041')
    password_txt = (MobileBy.ID, '00000000-0000-001e-ffff-ffff00000061')
    login_btn = (MobileBy.ID, '00000000-0000-0009-ffff-ffff00000046')
    questions_lbl = (MobileBy.ID, 'marcostudios.Login:id/question')
    answer_one_btn = (MobileBy.ID, 'marcostudios.Login:id/answerone')
    answer_two_btn = (MobileBy.ID, 'marcostudios.Login:id/answertwo')
    answer_three_btn = (MobileBy.ID, 'marcostudios.Login:id/answerthree')
    progress_lbl = (MobileBy.ID, 'marcostudios.Login:id/progress')

    def set_players(self, name1, name2):
        Functions.implicit_wait_visible(self, Login.title_lbl)
        Functions.setText(self, Login.yourName_txt, name1)
        Functions.setText(self, Login.herName_txt, name2)
        Functions.click_element(self, Login.login_btn)

    def set_answers(self, number):
        progress = 1
        for progress in range(number):
            Functions.implicit_wait_visible(self, Login.questions_lbl)
            answers = [Login.answer_one_btn,
                       Login.answer_two_btn,
                       Login.answer_three_btn]
            answer = random.choice(answers)
            Functions.click_element(self, answer)
            Functions.implicit_wait_visible(self, Login.progress_lbl)
            #assert Functions.get_element_text(self, Login.progress_lbl) == f"{str(progress)}/10", "This is not the step"
            ++progress