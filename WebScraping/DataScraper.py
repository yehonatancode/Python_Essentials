import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# https://www.geeksforgeeks.org/how-to-get-the-daily-news-using-python/
# https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558


# Creates a header
headers = {'User-agent': 'Mozilla/5.0'}

# Requests the webpage
request = requests.get('https://www.bbc.com/news', headers=headers)
html = request.content

# Create some soup
soup = bs(html, 'html.parser')
coverpage_news = []
"""def news_contents_gathered:
    with open('readme.txt', 'w') as f:
        f.write('Create a new text file!') #create a new text file to hold all the data
"""


# Used to easily read the HTML that we scraped
# print(soup.prettify())

def bbc_news_headlines(keyword):
    # Finds all the headers in BBC Home
    for h in soup.findAll('h3', class_='gs-c-promo-heading__title'):
        news_title = h.contents[0].lower()

        if news_title not in coverpage_news:
            if 'bbc' not in news_title:
                coverpage_news.append(news_title)

    no_of_news = 0
    keyword_list = []
    # Goes through the list and searches for the keyword
    for i, title in enumerate(coverpage_news):
        text = ''
        if keyword.lower() in title:
            text = ' <------------ KEYWORD'
            no_of_news += 1
            keyword_list.append(title)

        print(i + 1, ':', title, text)

    # Prints the Titles of the articles that contain the keywords
    print(f'\n--------- Total mentions of "{keyword}" = {no_of_news} ---------')
    for i, title in enumerate(keyword_list):
        print(i + 1, ':', title)


bbc_news_headlines('covid')


    def new_func():
        number_of_articles = 5


        # Empty lists for content, links and titles
        news_contents = []
        list_links = []
        list_titles = []

        for n in np.arange(0, number_of_articles):

            # We need to ignore "live" pages since they are not articles
            if "live" in coverpage_news[n].find('a')['href']:
                continue

            # Getting the link of the article
            link = coverpage_news[n].find('a')['href']
            list_links.append(link)

            # Getting the title
            title = coverpage_news[n].find('a').get_text()
            list_titles.append(title)

            # Reading the content (it is divided in paragraphs)
            article = requests.get(link)
            article_content = article.content
            soup_article = bs(article_content, 'html5lib')
            body = soup_article.find_all('div', class_='content__article-body from-content-api js-article__body')
            x = body[0].find_all('p')

            # Unifying the paragraphs
            list_paragraphs = []
            for p in np.arange(0, len(x)):
                paragraph = x[p].get_text()
                list_paragraphs.append(paragraph)
                final_article = " ".join(list_paragraphs)

            news_contents.append(final_article)
        for art in final_article:
            print(art)

"""
def headline_contents():
    # Empty lists for content, links and titles
    news_contents = []
    list_links = []
    list_titles = []
    number_of_articles = 5

    for n in np.arange(0, number_of_articles):


        # Getting the link of the article
        link = coverpage_news[n].find('a')['href']
        list_links.append(link)

        # Getting the title
        title = coverpage_news[n].find('a').get_text()
        list_titles.append(title)

        # Reading the content (it is divided in paragraphs)
        article = requests.get(link)
        article_content = article.content
        soup_article = bs(article_content, 'html5lib')
        body = soup_article.find_all('div', class_='content__article-body from-content-api js-article__body')
        x = body[0].find_all('p')

        # Unifying the paragraphs
        list_paragraphs = []
        for p in np.arange(0, len(x)):
            paragraph = x[p].get_text()
            list_paragraphs.append(paragraph)
            final_article = " ".join(list_paragraphs)

        news_contents.append(final_article)
        # df_features
        df_features = pd.DataFrame(
            {'Article Content': news_contents
             })

        # df_show_info
        df_show_info = pd.DataFrame(
            {'Article Title': list_titles,
             'Article Link': list_links})
        print(df_show_info)
        for c in news_contents:
            print(c)


headline_contents()

"""
