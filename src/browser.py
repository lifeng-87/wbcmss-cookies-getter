from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class Browser(Chrome):
  options = Options()
  options.add_argument("--disable-notifications")
  options.add_argument('--ignore-certificate-errors-spki-list')
  options.add_argument('--ignore-ssl-errors')
  options.add_argument('log-level=3')
  options.add_argument('--headless')
  
  def __init__(self) -> None:
    
    super().__init__(options=self.options)
    
  def login(self, account:str, passwd:str):
    self.get("https://nmsd.ncut.edu.tw/wbcmss/Auth/Login")
    
    time.sleep(2)
    
    account_input = self.find_element(By.ID, 'Account')
    passwd_input = self.find_element(By.ID, 'Password')
    login_btn = self.find_element(By.XPATH, '//*[@id="signupform"]/fieldset/section/div[3]/div/button[1]')
    
    account_input.send_keys(account)
    passwd_input.send_keys(passwd)
    
    login_btn.click()
    
  