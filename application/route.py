from application import app
from flask import Flask, request, url_for, render_template, redirect
from twilio.rest import Client 
from application.twilio_auth import collection as tauth



client = Client(tauth['account_sid'], tauth['auth_token']) 

@app.route("/")
def home():
    return "<h1>hello world</h1>"

@app.route("/<string:msg>")
def msg(msg):
    return client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=msg,      
                              to='whatsapp:+918085129146' 
                          ) 
     