import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://spoton.it:27272/') # this is for local. For production, I used MongoClient("spoton.it", 27272)
db = client["calendar"]
nfl_teams = db.buttoncategories.find({"shortname": {"$regex": "nfl"}})
activity_pools = [team['activities'] for team in nfl_teams]
for activity_pool in activity_pools:
	for activityId in activity_pool:
		activity = db.buttonactivities.find_one({"_id": activityId})
		print(str(activity['name']) + "," + str(activityId))