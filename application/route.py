from application import app
from flask import Flask, request, url_for, render_template, redirect,session,request
from application import db
from twilio.rest import Client 
from application.twilio_auth import collection as tauth
from application.tpo import tpo_data 

from twilio.twiml.messaging_response import MessagingResponse
import time

app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

session={'user':'student'}

client = Client(tauth['account_sid'], tauth['auth_token']) 


# jupyter notebook data ------------------------------------------------------1


# daily classes data
oe="Open elective\nhttps://meet.google.com/rjz-pghg-jrb"
b="Biomaterials\nhttps://meet.google.com/rmb-kayq-wrf"
m="Microelectronics & ic\nhttps://meet.google.com/acf-tnhp-fry"
t="Telemedicine\nhttps://meet.google.com/keo-qqht-tqd"
d="BDMS\nhttps://rb.gy/wlydv3"

timeSlot = ["09:30","10:30","11:30","12:30"]
time_table ={"mon":[b,oe,m,t],"tue":[b,t,m,d],"wed":[b,oe,d,m],"thu":[d,b,m,t],"fri":[d,oe,t,m],"sat":["-noClass-","-noClass-","-noClass-","-noClass-"],"sun":["-noClass-","-noClass-","-noClass-","-noClass-"]}
days =["mon","tue","wed","thu","fri","sat","sun"]

#----------------------------------------------------------------------------------------------------------------------------------------------------
@app.route("/")
def home():
    return "<h1>BME Bot</h1>"


@app.route("/message/<string:msg>")
def msg(mailscript):
    return client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=mailscript,      
                              to='whatsapp:+918085129146' 
                          ) 

#--------------------------------------------------------------------------------------
# bot

@app.route('/bot',methods=['GET','POST'])
def bot():

    user_msg = request.values.get('Body','').lower()
    user_mobile = request.values.get('From','').lower()
    bot_resp=MessagingResponse()
    msg=bot_resp.message()

    mob=str(user_mobile)[12:]
    user_name=""
    reply=""

    if "time table" in user_msg or "classes" in user_msg:
        reply =""

        if "exam" in user_msg:
            reply ="Data not found"
            msg.body(reply)
            return str(bot_resp)
        
        for i in days:
            if i in user_msg:
                classes = time_table[i]
                for j in range(4):
                    reply= reply + f"\n{timeSlot[j]} {classes[j]}"
                msg.body(reply)
                return str(bot_resp)
        
        day = time.ctime()
        day=day[0:3].lower()
        classes = time_table[day]
        for i in range(4):
            reply= reply + f"\n{timeSlot[i]} {classes[i]}"
        msg.body(reply)
        return str(bot_resp)


    elif 'classroom' in user_msg or 'class room' in user_msg or 'google class' in user_msg:
        reply=db.class_room_details()
        msg.body(reply)
        return str(bot_resp)

    elif "tpo" in user_msg or "internship" in user_msg or "placement" in user_msg or "company" in user_msg or "companies" in user_msg:
        reply = db.interns_details()
        msg.body(reply)
        return str(bot_resp)

    elif "event" in user_msg or "upcoming event" in user_msg or "clubs" in user_msg :
        reply=db.events_details()
        msg.body(reply)
        return str(bot_resp)

    elif "update" in user_msg or "announce" in user_msg:
        reply = db.new_updates_details()
        msg.body(reply)
        return str(bot_resp)

    elif "college website" in user_msg or "clg website" in user_msg:
        reply = "http://www.nitrr.ac.in/"
        msg.body(reply)
        return str(bot_resp)

    elif "hello" in user_msg or "hi" in user_msg or "hey" in user_msg:
        if db.db.users.find({"mobile_no":mob}):
            valid_user = db.db.users.find_one({"mobile_no":mob})
            user_name = valid_user['name']
        reply = f"Hello {user_name}!\nHow are you?"
        msg.body(reply)
        return str(bot_resp)

    msg.body(f"Hello {user_name}!\nI am BME bot. I can help you in following operations:\n*time table* | *classes* | *events* | *updates* | *tpo* | *clg*")
    return str(bot_resp)


#--------------------------------------------------------------------------------------
# update database
#
@app.route("/newusersdb",methods =['POST','GET'])
def newusersdb():
    if request.method == "POST":
        dataset={"name":request.form['std_name'],"roll_no":request.form['rollno'],"mobile_no":request.form['mobile'],"email":request.form['email'],"open_elective":request.form['oe'],"sem":6}
        db.db.users.insert_one(dataset)
        return "<h1>data successfully added</h1>"
    return render_template('index.html',pagetitle="New User")

@app.route("/tpodb",methods =['POST','GET'])
def tpodb():
    if request.method == "POST":
        dataset={"deadline":request.form['deadline'],"link":request.form['link'],"subj":request.form['subj']}
        db.db.tpo.insert_one(dataset)
        return "<h1>data successfully added</h1>"
    return render_template('index.html',pagetitle="TPO")

@app.route("/eventsdb",methods =['POST','GET'])
def eventsdb():
    if request.method == "POST":
        dataset={"deadline":request.form['deadline'],"link":request.form['link'],"subj":request.form['subj']}
        db.db.events.insert_one(dataset)
        return "<h1>data successfully added</h1>"
    return render_template('index.html',pagetitle="Events")

@app.route("/newupdatesdb",methods =['POST','GET'])
def newUpdatesdb():
    if request.method == "POST":
        dataset={"subj":request.form['subj']}
        db.db.class_update.insert_one(dataset)
        return "<h1>data successfully added</h1>"
    return render_template('index.html',pagetitle="New Updates")

