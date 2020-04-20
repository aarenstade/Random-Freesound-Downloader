from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path='/path/to/chromedriver')
driver.set_page_load_timeout(10)
driver.get('http://freesound.org')

time.sleep(2)

login = driver.find_element_by_xpath("/html/body/div[1]/div[1]/a[2]")
login.click()

username = 'YOUR FREESOUND USERNAME'
loginfield = driver.find_element_by_xpath("//*[@id='id_username']")
loginfield.clear()
loginfield.send_keys(username)

password = 'YOUR FREESOUND PASSWORD'
passwordfield = driver.find_element_by_xpath("//*[@id='id_password']")
passwordfield.clear()
passwordfield.send_keys(password)

loginbutton = driver.find_element_by_xpath(
    "//*[@id='content_full']/form/input[2]")
loginbutton.click()

time.sleep(2)

soundsbutton = driver.find_element_by_xpath("/html/body/div[1]/ul/li[2]/a")
soundsbutton.click()

randomsoundbutton = driver.find_element_by_xpath(
    "/html/body/div[2]/div/div/div[2]/div[1]/ul/li[6]/b/a")
randomsoundbutton.click()
acceptcookies = driver.find_element_by_xpath(
    "/html/body/div[3]/div/div[1]/div[2]/button")
acceptcookies.click()

for i in range(10):
    downloadbutton = driver.find_element_by_xpath("//*[@id='download_button']")
    downloadbutton.click()
    time.sleep(2)

    try:
        closewindow = driver.find_element_by_xpath(
            "/html/body/div[4]/div/div[1]/span")
        closewindow.click()
    except:
        print("no closewindow button")

    randombutton = driver.find_element_by_xpath(
        "/html/body/div[2]/div/div/div[4]/ul/li[1]/a")
    randombutton.click()
    time.sleep(1)
