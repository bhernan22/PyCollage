from PIL import Image
#from imageFinder import ImageSearch
// making a comment to test ssh key

HOR = 100
VER = 100


def main():
    
    
    im = Image.open("test.jpg")
    width, height = im.size
    print width, height
    query = raw_input('What type of images would you like to fill with?')
    HOR = raw_input('How many boxes X')
    VER = raw_input('How many boxes Y')
    ImageSearch(query, 'temps')
    regions = cutBox(im)

def cutBox(im):
    startX = 0
    startY = 0
    endX = HOR
    endY = VER
    width, height = im.size
    regions = []
    while endX < width:
        while endY < height:
            
            box = (startX, startY, endX, endY)
            region = im.crop(box)
            regions.append(region)
            startY += VER
            endY += VER
        startY = 0
        endY = VER
        startX += HOR
        endX += HOR
 
    return regions

def findAverageColor(im):#This is all Jelly!!
    red = 0
    green = 0
    blue = 0

    x, y = im.size # gets height and width
    count = 0 

    pixels = im.load()
    for i in range(x):
        for j in range(y):
            tempr,tempg,tempb = pixels[i,j]
            red += tempr
            green += tempg
            blue += tempb
            count += 1

    avgRed = red/count
    avgGreen = green/count
    avgBlue = blue/count
    return(avgRed, avgGreen, avgBlue)

def pixConverter(lis):
    ColorDigits = []
    for pix in lis:
        ColorDigits.append(findAverageColor(pix))
    return ColorDigits

#main()


#findAverageColor(im)
