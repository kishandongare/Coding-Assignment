#!/usr/bin/env python
# coding: utf-8

# In[8]:


###########################################################
#Name : Kishan Dongare
#Email : kishan.tech25@gmail.com
#Phone : +918319171837
#Role : Python Developer
############################################################

from bs4 import BeautifulSoup
import requests
import pandas

url = "https://www.justwatch.com/ag/movie/k-g-f-chapter-1" #Already a movie link

page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
#print(soup.prettify())

def movie_name():
    scraped_movies2= soup.find_all('div',class_='title-block')
    scraped_movies2
    movies2 = []
    for movie in scraped_movies2:
        for h in soup.find_all('h1'):
            movies2.append(h.get_text('h1').strip())
    movie_name = movies2
    print("Movie Name:>", movie_name)
movie_name()

def Release_Year():
    scraped_movies3= soup.find_all('div',class_='title-block')
    scraped_movies3
    movies3 = []
    for movie in scraped_movies3:
        for h in soup.find_all('span',class_="text-muted"):
            movies3.append(h.get_text('span').strip())
    release_year = movies3
    print("Release Year :>",release_year)
Release_Year()

def rating_genre_duration_Dname():
    scraped_movies = soup.find_all('div', class_='detail-infos__value' )
    scraped_movies
    movies = []
    for movie in scraped_movies:
        movies.append(movie.get_text().strip())
    movies[0:4]
    rating = movies[0]
    print("IMDB Rating :>",rating)
    genre = movies[1]
    print("Genre:>", genre)
    duration = movies[2]
    print("Duration:>",duration)
    director = movies[3]
    print("Director Name:>",director)
    
rating_genre_duration_Dname() 

def cast():
    scraped_movies1= soup.find_all('div', class_= 'title-credits__actor')
    scraped_movies1
    movies1 = []
    for movie in scraped_movies1:
        movies1.append(movie.get_text())
    cast = movies1
    print("Cast:>",cast)
cast()

#Language  :  Not found Language of movie in webpage or movie of link.
#movie link : Movie link is a already a scraping link


# In[ ]:




