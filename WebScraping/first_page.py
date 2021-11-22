from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time


urls = []
headlines = []
articles = []
url_as_key ={} #saving articles as value, url as key

response = requests.get('http://www.bbc.co.uk/news')
doc = BeautifulSoup(response.text, 'html.parser')


def get_headlines():
    headlines = doc.find_all('h3')

    for headline in headlines:
        print(headline.text)
        headlines.append(headline.text)


#Using the ['href] attribute we recieve the url, without the website(bbc.com,google.com,etc. to fill this gap, I added this func.
def create_url(website,link):
    newlink = ""
    newlink += website
    newlink += str(link)
    new_url = newlink
    return new_url



#note: there's a limited amount of web entries before BBC blocks login attempt. Adding sleep to try prevent block.

def get_content():

    website = "http://bbc.com"
    links = doc.find_all('a', { 'class': 'gs-c-promo-heading' })
    for link in links:
        urls.append(create_url(website,link['href']))
    for link in links:
        new_url = create_url(website, link['href'])
        response2 = requests.get(new_url)
        text = ' '.join(BeautifulSoup(response2.text, 'html.parser').stripped_strings)
        print(text)
        articles.append(text)
        time.sleep(5) #waiting x amount of seconds to prevent blocking




def url_to_articles():
    for i in range(len(urls)):
        url_as_key[urls[i]] = articles[i]


print(urls)
print(articles)
url_to_articles()
print(url_as_key)



