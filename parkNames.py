import pandas as pd
from pathlib import Path

def getParkNames(file):
  df = pd.read_excel(file, engine='odf')

  parkShortenedNames = df['park_name'].tolist()
  governingBodies = df['governing_body'].tolist()
  
  parkFullNames = [str1 + ' ' + str2 for str1, str2 in zip(parkShortenedNames, governingBodies)]
  
  return parkFullNames

def addCoordinatesToFile(file, parkData):
  df = pd.read_excel(file, engine='odf')
  latitudes = []
  longitudes = []
  for obj in parkData:
    if obj != None:
      latitudes.append(list(obj.values())[0][0])
      longitudes.append(list(obj.values())[0][1])
    else:
      latitudes.append('')
      longitudes.append('')
  df['latitude'] = latitudes
  df['longitude'] = longitudes
  df.to_excel('visited-parks_output.ods', engine='odf', index=False)
  print(f'coordinates uploaded to: {file}')