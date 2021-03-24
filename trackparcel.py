import requests
import asyncio 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
import pickle 
import time


class ParcelTrack:


    def __init__(self):
        self.opt = Options()
        self.opt.add_argument("--headless")
        self.driver = webdriver.Firefox()
        self.url = "https://gdeposylka.ru/"

    def FoundField(self,id):
        self.driver.get(self.url)
        send = self.driver.find_element(By.XPATH, '//*[@id="tracking_form_tracking_number"]')
        send.send_keys(str(id) + Keys.RETURN)   
        print(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fragment-checkpoints"]/ul/li[1]/span[3]/strong'))).text)
        print("this  is it")
        self.driver.quit()