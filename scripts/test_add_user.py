import sys, os
import pytest, allure
sys.path.append(os.getcwd())

from base.init_driver import init_driver
from page.add_user_page import AddUserPage
from base.Read_Data import ret_yaml_data, return_yaml_data


def read_test_data():
    list_data = []
    test_Data = ret_yaml_data("add_user").get("User")
    for i in test_Data.keys():
        list_data.append((i, test_Data.get(i).get("name")
                          , test_Data.get(i).get("phone"),
                          test_Data.get(i).get("expect")))
    return list_data

def read_data():
    list_data=[]
    add_user_data=return_yaml_data("add_user").get("User")
    #{'test_user_001': {'name': '', 'phone': '', 'expect': ''}, 'test_user_002': {'name': 'x', 'phone': '', 'expect': 'x'}, 'test_user_003': {'name': '', 'phone': '1 348-883-4010',
    #'expect': '1 348-883-4010'}, 'test_user_004': {'name': 'xx', 'phone': '1 348-883-4010', 'expect': 'xx'}}
    for k in add_user_data.keys():
        list_data.append((k,add_user_data.get(k).get("name"),add_user_data.get(k).get("phone"),add_user_data.get(k).get("expect")))
    #[('test_user_001', '', '', ''), ('test_user_002', 'x', '', 'x'), ('test_user_003', '', '1 348-883-4010', '1 348-883-4010'), ('test_user_004', 'xx', '1 348-883-4010', 'xx')]

    return list_data

class Test_Add_User:
    def setup_class(self):
        self.driver=init_driver()
        self.addUserPageObj=AddUserPage(self.driver)

    def teardown_class(self):
        self.driver.quit()


    @pytest.fixture()
    def click_add_user_button(self):
        self.addUserPageObj.clickNewlianxirenButton()


    @pytest.mark.usefixtures("click_add_user_button")
    @pytest.mark.parametrize("test_num,name,phone,expect", read_data())
    def test_input_lianxiren_info(self,test_num,name,phone,expect):

        self.addUserPageObj.input_user_info(name, phone)
        if test_num == "test_user_001":
          assert expect not in self.addUserPageObj.get_user_list()
        else:
          assert expect in self.addUserPageObj.get_user_list()



