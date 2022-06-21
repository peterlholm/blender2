"Generate structured image"
from pathlib import Path
from math import cos, pi
from PIL import Image

PICTURE_SIZE = 2000
FREQ = 10
PIC_PR_PERIOD = PICTURE_SIZE / FREQ
PIXEL_COLOR = (0,255,0)
DPI = (300, 300)
INCH = 25.4     # mm

_DEBUG = False

def create_dias(folder):
    "create the dias"
    grey = Image.new('L', (PICTURE_SIZE, PICTURE_SIZE) )
    greya = Image.new('LA', (PICTURE_SIZE, PICTURE_SIZE) )
    rgb = Image.new('RGB', (PICTURE_SIZE, PICTURE_SIZE) )
    rgba = Image.new('RGBA', (PICTURE_SIZE, PICTURE_SIZE) )

    for x in range(PICTURE_SIZE):
        val = x /PIC_PR_PERIOD * 2 * pi
        intens = cos(val)
        #print(val, intens)
        for y in range(PICTURE_SIZE):
            grey.putpixel((x,y), 128 + int(intens * 128 ))
            greya.putpixel((x,y), (100,128 + int(intens * 128 )))
            color = (0, int((1-intens) * 128),0)
            rgb.putpixel((x,y),color)
            rgba.putpixel((x,y), (0,255,0, int((1-intens) * 128)))
    savefolder = Path(folder)
    rgb.save(savefolder / "rgb.png", dpi=DPI)
    rgba.save(savefolder / "rgba.png")
    grey.save(savefolder / "grey.png", transparency=2)
    greya.save(savefolder / "greyA.png")
    # img.save("int.png","I")
    rgb.save(savefolder / "rbg.jpg", dpi=DPI)
    return rgb


def picture_size(imgfile):
    "get the physical size of picture"
    img = Image.open(imgfile)
    #img.load()
    dpi = img.info.get('dpi', None)
    if dpi:
        size = (img.width/dpi[0]*INCH, img.height/dpi[1]*INCH)
    else:
        size = None
    if _DEBUG:
        exif = img.getexif()
        print("Exif", exif)
        print(img.format, img.size, img.mode)
        print("dpi", dpi)
    return size

create_dias("tmp")

sz = picture_size('tmp/rgb.png')
print ("Size (mm)", sz)
