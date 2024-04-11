import parkNames
import coordinates
from pathlib import Path

path = Path('visited-parks.ods')
parkNames = parkNames.getParkNames(path)

for item in parkNames:
  print(coordinates.getCoordinates(item))