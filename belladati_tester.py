from selenium import webdriver
from datetime import date
import logging, csv, sys, time
# logging.basicConfig(level= logging.INFO,
#                     filename= "scraper.log",
#                     format="format='%(asctime)s :: %(levelname)s :: %(name)s :: Line No %(lineno)d :: %(message)s")

driver = webdriver.Chrome(r'chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)

given_name = 'domain5'
given_pass = 'Interview01'
csv_file_path = "C:/Users/New_Admin/Desktop/Down X1/__@__Texty__@__/_Programovani ALL moje/Python All/_me_projekty/Belladati_task_all/road_safety_data.csv"

class WebScraper:

    """Open website, login """

    def __init__(self, instance_name, address_to_scrape):

        self.instance_name = instance_name

        self.webaddresss = address_to_scrape
        driver.get(self.webaddresss)


    def belladati_login(self, login_input, password_input):

        # login + pass
        self.login_field = driver.find_element_by_xpath('//*[@id="login"]')
        self.password_field = driver.find_element_by_xpath('//*[@id="password"]')
        self.login_btn  = driver.find_element_by_xpath('//*[@id="submit_0"]')

        self.login_field.send_keys(login_input)
        self.password_field.send_keys(password_input)
        self.login_btn.click()

        # click PopUpOK btn
        self.pop_up_ok_btn = driver.find_element_by_id('popupOk')
        self.pop_up_ok_btn.click()
        time.sleep(3)

    def belladati_import_dataset(self, dataset_name, csv_file_path):

        self.dataset_name = dataset_name
        self.csv_file_path = csv_file_path


        # click Import Your Data (+name it)
        self.import_your_data_btn = driver.find_element_by_xpath('//*[@id="howToBeginTable"]/tbody/tr[1]/th[3]')
        self.import_your_data_btn.click()
        self.start_import_btn = driver.find_element_by_xpath('//*[@id="begin1"]/p[1]/a')
        self.start_import_btn.click()
        time.sleep(3)
        self.name_field_btn = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/form/div[2]/div[1]/div[2]/table/tbody/tr[1]/td/input')
        self.name_field_btn.send_keys(dataset_name)
        time.sleep(3)
        driver.switch_to.frame(0)

        # Import the .csv file
        self.browse_btn = driver.find_element_by_id('uploadInput')
        self.browse_btn.send_keys(csv_file_path)
        # self.browse_btn.send_keys("road_safety_data.csv")
        time.sleep(3)
        driver.switch_to.default_content()

        self.continue_btn = driver.find_element_by_xpath("//input[@name='continue']")
        self.continue_btn.click()
        time.sleep(3)



def main():


    CZK_scraper = WebScraper('belladati_tester', 'https://service.belladati.com')
    CZK_scraper.belladati_login(given_name, given_pass)
    CZK_scraper.belladati_import_dataset("test_file_road_safety", csv_file_path)


if __name__ == "__main__":
    main()

    # driver.quit()                              # close all tabs, driver and console

