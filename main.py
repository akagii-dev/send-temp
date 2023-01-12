import json
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

# URLを指定
url = 'URL'

user = 'USER_EMAIL'
pswd = 'USER_PASSWARD'
webhook = 'WEBHOOK_URL'

driver.get(url)
time.sleep(5)
# ユーザーIDとパスワードを入力
driver.find_element(By.ID, 'i0116').send_keys(user)
driver.find_element(By.ID, 'idSIButton9').click()
print('メールアドレスを入力した')
time.sleep(3)

driver.find_element(By.ID, 'i0118').send_keys(pswd)
driver.find_element(By.ID, 'idSIButton9').click()
print('パスワードを入力した')
time.sleep(3)

# ログイン情報を記録させるかどうか
driver.find_element(By.ID, 'idSIButton9').click()
print('はいを押した')
time.sleep(5)

# フォームに入力
driver.find_elements(By.XPATH, '//input[@value="36.0〜36.9"]')[0].click()
print('体温を選択')
driver.find_elements(By.CLASS_NAME, 'button-content')[1].click()
time.sleep(1)
print('送信')
driver.close()

# discordに通知するように設定する(webhook経由)
content = {'content': '検温は送信されました'}
headers = {'Content-Type': 'application/json'}
requests.post((webhook), data=json.dumps(content), headers=headers)