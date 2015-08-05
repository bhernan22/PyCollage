from PIL import Image
import os
import sys


def resize(path, folder, size):
    #print os.listdir(os.getcwd())
    
    directory = os.getcwd() + '/' + path + '/' + folder + '/'
    filenames =  os.listdir(directory)
    resized = []

    for images in filenames:
        im = Image.open(directory + images)
        #im.show()
        width, height = im.size
    
        if(width >= height):
            box = (0,0,height,height)
            im = im.crop(box)
        else:
            box = (0,0,width,width)
            im = im.crop(box)
        #im.show()
        im.thumbnail(size, Image.ANTIALIAS)
        resized.append(im)
        #im.show()
        #print im.size
    return resized


resize('temps', 'wallpapers', (75,75))
