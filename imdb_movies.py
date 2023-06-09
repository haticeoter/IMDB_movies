import requests
from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")

a = float(input("Enter the rating:"))

titles = soup.find_all("td",{"class":"titleColumn"})
ratings = soup.find_all("td",{"class","ratingColumn imdbRating"})

for title, rating in zip(titles,ratings):
    title = title.text
    rating = rating.text

    title = title.strip()
    title = title.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating) > a):
        print("Film name: {} Film ratingi : {}".format(title,rating))
