#!/usr/bin/env python
# coding: utf-8

# In[393]:


from bs4 import BeautifulSoup as bs
from splinter import Browser
from pprint import pprint
import pymongo
import pandas as pd
import requests


def scrape_mars_mission():

    browser = Browser('chrome', headless = False)
    # browser.visit('https://www.google.com')


    # In[394]:


    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    # get_ipython().system('which chromedriver')


    # In[413]:


    executable_path = {'executable_path': r'C:\Users\sanja\Desktop\web-scraping-challenge\Missions_to_Mars/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[396]:


    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    # In[397]:


    #I use the beautiful soup(bs) to write the data into html format
    html = browser.html
    soup = bs(html,"html.parser")


    # In[398]:


    #Part I = in order to get the news title
    mission_to_mars_nt = soup.find("div",class_="content_title").text


    # In[399]:


    #to print the tile i used the print 
    print(f"Title: {mission_to_mars_nt}")


    # In[400]:


    # I used the beautiful soup(bs) to write the data into html format
    mission_to_mars_np = soup.find("div", class_="article_teaser_body").text


    # In[401]:


    #to print the tile i used the print 
    print(f"Paragraph: {mission_to_mars_np}")


    # In[402]:


    #Part II = JPL Mars Space Images - Featured Image
    browser = Browser('chrome', headless = False)
    browser.visit ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

    featured_imgaes_url ='https://photojournal.jpl.nasa.gov/jpeg/PIA17924.jpg'
    browser.visit (featured_imgaes_url)


    # In[403]:


    # pull image link
    pictures_from_mars_mission_src = []
    for image in images:
        pictures_from_mars_mission = image['data-fancybox-href']
        pictures_from_mars_mission_src.append(pic)

    featured_image_url = 'https://www.jpl.nasa.gov' + pic
    print (featured_image_url)


    # In[404]:


    #from Mars Weather, visit the Mars Weather twitter account
    url = ('https://twitter.com/marswxreport?lang=en')

    response = requests.get(url)
    soup = bs(response.text, 'html.parser')


    # In[405]:


    contents = soup.find_all("div",class_="content")
    print(content)


    # In[406]:


    from_mars_mission_weather_twitter = []
    for content in contents:
        tweet = content.find("div", class_="js-tweet-text-container").text
        weather_mars.append(tweet)
    #print(weather_mars)

    from_mars_mission_weather_twitter = weather_mars[8]
    print(from_mars_mission_weather_twitter)


    # In[407]:


    #Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    mission_mars_facts_url = "https://space-facts.com/mars/"
    mission_facts = pd.read_html(mission_mars_facts_url)
    mission_facts[0]


    # In[408]:


    #Use Pandas to convert the data to a HTML table string
    html_covert_pandas = mission_facts[0].to_html()
    html_covert_pandas = html_covert_pandas.replace("\n","")
    print (html_covert_pandas)


    # In[419]:


    hems_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit (hems_url)


    # In[415]:


    cerberus_hemisphere = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    browser.visit (cerberus_hemisphere)


    # In[416]:


    schiaparelli_hemisphere='https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    browser.visit (schiaparelli_hemisphere)


    # In[417]:


    syrtis_major_hemisphere='https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    browser.visit (syrtis_major_hemisphere)


    # In[418]:


    valles_marineris_hemisphere='https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
    browser.visit (valles_marineris_hemisphere)


    # In[420]:


    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]


    # In[422]:


    four_hemispheres = pd.DataFrame (hemisphere_image_urls)
    four_hemispheres

    return hemisphere_image_urls
  