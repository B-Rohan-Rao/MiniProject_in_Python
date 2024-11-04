from bs4 import BeautifulSoup

with open("website.html") as file:  # Files are opened here
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")  # This one line of code complete our parsing.
# And the 'Soup' is now an object that allows us to tap in to the different part of the website.
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup)
print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)  # For getting all the tags.
for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

# Searching with the help of id of elements
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# searching like css selector
company_url = soup.select_one(
    selector="p a")  # We can also use any id or class as we do while styling in css like '#name' or '.heading'
print(company_url)
