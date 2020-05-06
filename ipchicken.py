from bs4 import BeautifulSoup
import numpy as np
import time
import requests

scraped = ""
answer = False

url = 'https://httpbin.org/user-agent'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
response = requests.get(url,headers=headers)
html = response.content


def scrape():
    global answer
    page = requests.get("https://www.ipchicken.com/")
    soup = BeautifulSoup(page.text, "html.parser")
    ip = soup.find("b").text
    if ip != answer:
        print("The IP hasn't changed")
    else: 
        answer == True
        print("The IP has changed")
    time.sleep(3)
    while answer == False:
        scrape()
        time.sleep(3)

scrape()
