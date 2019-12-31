from selenium import webdriver
browser = webdriver.Chrome('')  #path of chromedriver
browser.get('https://www.codechef.com/submit/ISHVALA/')
username = browser.find_element_by_name('name')
password = browser.find_element_by_name('pass')
username.send_keys('')  #username
password.send_keys('')  #password
login = browser.find_element_by_name('op')
login.submit()
openfile = browser.find_element_by_xpath('//*[@id="ember345"]/div/div[1]/button')
openfile.send_keys('‪')  #path of the file
submit = browser.find_element_by_xpath('//*[@id="ember345"]/div/div[1]/div[2]/div/button')
submit.click()
