import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")
titles = soup.find_all("td",{"class" : "titleColumn"})
ratings =  soup.find_all("td",{"class" : "ratingColumn imdbRating"})

for title,rating in zip(titles,ratings):
    title = title.text
    rating = rating.text
    print("Titles", title)
    print("Rating", rating)
