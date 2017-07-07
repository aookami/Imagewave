# The Python Imaging Library (PIL) is
#   Copyright  1997-2011 by Secret Labs AB
#   Copyright  1995-2011 by Fredrik Lundh
#
# Pillow is the friendly PIL fork. It is
#
#   Copyright  2010-2017 by Alex Clark and contributors
#
#




from PIL import Image
import numpy
from numpy import random
from time import gmtime, strftime

fcalled = "f"


def contrast(imf, offset):
    global fcalled
    "this makes the contrast hard"
    fcalled = fcalled + "contrast" + str(offset)
    imc = imf
    size = imo.size
    width, height = size
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            r, g, b = imc.getpixel((x, y))
            if r > 125:
                r = r * (1 + offset)
            else:
                r = r * (1 - offset)
            if g > 125:
                g = g * (1 + offset)
            else:
                g = g * (1 - offset)
            if b > 125:
                b = b * (1 + offset)
            else:
                b = b * (1 - offset)
            imf.putpixel((x, y), (int(r), int(g), int(b)))
    print("done contrast")


def blur(imf):
    global fcalled
    fcalled = fcalled + "blur"
    imb = imf
    size = imo.size
    width, height = size
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            r1, g1, b1 = imb.getpixel((x - 1, y - 1))
            r2, g2, b2 = imb.getpixel((x - 1, y + 1))
            r3, g3, b3 = imb.getpixel((x - 1, y))
            r4, g4, b4 = imb.getpixel((x + 1, y - 1))
            r5, g5, b5 = imb.getpixel((x + 1, y + 1))
            r6, g6, b6 = imb.getpixel((x + 1, y))
            r7, g7, b7 = imb.getpixel((x, y + 1))
            r8, g8, b8 = imb.getpixel((x, y - 1))
            rt = (r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8) / 8
            gt = (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8) / 8
            bt = (b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8) / 8
            imf.putpixel((x, y), (int(rt), int(gt), int(bt)))
    print("done blur")


def addRGB(imf, value):
    global fcalled
    fcalled = fcalled + "addRGB" + str(value)
    size = imf.size
    width, height = size
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            r, g, b = imf.getpixel((x, y))
            r = r + value
            g = g + value
            b = b + value
            imf.putpixel((x, y), (int(r), int(g), int(b)))
    print("doneaddRGB")


def biggerelsemid(imf):
    global fcalled, b, g, r, y

    size = imf.size
    width, height = size

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            r, g, b = imf.getpixel((x, y))

            if r >= g and r >= b:
                g = 125
                b = 125
            elif g >= r and g >= b:
                b = 125
                r = 125
            elif b >= r and b >= g:
                r = 125
                g = 125
        imf.putpixel((x, y), (int(r), int(g), int(b)))
    fcalled = fcalled + "biggerelsemid"
    print("done biggerelsemid")

def camerafilter(imf,delta,mul):
    global fcalled
    size = imf.size
    width, height = size

    for i in range(1, int(height)-1):
       for j in range(1, int(width)-1):
            #print( str(i) + " " + str(j) + " " + str(size))
            r, g, b = imf.getpixel((j, i))
            r = r + delta * numpy.sin(i*mul)
            g = g + delta * numpy.sin(i*mul)
            b = b + delta * numpy.sin(i*mul)
            imf.putpixel((j, i), (int(r), int(g), int(b)))

    fcalled = fcalled + "camerafilter"
    print("donecamerafilter")
def blackandwhite(imf, val):
    global fcalled

    size = imf.size
    width, height = size

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            r, g, b = imf.getpixel((x, y))
            if r > val or b > val or g > val:
                r = 255
                b = 255
                g = 255
            else:
                r, g, b = (0, 0, 0)

            imf.putpixel((x, y), (int(r), int(g), int(b)))
    fcalled = fcalled + "bnwv" + str(val)
    print("done bnw")


def fuzz(imf):
    global fcalled
    ima = imf
    size = imf.size
    width, height = size
    widthi = width
    heighti = height
    array = numpy.zeros((width, height))
    for i in range(1, width):
        for j in range(1, height):
            x = int(int(widthi) * random.random())
            y = int(heighti * random.random())
            while (array[x][y] == 1):
                x = int(widthi * random.random())
                y = int(heighti * random.random())

            array[x][y] = 1

            if (x > width):
                x = width
            if (y > height):
                y = height
            r, g, b = ima.getpixel((i, j))
            imf.putpixel((x, y), (int(r), int(g), int(b)))
    fcalled = fcalled + "fuzz"


def getmeancolor(imf):
    global fcalled
    ima = imf
    size = imf.size
    width, height = size
    rtotal = 0
    gtotal = 0
    btotal = 0

    for i in range(0, width):
        for j in range(0, height):
            r, g, b = imf.getpixel((i, j))
            rtotal = rtotal + r
            gtotal = gtotal + g
            btotal = btotal + b

    rtotal = rtotal / (width * height)
    gtotal = gtotal / (width * height)
    btotal = btotal / (width * height)

    for i in range(1, width):
        for j in range(1, height):
            #imf.putpixel((i, j), (255, 255, 255))
             imf.putpixel((i, j), (rtotal, gtotal, btotal))

    fcalled = fcalled + "mean"


def split(imf, val):
    global fcalled
    listsmallimages = []
    size = imf.size
    width, height = size
    m = 0
    k = 0

    for x in range(0, (val * val)):
        if m == val:
            m = 0
            k = k + 1

        ims = Image.new("RGB", (width / val, height / val), color=(255, 255, 255))
        for i in range(((m) * (width / val)), ((m + 1) * (width / val))):
            for j in range(((k) * (height / val)), ((k + 1) * (height / val))):
                r, g, b = imf.getpixel((i, j))
                ims.putpixel((i - ((m) * (width / val)), j - ((k) * (height / val))), (int(r), int(g), int(b)))
        listsmallimages.append(ims)
        m = m + 1

    fcalled = fcalled + "split" + str(val)
    print("done split")
    return listsmallimages


def restore(listsmallimages, imf, val):
    global fcalled
    size = imf.size
    width, height = size

    c = 0
    f = 0
    random.shuffle(listsmallimages)
    while listsmallimages:
        imso = listsmallimages[0]
        listsmallimages.pop(0)
        sizeo = imso.size
        num = int(4 * random.random())
        num = num * 90
        # imso = imso.rotate(num, expand=0)
        #getmeancolor(imso)

        if (c == val):
            c = 0
            f = f + 1
        if (f == val):
            f = 0
        for i in range(0, (width / val)):
            for j in range(0, (height / val)):
                r, g, b = imso.getpixel((i, j))
                # print(str(i) + " " + str(j) + str(imso.size)+ " " +str((c * (width / val)) + i) + " "+ str(((f * height / val)) + j))
                imf.putpixel(((c * (width / val)) + i, ((f * height / val)) + j), (r, g, b))
        c = c + 1
    fcalled = fcalled + "restore"
    print("done restore")


imagename = "Amelie"
imo = Image.open(imagename + ".jpg")
im = imo

valin =2
camerafilter(im,255,1)

im.save(strftime("%Y%m%d%H%M%S", gmtime()) + imagename + ".jpeg")
