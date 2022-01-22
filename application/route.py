from application import app
from flask import Flask, request, url_for, render_template, redirect,session,request
from twilio.rest import Client 
from application.twilio_auth import collection as tauth

from twilio.twiml.messaging_response import MessagingResponse


session={'user':True}

client = Client(tauth['account_sid'], tauth['auth_token']) 

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
    bot_resp=MessagingResponse()
    msg=bot_resp.message()
    print("\n\n{}".format(str(user_msg)))
    msg.body("I am BME Server. how can i help you")
    return str(bot_resp)