#   Jennifer Walker
#   CS 1122
#   HW 02

def imageGeneration():
    #imports Pillow functions; imports random 
    from PIL import Image, ImageFont, ImageDraw
    import random

    #prompts user for name for image
    userName = input("Please enter the user's name. ") 

    #sets image size
    size = 240, 284 
    #background image
    imgNet = Image.new('RGBA', size, color=0)
    draw = ImageDraw.Draw(imgNet)
    #generates random RGB values and then draws rec. w that color
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
    draw.rectangle([(20,20),(220,220)], fill=color)

    #draws eyes
    draw.ellipse(((65, 65), (80, 80)), fill = 'white')
    draw.ellipse(((165, 65), (180, 80)), fill = 'white')

    #draws smile
    draw.arc([(100,100),(200,150)], 45, 135, fill = 'white')

    #draws text
    fnt = ImageFont.truetype("SignPainter.otf", 35)
    draw.text((80,240), userName, font=fnt, fill=('grey'))

    #saves picture
    imgNet.save("NetflixIcon.jpg")
    imgNet.show()

def JSONparse():
    import json, urllib.request
    #opens and reads
    with urllib.request.urlopen('http://elections.huffingtonpost.com/pollster/api/charts/2016-national-gop-primary') as response:
        DemData = str(response.read())
    start = DemData.find("[")
    end = DemData.find("]")
    dictString = DemData[start+1:end] 
    dictList = []
    #adds dicts from string into list 
    while len(dictString) > 1:
        bracket = dictString.find("}")
        dictList.append(dictString[:bracket+1])
        dictString = dictString[bracket+2:]
    #parses each dict
    for choice in dictList:
        parsedData = json.loads(choice)
        #prints candidate and value 
        try:
            print(parsedData['first_name'], parsedData['last_name'] + ":", str(parsedData['value']))
        except TypeError:
            print(parsedData['choice'] + ":", parsedData['value']) 

def main():
    #first task 
    imageGeneration()
    #second task
    JSONparse() 

main()
    
