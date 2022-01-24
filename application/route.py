from application import app
from flask import Flask, request, url_for, render_template, redirect,session,request
from twilio.rest import Client 
from application.twilio_auth import collection as tauth
from application.tpo import tpo_data 


from twilio.twiml.messaging_response import MessagingResponse
import time

app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'



session={'user':'student'}

client = Client(tauth['account_sid'], tauth['auth_token']) 


# jupyter notebook data ------------------------------------------------------1



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
    print("\n{}: {}\n{} ".format(user_name,str(user_msg),mob))

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
        for i in range(len(google_classroom)):
            reply += f"\n{google_classroom[i][0]}: {google_classroom[i][1]}"
        msg.body(reply)
        return str(bot_resp)

    elif "tpo" in user_msg or "internship" in user_msg or "placement" in user_msg or "company" in user_msg or "companies" in user_msg:
        tpo_data.sort()
        if "deadline" in user_msg or "recent" in user_msg or "recently" in user_msg:
            reply += f"{tpo_data[0][2]}\n\nDeadline: {tpo_data[0][0]}\nLink: {tpo_data[0][1]}"
        else:
            for i in range(len(tpo_data)):
                reply += f"{tpo_data[i][2]}\n\nDeadline: {tpo_data[i][0]}\nLink: {tpo_data[i][1]}\n---------/////////////////--------\n"
        msg.body(reply)
        return str(bot_resp)

    elif "event" in user_msg or "upcoming event" in user_msg or "clubs" in user_msg or "tcp" in user_msg or "update" in user_msg:
        upCommingEvents.sort()
        
        for i in range(len(upCommingEvents)):
            reply += f"{upCommingEvents[i][2]}\n\nDeadline: {upCommingEvents[i][0]}\nLink: {upCommingEvents[i][1]}\n---------/////////////////--------\n"
        msg.body(reply)
        return str(bot_resp)

    elif "hello" in user_msg or "hi" in user_msg or "hey" in user_msg:
        reply = f"Hello {user_name}!\nHow are you?"
        msg.body(reply)
        return str(bot_resp)

    elif "college website" in user_msg or "clg website" in user_msg:
        reply = "http://www.nitrr.ac.in/"
        msg.body(reply)
        return str(bot_resp)


    msg.body(f"Hello {user_name}!\nI am BME bot. I can help you in following operations:\n*time table* | *classes* | *events* | *updates* | *tpo* | *clg*")
    return str(bot_resp)



