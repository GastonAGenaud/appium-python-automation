from appium.webdriver.common.mobileby import MobileBy

from features.pages.base_page import Page


def compare_data_with_expected(expected, real):
    assert expected == real, "Expected '{}', but got '{}'".format(expected, real)


class MainPage(Page):
    MYWORKDOC_ICON_LIST = (MobileBy.CLASS_NAME, 'android.widget.ImageView')

    def verify_main_page_is_open(self):
        self.implicit_wait_visible(self.MYWORKDOC_ICON_LIST)
        user_icon_list = self.find_element(self.MYWORKDOC_ICON_LIST).is_displayed()
        return user_icon_list

