
__author__ = 'jbasalone'

'''
Load all JSON Files, create a single CSV Files
'''

import csv
import json
import os

csvFileObj = open("YOURFILE.csv", "w")
csvWriter = csv.writer(csvFileObj)
csvWriter.writerow(["ROWNAME", "", "", ""])

for jsonFilename in os.listdir('.'):
    if not jsonFilename.endswith('.json'):
        continue
    print('Open file ' + jsonFilename)
    with open(jsonFilename) as jsonfile:
        x = json.load(jsonfile)

        for row in x:
            csvWriter.writerow(["",
                   row["ROWNAME"],
                   row[""],
                   row[""],
                   row[""],
                   row[""],
                   row[""],
                   row[""]])
csvFileObj.close()
