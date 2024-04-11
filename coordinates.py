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
          latitudeStr = coordinates.split()[0]
          latitude = float(latitudeStr.split('°')[0]) if latitudeStr.split('°')[1] == 'N' else float(latitudeStr.split('°')[0]) * -1
          longitudeStr = coordinates.split()[1]
          longitude = float(longitudeStr.split('°')[0]) if longitudeStr.split('°')[1] == 'N' else float(longitudeStr.split('°')[0]) * -1

          return {parkName: [latitude, longitude]}