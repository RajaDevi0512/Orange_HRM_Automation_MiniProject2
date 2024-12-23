"""
This file contains locator that are used in automation
"""

class OrangeHRM_Locator:
    username_locator = "//input[@name='username']" # XPATH
    password_locator = "//input[@name='password']" # XPATH
    login_locator = '//div[@class="oxd-form-actions orangehrm-login-action"]/button' #ID
    profile_icon_locator = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i' #"//div[@class='oxd-topbar-header-userarea']/ul/li/span/i" #XPATH
    logout_locator =  '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a' #"//li[@class= '--active oxd-userdropdown']/ul/li[4]/a" #XPATH

    dashboard_item_locator = "//div[@class='oxd-sidepanel-body']//li[a][1]"