from Utilities.OrangeHRM_automation import TestHRM

# To verify thye URL
def test_urlCheck(): #test 1
    assert TestHRM().url_check() == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    print("Test Passed, Url Verified")

# To verify thye username text box visibility
def test_usernameVisibiliy():  #test 2
    assert TestHRM().username_visibility() == True
    print("Test Passed, Username visibility Checked")

# To verify thye password text box visibility
def test_passwordVisibiliy(): #test 3
    assert TestHRM().password_visibility() == True
    print("Test Passed, Password visibility Checked")
    TestHRM().Admin_visibility()

# To verify thye dashboard icon visibility
def test_admimVisibiliy(): #test 4
    expected_list = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Claim', 'Buzz']
    assert TestHRM().Admin_visibility() == expected_list
    print("Test Passed, dashboard icons' visibility Checked")

# To verify that new user can be added or not 
def test_Adding_newUser(): #test 5
    assert TestHRM().Adding_new_user() == "Personal Details"
    print("Test Passed, New user added")

# To verify that new user can be searched
def test_search_newUser(): #test 6
    assert TestHRM().verifiying_newUser() == "Anna"
    print("Test passed, new user added")
    
# To verify that login with cookies
def test_loginCheck_cookie(): #test 7
    assert TestHRM().login_check_with_cokkie() == 'opensource-demo.orangehrmlive.com'
    print("Test Passed! Cookie verified")

# To verify that login with DDT framework
def test_LoginwithExcel(): #test 8
    assert TestHRM().loginExcel() == 'Printed'
    print("Test Passed, Login Verified")

# Finally shutting down the browser
def test_shutdown(): #test 9
    assert TestHRM().shutdown() == True
    print("Test Passed! Automation completed")

