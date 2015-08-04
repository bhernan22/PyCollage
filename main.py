from PIL import Image

HOR = 25
VER = 25


def main():
    im = Image.open("test.jpg")
    width, height = im.size
    print width, height
    cutBox(im)

def cutBox(im):
    startX = 0
    startY = 0
    box = (startX, startY, HOR, VER)
    region = im.crop(box)
    findAverageColor(region)

def findAverageColor(im):#This is all Jelly!!
    red = 0
    green = 0
    blue = 0

    x = 0
    y = 0

    pixels = im.load()
    
    while(x < )

main()
