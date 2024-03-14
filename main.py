"""*"""
from helpful import *
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://ideas.veo.co/')

comments = browser.find_elements(By.XPATH, '//div[@class="sc-q2hkcp-0 gzWdQi"]')

scroll(browser)

links = []
for items in comments:
    item = items.find_element(By.TAG_NAME, 'a').get_attribute('href')
    links.append(item)

needed = {}
for link in links:
    browser.get(link)
    vote = browser.find_elements(By.XPATH, '//span[@class="sc-19vbhd9-2 bmFLkr"]')
    up_votes = vote[0].text
    down_votes = vote[1].text

    scroll(browser)

    elements = browser.find_elements(By.XPATH, '//div[@class="sc-1wdea31-0 cSBrqM"]')
    comment = elements[0].find_element(By.TAG_NAME, 'p').text
    date_made = elements[0].find_element(By.TAG_NAME, 'span').get_attribute('title')
    votes = (f"{up_votes}⬆ | {down_votes}⬇")

    sub_comments = {}
    for element in elements[1:]:
        name = element.find_element(By.TAG_NAME, 'button').text
        sub_elements = element.find_elements(By.TAG_NAME, 'p')
        for sub_element in sub_elements:
            sub_comment = sub_element.text
            sub_comments[name] = sub_comment

    needed.update({
        "Comment": comment,
        "Votes": votes,
        "Date_made": date_made,
        "Sub_comments": sub_comments,
    })

    write_json(needed, 'results/veo.json')

write_csv('results/veo.json')
