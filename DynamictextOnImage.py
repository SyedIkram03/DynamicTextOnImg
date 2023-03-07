
# # putTextOnImage
# Add text in center aligment on image using Python.

# # Installation 
# (sudo) pip3 install pil

# # Run file
# pyhton3 putTextOnImage.py


# import required classes
 
from PIL import Image, ImageDraw, ImageFont
 
# create Image object with the input image
 
image = Image.open('HappyBirthday.png')
 
# initialise the drawing context with
# the image object as background
 
draw = ImageDraw.Draw(image)
# create font object with the font file and specify
# desired size
 
font = ImageFont.truetype('PainterPersonalUseOnly-Br0w.ttf', size=48)
 
# starting position of the message
 
# (x, y) = (250, 250)
# message = "Happy Birthday!"
# color = 'rgb(0, 0, 0)' # black color
# # draw the message on the background
# draw.text((x, y), message, fill=color, font=font)

(x, y) = (285, 525)
name = 'Syed Ikram Uddin '
# color = 'rgb(255, 255, 255)' # white color
color = 'rgb(0,0,0)' # Black color

draw.text((x, y), name, fill=color, font=font)
 
# save the edited image
 
image.save('greeting_card.png')