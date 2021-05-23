# Declare Dependencies 
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    # @NOTE: Path to my chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

# Create Mission to Mars global dictionary that can be imported into Mongo
mars_info = {}

# NASA MARS NEWS
def scrape_mars_news():

        # Initialize browser 
        browser = init_browser()

        # Visit Nasa news url through splinter module
        url = 'https://redplanetscience.com/'
        browser.visit(url)

        # HTML Object
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve the latest element that contains news title and news_paragraph
        result = soup.find('div', class_="list_text")
        news_title = result.text
        news_p = result.find('div',class_="article_teaser_body").text

        # Dictionary entry from MARS NEWS
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_p

        return mars_info

        browser.quit()

# FEATURED IMAGE
def scrape_mars_image():

        # Initialize browser 
        browser = init_browser()

        # Visit Mars Space Images through splinter module
        img_url = 'https://spaceimages-mars.com/'
        browser.visit(img_url)

        # HTML Object 
        img_html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(img_html, 'html.parser')

        # Retrieve background-image url from style tag 
        img_result = soup.find('img', class_="headerimage fade-in")['src']

        img_url = img_result.replace("background-image: url('","").replace("');","")
        featured_image_url = f"https://spaceimages-mars.com/{img_url}"
      
        # Dictionary entry from FEATURED IMAGE
        mars_info['featured_image_url'] = image_url 
        
        browser.quit()

        return mars_info

        
# Mars Facts
def scrape_mars_facts():

        # Initialize browser 
        browser = init_browser()

         # Visit Mars facts url 
        facts_url = 'https://galaxyfacts-mars.com/'
        browser.visit(facts_url)

        # Use Pandas to "read_html" to parse the URL
        tables = pd.read_html(facts_url)

        #Find Mars Facts DataFrame in the lists of DataFrames
        df = tables[1]
        df.columns = ["Description","Value"]
        idx_df = df.set_index("Description")

        # Dictionary entry from Mars Facts

        mars_info['tables'] = idx_df

        return mars_info

# Mars Hemisphere

def scrape_mars_hemispheres():

        # Initialize browser 
        browser = init_browser()

        # Visit hemispheres website through splinter module 
        hemi_url = 'https://marshemispheres.com/'
        browser.visit(hemi_url)

        # HTML Object
        hemi_html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(hemi_html, 'html.parser')

        # Retreive all items that contain mars hemispheres information
        items = soup.find_all('div', class_='item')

        # Create empty list for hemisphere urls 
        hemi_img_urls = []

        # Store the main_ul 
        hemi_main_url = 'https://marshemispheres.com/'

        # Loop through the items previously stored
        for i in items: 
            # Store title
            title = i.find('h3').text
            
            # Store link that leads to full image website
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
            # Visit the link that contains the full image website 
            browser.visit(hemi_main_url + partial_img_url)
            
            # HTML Object of individual hemisphere information website 
            partial_img_html = browser.html
            
            # Parse HTML with Beautiful Soup for every individual hemisphere information website 
            soup = BeautifulSoup(partial_img_html, 'html.parser')
            
            # Retrieve full image source 
            img_url = hemi_main_url + soup.find('img', class_='wide-image')['src']
            
            # Append the retreived information into a list of dictionaries 
            hemi_img_urls.append({"title" : title, "img_url" : img_url})

        mars_info['hemi_img_urls'] = hemi_img_urls
        
       
        browser.quit()

        # Return mars_data dictionary 

        return mars_info