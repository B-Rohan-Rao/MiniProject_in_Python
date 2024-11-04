import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

movie_title = ["".join(i.getText().split()[1:]) for i in soup.select("h3")]
print(movie_title)
with open('movies.txt', "w", encoding="utf-8") as file:
    for index, movies in enumerate(movie_title):
        file.write(f"{index+1}) {movies}\n")
