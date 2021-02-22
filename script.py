import json

#Load WW_trends and US_trends
WW_trends = json.loads(open('datasets/WWTrends.json').read())
US_trends = json.loads(open('datasets/USTrends.json').read())

# Pretty-printing the results
print("WW trends:")
print (json.dumps(WW_trends, indent=1))

print("\n", "US trends:")
print (json.dumps(US_trends, indent=1))

#Extracting all the WW trend names from WW_trends
world_trends = set([trend['name']                    
                    for trend in WW_trends[0]['trends']])

#Extracting all the US trend names from US_trends
us_trends = set([trend['name'] 
                     for trend in US_trends[0]['trends']])

#Getting the intersection of the two sets
common_trends = world_trends = world_trends.intersection(us_trends)

#Inspecting data
print(world_trends, "\n")
print(us_trends, "\n")
print (len(common_trends), "common trends:", common_trends)
