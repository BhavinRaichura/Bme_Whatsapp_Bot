# Whatsapp_Bot


## python
 python 3,
 function,
 oops,
 environment,
 database connection

## Flask 
flask basic


## Twilio
• create twilio account and get a whatsapp bot number

• put account_sid and auth_token in twilio_auth.py

• when you run the server, you also need to change link of whatsapp message coming link from twilio (use below path)
     
     go to twilio > messaging > settings > whatsapp sendbox settings > page (Twilio Sandbox for WhatsApp)  > find (Sandbox Configuration) > find -("WHEN A MESSAGE COMES IN") and put here the link of your server ie. http://www.yourdomain/bot


## MongoDB
• basic knowledge of mongodb

• I used below given collections 
   1) classroom
   2) events
   3) Training management team
   4) class_update
   5) users

• put database connection link in db.py (MongoClient)


## Server
I use ngrok server. Server is required to connect Flask to Twilio.


## Installation
##### git clone https://github.com/BhavinRaichura/Bme_Whatsapp_Bot
##### cd Bme_Whatsapp_Bot
##### . venv/bin/activate
##### install requirements.txt
##### flask run
#
---------------------------Make sure you have covered all of the above requirements before running----------------------------------



