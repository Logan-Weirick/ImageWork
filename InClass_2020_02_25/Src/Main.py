'''
Created on Feb 25, 2020

@author: weiricle
'''
from Image_Functions import *
im = Image.open("SiriusAndViolet.jpg")
print(im.width, im.height, im.mode, im.format)  # Display some info about the image

#my_image = load_image("SiriusAndViolet.jpg")
#my_image.show(my_image)

# Make use of crop_image
#Load an image 
#call crop_image and save what it returns
#Call show to display the results
im = Image.open("SiriusAndViolet.jpg")  
im_cropped = im.crop(im, (200,300,400,500)) # (left, top, right, bottom) it's a tuple!
im.show()