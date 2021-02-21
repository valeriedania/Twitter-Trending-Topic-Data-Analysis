import json

#Load WW_trends and US_trends
WW_trends = json.loads(open('datasets/WWTrends.json').read())
US_trends = json.loads(open('datasets/USTrends.json').read())

#Inspecting data
print(WW_trends)
print(US_trends)
