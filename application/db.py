
import pymongo

mongoclient =pymongo.MongoClient()
 #jupyter notebook data ------------------------------------------------------3

db = mongoclient.BMEdb


#---------------------------------------------------------------------------------------------------------------------
# data fetch
# collections 
# 1) classroom
# 2) events
# 3) tpo
# 4) class_update
# 5) users


def class_room_details():
    reply=""
    clsrm = db.classroom
    for i in clsrm.find():
        reply += f"\n{i['subj']}: {i['link']}"
    return reply

def events_details():
    reply=""
    eve = db.events
    for i in eve.find():
        reply+=f"\n{i['subj']} \nLink: {i['link']} \nDeadline: {i['deadline']}\n-----------------------"
    return reply

def interns_details():
    reply=""
    interns = db.tpo
    for i in interns.find():
        reply+=f"\n{i['subj']} \nLink: {i['link']} \nDeadline: {i['deadline']}\n-----------------------"
    return reply

def new_updates_details():
    reply=""
    newup = db.class_update
    for i in newup.find():
        reply+=f"\n{i['subj']}\n-----------------------"
    return reply

