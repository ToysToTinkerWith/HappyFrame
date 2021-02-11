#! /usr/bin/python3

#cron
# * * * * * /home/pi/Desktop/happyframe/happyframe/Python/DBconnection.py 

#pip3 install pymongo
#pip3 install pymongo[srv]
#sudo apt install feh -y
import pymongo
from pymongo import MongoClient
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from io import BytesIO
import os
import shutil
import base64


cluster = MongoClient("mongodb+srv://abergquist96:clappersglee9610@cluster0-tzqlf.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["Facility1"]
collection = db["12345"]

path = "../../Pictures/"

shutil.rmtree(path)
os.mkdir(path)

#for file in os.listdir(path):
    #os.remove(file)
    #os.system("rm " + str(file))
    #print(str(file))


results = collection.find()

newImg = Image.open("smile.jpg")
newImgCaption = "Welcome to your frame! You have " + str(collection.count_documents({})) + " images to view"
fontSpec = ImageFont.truetype("Oswald-VariableFont_wght.ttf", 20)
draw = ImageDraw.Draw(newImg)
draw.text(xy=(20, 20), text=newImgCaption, fill=(0,0,0), font=fontSpec)
newImg.save(path + "1.jpg", newImg.format)

            
for result in results:
    imgBytes = base64.b64decode(result['img'])
    newImg = Image.open(BytesIO(base64.b64decode(result['img'])))
    newImgCaption = result["imgCaption"]
    fontSpec = ImageFont.truetype("Oswald-VariableFont_wght.ttf", int(result["imgHeight"]/20))
    draw = ImageDraw.Draw(newImg)
    draw.rectangle(((0, result["imgHeight"]), (result["imgWidth"], result["imgHeight"] * 0.8)), fill="white")  
    draw.text(xy=(10, result["imgHeight"] * 0.8), text=newImgCaption, fill=(0,0,0), font=fontSpec)
    newImg.save(path + str(result["_id"]), result['imgType'])
    

os.system("DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority feh -qrYFD5 --zoom fill " + path)





