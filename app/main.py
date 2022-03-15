import os

from flask import Flask
from fake_useragent import UserAgent
from selenium import webdriver

app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>Hello, Flask!</h1>"

@app.route("/a")
def crawler():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('user-agent='+UserAgent().random)
    chrome_options.binary_location = "/drivers/headless-chromium"
    driver = webdriver.Chrome("/drivers/chromedriver", chrome_options=chrome_options)

    driver.get('https://en.wikipedia.org/wiki/Special:Random')
    line = driver.find_element_by_class_name('firstHeading').text
    print(line)
    driver.quit()
    return line

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)