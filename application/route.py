from application import app
from flask import Flask, request, url_for, render_template, redirect,session,request
from twilio.rest import Client 
from application.twilio_auth import collection as tauth

from twilio.twiml.messaging_response import MessagingResponse
import time

session={'user':True}

client = Client(tauth['account_sid'], tauth['auth_token']) 

oe="Open elective "
b="Biomaterials"
m="Microelectronics & ic"
t="Telemedicine"
d="BDMS"
timeSlot = ["09:15","10:15","11:15","12:15"]
mobile_collection={8085129146:"Bhavin",6268377894:"Deepti",7879789302:"Shivam"}
time_table ={"mon":[b,oe,m,t],"tue":[b,t,m,d],"wed":[b,oe,d,m],"thu":[b,d,m,t],"fri":[d,oe,t,m],"sat":["--","--","--","--"],"sun":["--","--","--","--"]}
days =["mon","tue","wed","thu","fri","sat","sun"]




def checkUser():
    print("ckeck is called")
    if session['user'] == False:
        return redirect(url_for('home'))
    else:
        print("present")
    return


@app.route("/")
def home():
    return "<h1>hello world</h1>"

@app.route("/auth")
def auth():
    print("auth")
    return "auth"


@app.route("/message/<string:msg>")

def msg(mailscript):
    return client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=mailscript,      
                              to='whatsapp:+918085129146' 
                          ) 


@app.route('/bot',methods=['GET','POST'])
def bot():
    user_msg = request.values.get('Body','').lower()
    user_mobile = request.values.get('From','').lower()
    bot_resp=MessagingResponse()
    msg=bot_resp.message()

    user_name=""
    mob=int(str(user_mobile)[12:])
    if mob in mobile_collection:
        user_name = mobile_collection[mob]
    print("\n{}\n{} ".format(str(user_msg),mob))

    if "time table" in user_msg:
        reply =""
        if "today" in user_msg:
            day = time.ctime()
            day=day[0:3].lower()
            classes = time_table[day]
            for i in range(4):
                reply= reply + f"\n{timeSlot[i]} {classes[i]}"
            msg.body(reply)
            return str(bot_resp)

        else:
            for i in days:
                if i in user_msg:
                    classes = time_table[i]
                    for j in range(4):
                        reply= reply + f"\n{timeSlot[j]} {classes[j]}"
                    msg.body(reply)
                    return str(bot_resp)

    elif "mc"  in user_msg or "madercho" in user_msg:
        reply="tu MC tera baap MC"
        msg.body(reply)
        return str(bot_resp)

    if "fuck" in user_msg or "gandu" in user_msg or "bhosd" in user_msg or "bc" in user_msg or "bahencho" in user_msg or "chodu" in user_msg or "bhncho" in user_msg or "f*ck" in user_msg or "chutiya" in user_msg:
        msg.body("chup kr gandu bhosadike")
        return str(bot_resp)

    if "hello" in user_msg or "hi" in user_msg or "hey" in user_msg:
        reply = f"Hello {user_name}!\nIts BME Server. How can i help you"
        msg.body(reply)
        return str(bot_resp)

    msg.body(f"Hello {user_name}!\nIts BME Server. ")
    return str(bot_resp)