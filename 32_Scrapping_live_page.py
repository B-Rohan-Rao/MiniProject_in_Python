from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.select(".storylink")
link = [i.get("href") for i in article_tag]
title = [i.getText() for i in article_tag]
article_upvote = [int(i.getText().split()[0]) for i in soup.select(".score")]
index = article_upvote.index(max(article_upvote))
print(link[index])
print(title[index])

# print(link)
# print(title)
# print(article_upvote)
