#load env
from dotenv import load_dotenv
load_dotenv()

import os
ACCOUNT = os.getenv('ACCOUNT')
PASSWD = os.getenv('PASSWD')

#main
from src.browser import Browser
import json
import time

browser = Browser()

browser.login(ACCOUNT, PASSWD)

time.sleep(2)

cookies = browser.get_cookies()

with open('./cookies.json', 'w+', encoding='utf-8') as jfile:
  jfile.write(json.dumps(cookies))
  
browser.quit()

print('ok')