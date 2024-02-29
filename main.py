import requests
from bs4 import BeautifulSoup
import json

# Define the headers 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

# Make a request to the webpage with headers
response = requests.get('https://www.moneycontrol.com/news/business/markets/', headers=headers)

# Parse the content of the response with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all elements with class 
list_items = soup.find_all('li', class_='clearfix')

# Initialize an empty list to store extracted data
data = []

# Iterate through each element
for item in list_items:
    # Extract the text and href link from each element
    link = item.find('a')['href']
    date = item.find('span').text.strip()
    headline = item.find('h2').text.strip()
    paragraphs = item.find('p').text.strip()
    
    # Append the extracted data to the list
    data.append({
        'date': date,
        'headline': headline,
        'paragraph': paragraphs,
        'link': link
    })

# Save the extracted data into a JSON file
with open('moneycontrol_news.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)