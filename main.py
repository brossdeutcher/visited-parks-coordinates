import parkNames
import coordinates
from pathlib import Path

path = Path('visited-parks.ods')
parkNamesList = parkNames.getParkNames(path)

parkData = []
for item in parkNamesList:
  parkData.append(coordinates.getCoordinates(item))

output = parkNames.addCoordinatesToFile(path, parkData)
print(output)