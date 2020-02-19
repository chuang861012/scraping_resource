import requests
from lxml import etree
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

def scrape(url):
    res = requests.get(url, headers=headers)
    content = res.content.decode()

    html = etree.HTML(content)

    print(*html.xpath('//div[@class="g"]//div[@class="r"]/a/@href'),sep='\n')

    next = html.xpath('//div[@id="navcnt"]//td[contains(@class,"navend")][last()]/a/@href')

    time.sleep(1)

    return scrape(f'https://www.google.com{next[0]}')

scrape("https://www.google.com/search?q=youtube&tbs=li:1")