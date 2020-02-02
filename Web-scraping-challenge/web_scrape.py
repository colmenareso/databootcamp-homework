#################################################
# Jupyter Notebook Conversion to Python Script
#################################################

# Setting the dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

# Function to initialize Splinter browser
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


# Defining function to scrape the web
def scrape():
    
    browser = init_browser()
    # Creating a dictionary to store the scrapped data
    mars_data = {}

    #################################################
    # Nasa Mars News scraping
    #################################################


    # Providing first url to Mars news and opening site in splinter
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    time.sleep(1)

    # Opening Beautifulsoup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Defining the html elements to scrap for the information
    item_list = soup.find('div', {'class': 'list_text'})

    # Grabing most recent news headline
    news_title = item_list.find('div', {'class': 'content_title'}).text

    # Grabing the most recent news teaser text
    news_teaser = item_list.find('div', {'class': 'article_teaser_body'}).text

    #Storing scraped data into the mars_data dictionary
    mars_data["nasa_headline"] = news_title
    mars_data["nasa_teaser"] = news_teaser
 
    #################################################
    # JPL Mars Space Images - Featured Image
    #################################################

    # Providing second url to Mars Space Images and opening site in splinter
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    
    # Opening Beautifulsoup
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')

    # Defining the html elements to scrap for the information
    image = soup2.find('a', {'class': 'button fancybox'})
  
    # Checking image attributes
    image.attrs
    featured_image_url = 'jpl.nasa.gov'+image.attrs['data-fancybox-href']
    
    # Storing the url in a variable 
    image_path = f'https://www.{featured_image_url}'
    
    #Storing scraped data into the mars_data dictionary
    mars_data["feature_image_src"] = image_path

    #################################################
    # Mars Weather
    #################################################

    # Providing third url to Mars Weather and opening requests to the url
    url_3='https://twitter.com/marswxreport?lang=en'
    response=requests.get(url_3)

    # Opening Beautifulsoup and showing html to check the tag for the weather update
    html3 = browser.html
    soup3 = BeautifulSoup(html3, 'html.parser')

    # Set up parser
    soup=BeautifulSoup(response.text, 'lxml')

    # Finding all tweets for Mars weather
    mars_weather=soup.find_all('div', class_='js-tweet-text-container')

    # Opening an empty list to store the Mars weather and appending by looping through the Mars weather updates
    weather_updates = []
    for weather in mars_weather:
        update = weather.text
        weather_updates.append(update)

    # Storing insights into a variable
    weather_report = [s for s in weather_updates if "InSight" in s]

    # Checking the first record of the array
    mars_weather = weather_report[0]

    # Cleaning text
    mars_weather = mars_weather.replace('\n',' ')
    mars_weather = mars_weather.split('pic.twitter')[0]


    #Storing scraped data into the mars_data dictionary
    mars_data["weather_summary"] = mars_weather

    #################################################
    # Mars Facts
    #################################################

    # Providing fourth url to Mars Facts and opening site in splinter
    url4= 'https://space-facts.com/mars/'
    browser.visit(url4)
    
    time.sleep(1)

    # Opening Beautifulsoup
    html4 = browser.html
    soup4 = BeautifulSoup(html4, 'html.parser')

    # Defining the html elements to scrap for the information (table)
    table = soup4.find('tbody')

    # Opening an empty list to store the Mars facts and appending by looping through the Mars facts 
    mars_facts = []

    for fact in table:
        facts = {}
        facts['fact'] = fact.find('td', {'class':'column-1'}).text
        facts['measurement'] = fact.find('td', {'class':'column-2'}).text
        mars_facts.append(facts)
    
    # Creating a dataframe to store the facts
    mars_facts = pd.DataFrame(mars_facts)

    #Storing scraped data into the mars_data dictionary
    mars_facts_html = mars_facts.to_html(header=False, index=False)
    mars_data["fact_table"] = mars_facts_html
    
    #################################################
    # Mars Hemispheres
    #################################################

    # Providing the url's for Mars hemispheres and opening sites in splinter
    urls = ['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 
           'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced', 
           'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced', 
           'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']

    # Opening an empty list to store the hemisphere information and appending by looping through the site 
    mars_hemispheres = []

    for url in urls:
        browser.visit(url)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        hemispheres = {}
        hemispheres['img_url'] = soup.find('a',{'target':'_blank'}).attrs['href']
        hemispheres['title'] = soup.find('h2', {'class':'title'}).text.split(' Enhanced')[0]
        mars_hemispheres.append(hemispheres)

    #Storing scraped data into the mars_data dictionary
    mars_data["hemisphere_imgs"] = mars_hemispheres

    # Closing browsing session
    browser.quit()
    
    return mars_data