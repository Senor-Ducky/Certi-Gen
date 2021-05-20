import PIL
from PIL import Image, ImageDraw, ImageFont #install these libraries before using or running the file.
import pandas as pd
import os

df = pd.read_csv("") #path to your csv file
names = df.to_dict(orient='record')

def generate_certificate(data): #function to
    template = Image.open("") #path to your template image
    font = ImageFont.truetype("", size=20) # path to your font
    draw = ImageDraw.Draw(template)
    draw.text((875,697), f"{data['name']}", font=font, fill='black') #renders text when you pass in the desired (x,y) co-ordinates and index from your CSV file.
    draw.text((897,758), "", font=font,fill='black') #renders date
    return template

#loop statement to output the number of certificates corresponding to the number of id's in your csv.
for record in names:
    certificate = generate_certificate(record)
    certificate.save(f"./certificates/{record['name']}.jpg") #outputs image in a folder of your choice with the name of the certificate recipient.