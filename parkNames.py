import pandas as pd
from pathlib import Path

def getParkNames(file):
  df = pd.read_excel(file, engine='odf')

  parkShortenedNames = df['park_name'].tolist()
  governingBodies = df['governing_body'].tolist()
  
  parkFullNames = [str1 + ' ' + str2 for str1, str2 in zip(parkShortenedNames, governingBodies)]
  
  return parkFullNames

def addCoordinatesToFile(file, parkData):
  return parkData