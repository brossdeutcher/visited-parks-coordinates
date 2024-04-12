import fileHandler
import webScraper
from pathlib import Path

path = Path('visited-parks.ods')
parkNamesList = fileHandler.getParkNames(path)

parkData = []
for item in parkNamesList:
  parkData.append(webScraper.getData(item))

output = fileHandler.addDataToFile(path, parkData)