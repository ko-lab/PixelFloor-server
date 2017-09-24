import sys
from PIL import Image
def clamp(x): 
  return max(0, min(x, 255))

if len(sys.argv) > 1: 
    image = sys.argv[1]
    imObj = Image.open(image)
    print imObj.size
    for x in xrange(imObj.size[0]):
        for y in xrange(imObj.size[1]):
            pixel =  imObj.getpixel((x,y))
            print"px " +str(x) + " "+ str(y)  +  str(" {0:02x}{1:02x}{2:02x}".format(clamp(pixel[0]), clamp(pixel[1]), clamp(pixel[2])))

