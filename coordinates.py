import requests
from bs4 import BeautifulSoup

def getCoordinates(parkName):
  # replaces spaces in park name with underscore to match url formatting
  park_name = parkName.replace(' ', '_')
  url = f'https://en.wikipedia.org/wiki/{park_name}'
  
  response = requests.get(url)

  if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    coordinates_table = soup.find('table', class_='infobox')

    if coordinates_table:
      rows = coordinates_table.find_all('tr')

      for row in rows:
        if 'coordinates' in row.text.lower():
          coordinates = row.find('span', class_='geo-dec').text
          latitude = coordinates.split()[0]
          longitude = coordinates.split()[1]

          return {parkName: [latitude, longitude]}