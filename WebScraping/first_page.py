from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

urls = []
response = requests.get('http://www.bbc.co.uk/news')
doc = BeautifulSoup(response.text, 'html.parser')


def get_headlines():
    headlines = doc.find_all('h3')

    for headline in headlines:
        print(headline.text)


def get_content():

    website = "bbc.com"
    links = doc.find_all('a', { 'class': 'gs-c-promo-heading' })
    for link in links:
        char = '"'
        urls.append(link)
        new_url = char + website + link + char
        response = requests.get(new_url)
        text = ' '.join(BeautifulSoup(response.text, 'html.parser').stripped_strings)
        print(text)




get_content()




#testing the bbc base url + link

def test():
    char = '"'
    website = "bbc.com"
    link = "/news/world-us-canada-59369492"
    new_link = char + website + link + char
    print(new_link)






"""
    text = ' '.join(BeautifulSoup(response.text, 'html.parser').stripped_strings)
    print(text)
    
    
        # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print(text)
    
    
headlines = doc.find_all('h3')

for headline in headlines:
    print(headline.text)

links = doc.find_all('a', { 'class': 'gs-c-promo-heading' })

for link in links:
    print(link.text)

links = doc.find_all('a', { 'class': 'gs-c-promo-heading' })

for link in links:
    print(link.text)
    print(link['href'])
"""