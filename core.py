from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

class Tweet:
    def __init__(self, id, text):
        self.id = id
        self.text = text
    def getText(self):
        return str(self.text)
    def getId(self):
        return str(self.getId)
    def print(self):
        a = str(self.id) + ' ' + str(self.text)
        print(a)

# username = raw_input("What's your twitter id?")
def crawl():
    browser = webdriver.Chrome()
    username = u'radian614'
    header = u'https://twitter.com/search?q='
    url = header + username

    browser.get(url)
    time.sleep(1)

    body = browser.find_element_by_tag_name('body')

    for num in range(5):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    tweet_list = browser.find_elements_by_class_name('tweet-text')
    tweetSet = set()
    id = 0

    for tweet in tweet_list:
        tweetObj = Tweet(id, tweet.text)
        tweetSet.add(tweetObj)
        id = id + 1

    makeJSON(tweetSet, username)

def makeJSON(tweetSet, username):
    data = {}
    data['documents'] = []
    for tweet in tweetSet:
        text = tweet.text
        id = tweet.id
        data['documents'].append({
            'language': 'en',
            'id': id,
            'text': text
        })

    with open(username + '.txt', 'w') as outfile:
            json.dump(data, outfile)
