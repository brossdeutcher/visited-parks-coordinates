import parkNames
import coordinates
from pathlib import Path

path = Path('C:/Users/blake/Documents/Tableau/visited-parks/visited-parks.odf')
parkNames = parkNames.getParkNames(path)

for item in parkNames:
  print(coordinates.getCoordinates(item))