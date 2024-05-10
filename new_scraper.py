from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

time.sleep(10)

new_planets_data = []

star_list = []
star_names = []
radius = []
masses = []
distances = []
def scrape_field_brown_dwarfs(hyperlink):

    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content,"html.parser")        

    temp_list = []
    for tr_tag in soup.find_all("tr",attrs={ "class" : "wikitable sortable jquery-tablesorter"}):
        td_tags = tr_tag.find_all("td")
        for td_tag in td_tags:
            try :
                temp_list.append(td_tag.find_all("div", attrs={"class":"value"})[0].contents[0])
            except : 
                temp_list.append("")
                print("no value")
    star_list.append(temp_list)

    for data in star_list:
        star_names.append(data[0])
        radius.append(data[8])
        masses.append(data[7])
        distances.append(data[5])

headers = ["Star Name",
           "Radius",
            "Mass",
            "Distance"]
new_planet_df_1 = pd.DataFrame(star_list,columns = headers)

# Convert to CSV
new_planet_df_1.to_csv('drawfs_scraped_data.csv', index=True, index_label="id")
