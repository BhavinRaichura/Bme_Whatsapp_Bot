# Bme_Whatsapp_Bot
I have made this bot for my college. It is a WhatsApp bot that is connected to a database that has some collection that contains information related to new updates, time table, upcoming events etc. When someone needs something he will call this bot and the bot will search for keywords and actions, and return the data accordingly.

## Requirements

## python
 python 3.x
 function,
 oops,
 environment,
 database connection

## Flask 
flask basic


## Twilio
create twilio account and get a whatsapp bot number
put account_sid and auth_token in twilio_auth.py
when you run your server the also do
    go to twilio > messaging > settings > whatsapp sendbox settings > page (Twilio Sandbox for WhatsApp)  > find (Sandbox Configuration) > find -("WHEN A MESSAGE COMES IN") and put here the link of your server ie. http://www.yourdomain/bot


## MongoDB
basic knowledge of mongodb
database link
put database connection link in db.py (MongoClient)
#### collections 
 1) classroom
 2) events
 3) tpo
 4) class_update
 5) users


## Server
I use ngrok server. Server is required to connect Flask to Twilio.

### ---------------------------------------------------------------------------------------------------------------------
## Installation
##### git clone https://github.com/BhavinRaichura/Bme_Whatsapp_Bot
##### cd Bme_Whatsapp_Bot
##### . venv/bin/activate
##### install requirements.txt
##### flask run


