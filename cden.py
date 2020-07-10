from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from password import username, pw
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
class CodingForE():
    def __init__(self):
        self.driver = webdriver.Chrome(options = option )

    def login(self):
        
        sleep(2)
        self.driver.refresh()
        sleep(5)
        self.driver.get('https://www.codingforentrepreneurs.com/login/')
        print(self.driver.title)
        sleep(5)

        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[3]/form/div[1]/input').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[3]/form/div[2]/input').send_keys(pw)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[3]/form/p[1]/button').click()
        return True
        driver.maximize_window()
    def course(self):
        
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/ul[1]/a[2]').click()
        # actions = ActionChains(driver)
        # actions.move_to_element(course).click().perform()
        sleep(5) 
        
        self.driver.save_screenshot("screenshot1.png")
        sleep(5)
        
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/nav/div/span/ul/span[2]/li/a/span').click()
        
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/nav/div/span/ul/span[2]/li/div/a[2]').click()
        
        sleep(3)
        
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/p[2]/button[1]').click()
        sleep(5)
        
        
        self.driver.quit()
bot = CodingForE()
sleep(2)
login = bot.login()

if login:
    try:
        sleep(5)
        bot.course()
    except:
        print('Something went wrong!')