from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup 
import time
import pandas as pd

scraped_data = []

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# chrome_location = "/Users/Gargi/Desktop/Project127/chromedriver-mac-x64/chromedriver"
browser = webdriver.Chrome()
browser.get(START_URL)

soup = BeautifulSoup(browser.page_source,"html.parser")


def scrape():
    
    brightest_star_table = soup.find("table", attrs={"class","wikitable"})
    table_body = brightest_star_table.find('tbody')
    table_body = table_body.find_all('tr')

    for row in table_body:
        table_cols = row.find_all('td')
        print(table_cols)

        temp_list = []

        for col_data in table_cols:
            data = col_data.text.strip()
            print(data)

            temp_list.append(data)
        scraped_data.append(temp_list)

scrape()

stars_data = []

for i in range(0, len(scraped_data)):
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
 #   Lum = scraped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius]
    stars_data.append(required_data)

header = ['Star_name', 'Distance', 'Mass', 'Radius']
stars_df_1 = pd.DataFrame(stars_data, columns=header)

stars_df_1.to_csv('scraped_data.csv',index=True, index_label="id")



