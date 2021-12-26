import os.path
import time
from urllib.parse import urlparse

import requests

from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

s = Service(executable_path="./drivers/geckodriver")
browser = webdriver.Firefox(service=s)

url = "https://www.instagram.com"
browser.get(url)

time.sleep(4)
username_el = browser.find_element_by_name("username")
username_el.send_keys(INSTA_USERNAME)

password_el = browser.find_element_by_name("password")
password_el.send_keys(INSTA_PASSWORD)

time.sleep(1.5)
submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
submit_btn_el.click()

body_el = browser.find_element_by_css_selector("body")
html_text = body_el.get_attribute("innerHTML")


def click_to_follow(browser):
    my_follow_btn_xpath = "//button[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    follow_btn_elements = browser.find_element_by_xpath(my_follow_btn_xpath)
    for btn in follow_btn_elements:
        time.sleep(2)
        try:
            btn.click()
        except:
            pass


time.sleep(10)

profile_url = "https://www.instagram.com/therock/"
browser.get(profile_url)

post_xpath_str = "//a[contains(@href, '/p/')]"
post_links = browser.find_element_by_xpath(post_xpath_str)
post_link_el = None

if len(post_links) > 0:
    post_link_el = post_links[0]

if post_link_el != None:
    post_href = post_link_el.get_attribute("href")
    browser.get(post_href)

video_els = browser.find_element_by_xpath("//video")
img_els = browser.find_element_by_xpath("//img")
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)


def scrape_save(elements):
    for el in elements:
        url = el.get_attribute('src')
        base_url = urlparse(url).path
        filename = os.path.basename(base_url)
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            continue
        with requests.get(url, stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath, 'wb') as f:
                for ch in r.iter_content(chunk_size=8192):
                    if ch:
                        f.write(ch)


def auto_comment(browser, comment='Yaaay!!!'):
    time.sleep(3)
    comment_xpath_str = "//textarea[contains(@placeholder, 'Add a comment')]"
    comment_el = browser.find_element_by_xpath(comment_xpath_str)
    comment_el.send_keys(comment)
    submit_btn = "//button[type='submit']"
    submit_btn_els = browser.find_elements_by_css_selector(submit_btn)
    time.sleep(2)
    for btn in submit_btn_els:
        try:
            btn.click()
        except:
            pass


def auto_likes(browser):
    like_xpath = "//*[contains(@aria-label, 'Like')]"
    all_like_els = browser.find_element_by_xpath(like_xpath)
    max_heart_h = -1
    for heart_el in all_like_els:
        h = heart_el.get_attribute("height")
        current_h = int(h)
        if current_h > max_heart_h:
            max_heart_h = current_h
    all_like_els = browser.find_element_by_xpath(like_xpath)
    for heart_el in all_like_els:
        h = heart_el.get_attribute('height')
        if h == max_heart_h or h == f'{max_heart_h}':
            parent_button = heart_el.find_element_by_xpath('..')
            time.sleep(2)
            try:
                parent_button.click()
            except:
                pass
