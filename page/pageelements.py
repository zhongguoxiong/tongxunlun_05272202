from selenium.webdriver.common.by import By
class PageElements:
    newlianxirenbutton=(By.ID,"com.android.contacts:id/menu_add_contact")
    xingming_input=(By.XPATH,"//*[contains(@text,'姓名')]")
    phone_input=(By.XPATH,"//*[contains(@text,'电话号码')]")
    finish=(By.ID,"android:id/icon2")
    back=(By.ID,"com.android.contacts:id/backImg")

    user_text = (By.CLASS_NAME, "android.widget.TextView")