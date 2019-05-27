from base.baseaction import BaseAction
#from base.init_driver import init_driver
from page.pageelements import PageElements
import sys, os
sys.path.append(os.getcwd())
class AddUserPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    def clickNewlianxirenButton(self):
        self.click_element(PageElements.newlianxirenbutton)


    def input_user_info(self,username,phone):
        self.input_text(PageElements.xingming_input,username)
        self.input_text(PageElements.phone_input,phone)
        self.click_element(PageElements.finish)
        if self.if_disp(PageElements.back):
           self.click_element(PageElements.back)



    def get_user_list(self):
       user_data= self.find_elements_o(PageElements.user_text)
       return [i.text for i in user_data]

#if __name__ == '__main__':
    #driver=init_driver()
    #baseActionObj=AddUserPage(driver)
    #baseActionObj.click_element(PageElements.newlianxirenbutton)
    #baseActionObj.input_user_info("里皮","13222222222")
    #print(baseActionObj.get_userlist())