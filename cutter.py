#!/usr/bin/python

import os, sys
from PIL import Image

print("""

//  ████████╗██╗    ██╗██╗████████╗████████╗███████╗██████╗      
//  ╚══██╔══╝██║    ██║██║╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗██╗  
//     ██║   ██║ █╗ ██║██║   ██║      ██║   █████╗  ██████╔╝╚═╝  
//     ██║   ██║███╗██║██║   ██║      ██║   ██╔══╝  ██╔══██╗██╗  
//     ██║   ╚███╔███╔╝██║   ██║      ██║   ███████╗██║  ██║╚═╝  
//     ╚═╝    ╚══╝╚══╝ ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝     
//   ██████╗  ██╗ ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗     
//  ██╔═══██╗███║██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║     
//  ██║██╗██║╚██║██║     ███████║███████║██████╔╝█████╗  ██║     
//  ██║██║██║ ██║██║     ██╔══██║██╔══██║██╔══██╗██╔══╝  ██║     
//  ╚█║████╔╝ ██║╚██████╗██║  ██║██║  ██║██║  ██║███████╗███████╗
//   ╚╝╚═══╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
//                                                               

""")

def process(filename):
  def centercrop(image):
    width, height = image.size

    
    
    left = 0
    top = 0
    right = width
    bottom = height - number

    img = image.crop((left, top, right, bottom))
    return img
  try:
    im = Image.open(filename)
    im = centercrop(im)
    im.save(filename)
    print("cropped", filename)
  except IOError:
    pass
number = int(input("Enter how many pixels to shorten from the bottom: "))
path = input("Enter the path to the folder: ")
dirs = os.listdir(path)

for file in dirs:
  process(path + "/" + file)