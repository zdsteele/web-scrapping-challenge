
from splinter import Browser
from bs4 import BeautifulSoup
import time


def init_browser(): 

    return Browser("chrome", headless=False)


def scrape_info():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
    time.sleep(1)
    
    soup = BeautifulSoup(browser.html, 'html.parser')

    titles = soup.find_all(class_='content_title')

    paragraph = soup.find_all(class_ = 'article_teaser_body')


# MOST RECENT TITLE
    title = soup.find_all(class_='content_title')[0].text
    title



# MOST RECENT DESCRITPTION 
    paragraph = soup.find_all('div', class_='article_teaser_body')[0].text
    paragraph



#  JPL Mars Space Image
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
    Image = browser.visit(featured_image_url)
    Image


# Mars Image
    browser.visit('https://twitter.com/marswxreport?lang=en')
    time.sleep(5)
    soup2 = BeautifulSoup(browser.html, 'html.parser')


    Mars_Weather = soup2.find_all(class_ ='tweet-text')[0].text
    Mars_Weather


    import pandas as pd 


### Mars Facts
    Mars_facts = 'https://space-facts.com/mars/'
    tables = pd.read_html(Mars_facts)
    tables


    Mars_df = tables[1]
    Mars_df


    html_mars_table = Mars_df.to_html()
    html_mars_table
    html_mars_table.replace('\n', '')


    Mars_df.to_html('mars_data_table.html')


# Mars Hemispheres
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    time.sleep(5)
    link_url = 'https://astrogeology.usgs.gov'


    soup3=BeautifulSoup(browser.html, 'html.parser')

    items = soup3.find_all("div", class_='item')

    dictionary_list = [] 
    title = "title"

    for item in items:
        link = item.find('a')
        href = link['href']
        h3 = item.find('h3').text
        dictionary_list.append({title:h3, "link": link_url + href},)
    
    
        # print(h3)
        # print(link_url + href)
        # print("-------------------------------------------------------------------------------------------------")
        dictionary_list







