"""
This file contains test logic for Orange HRM automation
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


# importing other files
from TestLocator.locator import OrangeHRM_Locator
from TestData.data import Orange_HRM_Data
from Utilities.excel_functions import ExcelFunction

# import the webdriver wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from  selenium.common.exceptions import TimeoutException

#import time functionality
from time import sleep
from datetime import datetime


class TestHRM:

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    ignored_exceptions = [NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException, TimeoutException]
    wait = WebDriverWait(driver, 50, poll_frequency=5, ignored_exceptions= ignored_exceptions)
        

# Logic to open to browser and maximizing the window
    def url_check(self):
              
        self.driver.get(Orange_HRM_Data().url)
        self.driver.maximize_window()
        login_url = self.driver.current_url
        return(login_url)
    
    # Logic to check the username visibility used is_displayed method
    def username_visibility(self):
        try:
            is_present = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locator().username_locator)))
            print("True")  # Element is present
            return True
        except TimeoutException:
            print("False")  # Element is not present
            return False

    # Logic to check the password visibility used is_displayed method
    def password_visibility(self):
        try:
            is_present = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locator().password_locator)))
            print("True")  # Element is present
            return True
        except TimeoutException:
            print("False")  # Element is not present
            return False
   
   # Logic to login into th webpage
    def login(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locator.username_locator))).send_keys(Orange_HRM_Data.username)
        print("Username")
        self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locator.password_locator))).send_keys(Orange_HRM_Data.password)
        print("Password")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locator.login_locator))).click()
        print("Logged In")

    # Logic to logot from th webpage
    def logout(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locator.profile_icon_locator))).click()
        print("profile_icon")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locator.logout_locator))).click()
        print("logout")
        self.driver.refresh()

    # Logic to check the dashboard items are displayed correctly. collected all the items using while loop and combined the data into a list.
    # This function returns the list of dashboard items
    def Admin_visibility(self):
        dashboard_icon_texts =[]
        self.login()
        sleep(10)
        index = 1
        while index <= 12:
            try:
            # Dynamically update the XPath with the index
                element = self.driver.find_element(By.XPATH, f"(//div[@class='oxd-sidepanel-body']//li)[{index}]")
                dashboard_icon_texts.append(element.text)
                index += 1  # Increment index
            except:
                print("No more elements found.")
        print(dashboard_icon_texts)
        self.logout()
        return dashboard_icon_texts
    
        
    # New user is added in the HRM portal with this logic. 
    # This function returns the "Personal details" text to verify whether the new user is added or not 
    def Adding_new_user(self):
        self.login()
        # Clicks the PIM icon
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[(text()='PIM')]"))).click()
        adding_NewUser_url = self.driver.current_url
        print("Admin icon clicked")
        # Checks whether it opens PIM page
        if adding_NewUser_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList':
            print("URL verified")
            sleep(10)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='orangehrm-header-container']/button"))).click()
            print("Adding New user")
            savingNewUser_url = self.driver.current_url
            # Checks whether it moves to adding user page
            if savingNewUser_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee':
                print("Saving URL verified")
                sleep(10)
                # Adding new user
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='firstName']"))).send_keys("Anna")
                print('firstname')
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='lastName']"))).send_keys("Hathway")
                print('last name')
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
                print('new user saved')
                sleep(10)
                newUser_verification = self.driver.find_element(by=By.XPATH, value = "//h6[(text()='Personal Details')]").text
                print (newUser_verification)
                return newUser_verification
            else:
                # self.logout()
                return False
        else:
            # self.logout()
            return False


    #This method checks whether added new user is present in the portal or not.
    #This funtion returns "Employye search table with result"
    def verifiying_newUser(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[(text()='PIM')]"))).click() # moves back to PIM page using PIM icon click
        Back_to_PIM = self.driver.current_url
        # Checks whether it moves to PIM page or not
        if Back_to_PIM == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList':
            print("PIM icon clicked")
            # typing the employee name
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Type for hints...'])[1]"))).send_keys("Anna Hathway")
            print("TYped employee name")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
            print("Clicked search icon")
            sleep(5)
            #locating the search found element
            emp_search_text = self.driver.find_element(By.XPATH, "(//div[@class='oxd-table-cell oxd-padding-cell']/div)[3]").text
            print(emp_search_text)
            self.logout()
            return emp_search_text

    # This functions check the login using cookies.
    # Function returns domain of the given URL 
    def login_check_with_cokkie(self):
        self.login()
        Orange_HRM_cookie = self.driver.get_cookie('orangehrm')  #getting cookie with cookie_name
        # print(Orange_HRM_cookie)
        if Orange_HRM_cookie['name'] == 'orangehrm': #checks the cookie
            print(Orange_HRM_cookie['domain'])
            # return Orange_HRM_cookie['domain']
        sleep(10)
        
        self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locator.profile_icon_locator))).click()
        print("profile_icon")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locator.logout_locator))).click()
        print("logout")
        self.driver.refresh()
        return (Orange_HRM_cookie['domain'])

    # This functions check the login using multiple data present in excel. 
    # Function is constructed using DDT framework
    def loginExcel(self):

        self.excel_file = Orange_HRM_Data().excel_file
        self.sheet_number = Orange_HRM_Data().sheet_number
        self.excel = ExcelFunction(self.excel_file, self.sheet_number)

        # Get the current date and time
        current_datetime = datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()

        self.row = self.excel.row_count()

        for row in range(2,self.row+1):
            username = self.excel.read_data(row, 5)
            password = self.excel.read_data(row, 6)
            
            self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locator.username_locator))).send_keys(username)
            print("username")
            self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locator.password_locator))).send_keys(password)
            print("password")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locator.login_locator))).click()
            print("Logged in")
           
            if Orange_HRM_Data().dashboard_url in self.driver.current_url:
                
                self.excel.write_data(row,4,current_date)
                self.excel.write_data(row,7,'Test Passed')
                self.excel.write_data(row,8, current_time)
                # self.driver.back()
                # sleep(5)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locator.profile_icon_locator))).click()
                print("profile_icon")
                self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locator.logout_locator))).click()
                print("logout")
                self.driver.refresh()
                
                    
            elif Orange_HRM_Data().url in self.driver.current_url:
                print("FAILED")
                self.excel.write_data(row,4,current_date)
                self.excel.write_data(row,7,'Test Failed')
                self.excel.write_data(row,8, current_time)
                self.driver.refresh()
                # sleep(5)
        return 'Printed'
    

        
    # Finally quitting the browser
    def shutdown(self):
        self.driver.quit()
        return True