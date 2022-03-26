import json
import requests
from pydoc import cli
from this import d
import time
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ユーザーID, パスワードを指定
user_id = 'your mail address'
user_pass = 'your account password'

# chromedriverのPATHを指定
driver_path = '/app/.chromedriver/bin/chromedriver'
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(options=options, executable_path=driver_path)
# URLを指定
url = 'https://login.microsoftonline.com/common/oauth2/authorize?client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&resource=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3DeyJ2ZXJzaW9uIjoxLCJkYXRhIjp7IklkZW50aXR5UHJvdmlkZXIiOiJBVGJLMUNxZWFvODlmdkprZENFN2xjdW5ITzdyeFVXQW1teEU0NDNTQUdsc1lrM2RiV3V0UjBjRzEtRUc3OFNqMXRGaVh2Wnd1QXM0cDE5Mm95N0c1RHciLCIucmVkaXJlY3QiOiJodHRwczovL2Zvcm1zLm9mZmljZS5jb20vUGFnZXMvUmVzcG9uc2VQYWdlLmFzcHg_aWQ9TXBGOU9WZE50MFdKSWxsTmZqWV82X1pMemxnZ2UweEVwWHJRcEh5clVPOVVSVlJTVURjMldGRlFXVUpNVlU5Vk5EZFFSVlJJUWpCSVdTNHUmc2lkPTA1Y2QwM2U4LWEwZjktNDdhMi1hZjQ2LTljMWI5MjgxNjdiOCJ9fQ&response_mode=form_post&nonce=637800136823934510.OWZjYjE1OTUtNmZlMS00OWI1LWI1ZjEtMzE3MDhjYzYyMDA5N2YxNzVjYzQtNjU0My00ZjhmLWJjZDktMDcxYjY2MzU5ZDQ4&redirect_uri=https%3A%2F%2Fforms.office.com%2Flanding&msafed=0&x-client-SKU=ID_NET472&x-client-ver=6.14.1.0&sso_reload=true'
# URLを開く
driver.get(url)
print('urlを開いた')
# ユーザーIDとパスワードを入力
element = driver.find_element_by_css_selector('#i0116')
element.send_keys(user_id)
time.sleep(3)
element = driver.find_element_by_css_selector('#idSIButton9')
element.click()
time.sleep(3)
print('メールアドレスを入力した')
element = driver.find_element_by_css_selector('#i0118')
element.send_keys(user_pass)
time.sleep(3)
element = driver.find_element_by_css_selector('#idSIButton9')
element.click()
time.sleep(5)
print('パスワードを入力した')
# ログイン情報を記録させるかどうか
element = driver.find_element_by_css_selector('#idSIButton9')
element.click()
time.sleep(5)
print('はいを押した')

# フォームに入力
element = driver.find_element_by_xpath(
    '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/label/input')
element.click()
print('体温を選択')
element = driver.find_element_by_xpath(
    '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[4]/div[1]/button/div')
element.click()
print('送信')

# 終了
driver.close()
print('成功')

# discordに通知するように設定する(webhook経由)

wenhook_url = 'discordのwebhookのurl'
main_content = {'content': '検温は送信されました'}
headers = {'Content-Type': 'application/json'}

response = requests.post(
    wenhook_url, data=json.dumps(main_content), headers=headers)
