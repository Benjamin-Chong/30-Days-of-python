#Exercise 1

#1 Scrape Data as a json file from bu.edu
import requests
from bs4 import BeautifulSoup
import json
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

response = requests.get(url) #makes sure that the website is fetched correctly and is working
if response.status_code != 200:
    print(f"Failed to get page: {response.status_code}")
    exit()
status = response.status_code

content = response.content #creating a content variable that hold the html code.
soup = BeautifulSoup(content, 'html.parser') #parses the html code
print(soup.title.get_text()) #prints title

tables = soup.find_all('table',  class_='wikitable') #finds all tables on the website so that I can take the data from it
data = [] #place for the data on the website

for table in tables: #looping through each table found
    headers = [th.get_text(strip = True) for th in table.find_all('th')] #in the for loop here we iterate over the th's in the table and strip the whitespace and put it into a list
    rows = []
    for row in table.find_all('tr'): #iterates over all of the rows in the cells
        cells = row.find_all('td') #finds all of the data in the row (cells)
        if cells: #if not empty
            row_data  = [cell.get_text(strip = True) for cell in cells] #extract the text content and whitespace
            rows.append(dict(zip(headers, row_data)) if headers else row_data) #append with the header to the corresponding cell. turns the list into a dictionary if no headers then save the list of values instead of a dictionary
    if rows:
        data.append(rows) #if list is not empty, append to data list from the beginning
    
with open('./day_22/jsons/country_stats.json', 'w',  encoding = 'utf-8') as file: #creates a file or writes to the file
    json.dump(data, file, indent = 4) #takes the data and puts it into the file and formats as a readable json.

print(f'Scraped and saved. {len(data)}') #final print to indicate it is finished