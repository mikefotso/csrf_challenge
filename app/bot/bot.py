from selenium import webdriver

def bot_run():
    print('in bot!')
    print('in run bot!')
    driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")
    driver.set_window_size(1120, 550)
    print('anything')
    driver.get("http://0.0.0.0:8000/login")
    driver.save_screenshot('login_page.png')
    print('anything1')
    driver.find_element_by_id("username").send_keys("mholloway")
    print('anything2')
    driver.find_element_by_id("password").send_keys("C@ntg3tme!n")
    print('anything3')
    driver.find_element_by_id("submit").click()
    print('anything4')
    driver.save_screenshot('on_dashboard.png')
    driver.get("http://0.0.0.0:8000/unread_messages")
    print('anything5')
    driver.save_screenshot('reading_messages.png')
    print('anything6')
    driver.get("http://0.0.0.0:8000/logout")
    driver.save_screenshot('going_baccdk_to_login.png')
    driver.quit()
bot_run()
