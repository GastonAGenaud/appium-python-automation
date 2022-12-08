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
        # compare_data_with_expected(expected=5, real=len(user_icon_list))
        # compare_data_with_expected(expected="Your Story", real=user_icon_list[0].text)
        #
        # tab_bar = self.find_element(self.TAB_BAR)
        # liner_tab = tab_bar.find_elements(self.LINER_BAR[0], self.LINER_BAR[1])
        #
        # compare_data_with_expected(expected=5, real=len(liner_tab))
        #
        # compare_data_with_expected(expected="Home", real=liner_tab[0].get_attribute("content-desc"))
        # compare_data_with_expected(expected="Search and Explore", real=liner_tab[1].get_attribute("content-desc"))
        # compare_data_with_expected(expected="Camera", real=liner_tab[2].get_attribute("content-desc"))
        # compare_data_with_expected(expected="Activity", real=liner_tab[3].get_attribute("content-desc"))
        # compare_data_with_expected(expected="Profile", real=liner_tab[4].get_attribute("content-desc"))
