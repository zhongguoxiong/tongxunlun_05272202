from selenium.webdriver.support.wait import WebDriverWait
import sys, os

from base.init_driver import init_driver
from page.pageelements import PageElements

sys.path.append(os.getcwd())
class BaseAction:
    def __init__(self,driver):
        self.driver=driver
    def find_element_o(self,loc):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*loc))

    def find_elements_o(self,loc):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_elements(*loc))

    def click_element(self,loc):
        element_o=self.find_element_o(loc)
        element_o.click()

    def input_text(self,loc,text):
        element_o = self.find_element_o(loc)
        element_o.clear()
        element_o.send_keys(text)


    def if_disp(self,loc):
        try:
            self.find_element_o(loc)
            return  True
        except Exception as  e:
            return  False

    def get_userlist(self):
        user_data=self.find_elements_o(PageElements.user_text)
        return [i.text for i in user_data]

if __name__ == '__main__':
    driver=init_driver()
    baseActionObj=BaseAction(driver)
    baseActionObj.click_element(PageElements.newlianxirenbutton)
    baseActionObj.input_text(PageElements.xingming_input,"政治")
    baseActionObj.input_text(PageElements.phone_input, "13833333333")
    baseActionObj.click_element(PageElements.finish)
    if baseActionObj.if_disp(PageElements.back):
        baseActionObj.click_element(PageElements.back)
    print(baseActionObj.get_userlist())