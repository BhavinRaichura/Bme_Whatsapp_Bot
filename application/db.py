import pymongo

mongoclient = pymongo.MongoClient() #jupyter notebook data ------------------------------------------------------3

db = mongoclient.BMEdb

#--------------------------------------------------------------------------------------
# update database

@app.route("/usersdb",methods =['POST','GET'])
def usersdb():
    if request.method == "POST":
        dataset={"name":request.form['std_name'],"roll_no":request.form['rollno'],"mobile_no":request.form['mobile'],"email":request.form['email'],"open_elective":request.form['oe'],"sem":6}
        db.users.insert_one(dataset)
        return "<h1>data successfully added</h1>"
    return "<h1>thank you</h1>"

@app.route("/tpodb",methods =['POST','GET'])
def tpodb():
    if request.method == "POST":
        dataset={"deadline":request.form['deadline'],"link":request.form['link'],"subj":request.form['subj']}
        db.tpo.insert_one(dataset)
        return "<h1>data successfully added</h1>"
    return "<h1>thank you</h1>"

@app.route("/eventsdb",methods =['POST','GET'])
def eventsdb():
    if request.method == "POST":
        dataset={"deadline":request.form['deadline'],"link":request.form['link'],"subj":request.form['subj']}
        db.events.insert_one(dataset)
        return "<h1>data successfully added</h1>"
    return "<h1>thank you</h1>"

@app.route("/newUpdatesdb",methods =['POST','GET'])
def newUpdatesdb():
    if request.method == "POST":
        dataset={"subj":request.form['subj']}
        db.class_update.insert_one(dataset)
        return "<h1>data successfully added</h1>"
    return "<h1>thank you</h1>"

#---------------------------------------------------------------------------------------------------------------------
# data fetch

def class_room_details():
    clsrm = db.classroom
    for i in clsrm.find():
        reply += f"\n{i['subj']}: {i['link']}"
    return reply

def events_details():
    eve = db.events
    for i in eve.find():
        reply+=f"\n{i['subj']} \nLink: {i['link']} \n{i['deadline']}\n-----------------------"
    return reply

def interns_details():
    interns = db.tpo
    for i in interns.find():
        reply+=f"\n{i['subj']} \nLink: {i['link']} \n{i['deadline']}\n-----------------------"
    return reply

def new_updates_details():
    newup = db.class_update
    for i in newup.find():
        reply+=f"\n{i['subj']}\n-----------------------"
    return reply

