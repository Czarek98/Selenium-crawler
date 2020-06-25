from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option('prefs',  {
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
    }
)

def test_testcrawler(number):

    driver = webdriver.Chrome(executable_path=r'C:\Users\Predator\Desktop\chromedriver_win32\chromedriver.exe', options = options)
    driver.get("https://www.bundestag.de/mediathek")
    driver.maximize_window()
    child =1
    while child < number:
        driver.find_element(By.CSS_SELECTOR, "#mediathek_442344 .bt-slide:nth-child({}) h3".format(child)).click()
        i = 1
        while i < 5:
            driver.execute_script("window.scrollTo(0,1000.5999755859375)")
            time.sleep(1)
            driver.find_element_by_css_selector(".icon-download").click()
            driver.find_element_by_css_selector("label:nth-child(8)").click()
            driver.find_element_by_css_selector(".download-continue").click()
            driver.find_element_by_css_selector(".icon-doc").click()
            driver.execute_script("window.scrollTo(0,1500.5999755859375)")
            time.sleep(1)
            if  i==4:
                time.sleep(1)
                driver.execute_script("window.scrollTo(0,1000.5999755859375)")
                driver.find_element(By.LINK_TEXT, "schließen").click()
                break


            driver.find_element(By.CSS_SELECTOR, ".bt-fixed .slick-next").click()
            i += 1
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,1200.5999755859375)")
        driver.find_element_by_xpath("//div[@id='mediathek_442344']/button[2]").click()
        time.sleep(1)
        child = child +4
        time.sleep(2)



test_testcrawler(50)