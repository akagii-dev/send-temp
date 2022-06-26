import json
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

# URLを指定
url = 'https://login.microsoftonline.com/common/oauth2/authorize?client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&resource=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3DeyJ2ZXJzaW9uIjoxLCJkYXRhIjp7IklkZW50aXR5UHJvdmlkZXIiOiJBWjVjZXI4WDRWY0ZhMG1kLWo5YnFmazFtcllvLWo4M3M3NVBTZDJHalAzc1Z1Q3Qxc0s4UE5CeTF6TF9lRXpjcTFOX2hsUmxCSFMxc2JWMGN6eHVMZW8iLCIucmVkaXJlY3QiOiJodHRwczovL2Zvcm1zLm9mZmljZS5jb20vUGFnZXMvUmVzcG9uc2VQYWdlLmFzcHg_aWQ9TXBGOU9WZE50MFdKSWxsTmZqWV82X1pMemxnZ2UweEVwWHJRcEh5clVPOVVSVlJTVURjMldGRlFXVUpNVlU5Vk5EZFFSVlJJUWpCSVdTNHUmc2lkPWE5OWUwYWMyLTY5ZjctNGNhNS1hODE2LThlYTVlYjhkY2Y4YSJ9fQ&response_mode=form_post&nonce=637910755195240468.MzcwNzVjMmUtN2ZiMS00MjNhLTk1YjYtNTE2NTFmNTc5NzZkZDk5OThjMmMtZTc0MC00MGJjLTgzYjUtY2IxMDNjZDQ2MTBi&redirect_uri=https%3A%2F%2Fforms.office.com%2Flanding&msafed=0&x-client-SKU=ID_NET472&x-client-ver=6.15.1.0'

def func(mail, psw, webhook_url):
    driver.get(url)
    print('urlを開いた')
    time.sleep(5)
    # ユーザーIDとパスワードを入力
    driver.find_element_by_id("i0116").send_keys(mail)
    driver.find_element_by_id("idSIButton9").click()
    print('メールアドレスを入力した')
    time.sleep(3)

    driver.find_element_by_id("i0118").send_keys(psw)
    driver.find_element_by_id("idSIButton9").click()
    print('パスワードを入力した')
    time.sleep(3)

    # ログイン情報を記録させるかどうか
    driver.find_element_by_id("idSIButton9").click()
    print('はいを押した')
    time.sleep(5)

    # フォームに入力
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div/label/input").click()
    print('体温を選択')
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[4]/div[1]/button/div").click()
    print('送信')

    driver.close()

    # discordに通知するように設定する(webhook経由)
    content = {'content': '検温は送信されました'}
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, data=json.dumps(content), headers=headers)

func("mail", "psw", "webhook_url")