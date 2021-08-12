from bs4 import BeautifulSoup
import requests

# CHALLENGE
# Did not finish because invalid HTML :)

# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
# response = requests.get(URL)
# top_movies_page = response.text
#
# soup = BeautifulSoup(top_movies_page, 'html.parser')
#
# print(soup.prettify())
#
# # top_movies = [movie.getText() for movie in soup.find_all(name="h3", class_="jsx-4245974604")]
# top_movies = soup.find_all(name="h3", class_="jsx-4245974604")
# print(top_movies)



# response = requests.get("https://news.ycombinator.com/news")
# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, 'html.parser')
#
# # print(soup.title)
#
# # first_title = soup.find(name="a", class_="storylink")
# # article_text = first_title.getText()
# # article_link = first_title.get("href")
# # article_upvote = soup.find(name="span", class_="score").getText()
# # print(article_text)
# # print(article_link)
# # print(article_upvote)
#
# all_articles = soup.find_all(name="a", class_="storylink")
# # print(all_articles)
# article_texts = []
# article_links = []
#
# for article_tag in all_articles:
#     article_text = article_tag.getText()
#     article_texts.append(article_text)
#     article_link = article_tag.get("href")
#     article_links.append(article_link)
#
# # article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# # print(article_texts)
# # print(article_links)
# # print(article_upvotes)
#
# max_value = max(article_upvotes)
# max_index = article_upvotes.index(max_value)
# print(article_texts[max_index])
# print(article_links[max_index])
# print(article_upvotes[max_index])


# LOCAL HTML

# import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')

###
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a) # first a
# print(soup.li) # first li

#
# print(soup.find_all(name="a"))

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.get("class"))

# CSS Selector
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# headings2 = soup.select(".heading")
# print(headings)
# print(headings2)