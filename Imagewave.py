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
import operator
import time

fcalled = "f"


def contrast(imf, offset):
    global fcalled
    "this makes the contrast hard"
    fcalled = fcalled + "contrast" + str(offset)
    imc = imf
    size = imo.size
    width, height = size
    for x in range(1, height - 1):
        for y in range(1, width- 1):
            r, g, b = imc.getpixel((y, x))
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
            imf.putpixel((y, x), (int(r), int(g), int(b)))
    print("done contrast")


def blur(imf):
    global fcalled
    fcalled = fcalled + "blur"
    imb = imf
    size = imo.size
    width, height = size

    for y in range(1, height - 1):
        for x in range(1, width - 1):
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
    for y in range(1, height - 1):
        for x in range(1, width - 1):
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

    for y in range(1, height - 1):
        for x in range(1, width - 1):

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


def camerafilter(imf, delta, mul):
    global fcalled
    size = imf.size
    width, height = size

    for i in range(1, int(height) - 1):
        for j in range(1, int(width) - 1):
            # print( str(i) + " " + str(j) + " " + str(size))
            r, g, b = imf.getpixel((j, i))
            r = r + delta * numpy.sin(i * mul)
            g = g + delta * numpy.sin(i * mul)
            b = b + delta * numpy.sin(i * mul)
            imf.putpixel((j, i), (int(r), int(g), int(b)))

    fcalled = fcalled + "camerafilter"
    print("donecamerafilter")


def blackandwhite(imf, val):
    global fcalled

    size = imf.size
    width, height = size
    for y in range(1, height - 1):
        for x in range(1, width - 1):
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
    for j in range(1, height):
        for i in range(1, width):
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
    for j in range(0, height):
        for i in range(0, width):
            r, g, b = imf.getpixel((i, j))
            rtotal = rtotal + r
            gtotal = gtotal + g
            btotal = btotal + b

    rtotal = rtotal / (width * height)
    gtotal = gtotal / (width * height)
    btotal = btotal / (width * height)

    for j in range(1, height):
        for i in range(1, width):
            # imf.putpixel((i, j), (255, 255, 255))
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
        for j in range(((k) * (height / val)), ((k + 1) * (height / val))):
            for i in range(((m) * (width / val)), ((m + 1) * (width / val))):
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
        # getmeancolor(imso)

        if (c == val):
            c = 0
            f = f + 1
        if (f == val):
            f = 0
        for j in range(0, (height / val)):
            for i in range(0, (width / val)):
                r, g, b = imso.getpixel((i, j))
                # print(str(i) + " " + str(j) + str(imso.size)+ " " +str((c * (width / val)) + i) + " "+ str(((f * height / val)) + j))
                imf.putpixel(((c * (width / val)) + i, ((f * height / val)) + j), (r, g, b))
        c = c + 1
    fcalled = fcalled + "restore"
    print("done restore")


def displacelayer(imf, angler, angleg, angleb, valr, valg, valb, mul, mulorig):
    global fcalled
    size = imf.size
    width, height = size


    # split imf into 3 images with only its rgb values
    imr = Image.new("RGB", (width,height),color = 0)
    imb = Image.new("RGB", (width,height),color = 0)
    img = Image.new("RGB", (width,height),color = 0)
    for j in range(0, height):
        for i in range(0, width):
            r, g, b = imf.getpixel((i, j))
            r = int(r*  mul)
            b = int(b * mul)
            g = int(g * mul)
            imr.putpixel((i, j),  (r, 0, 0))
            img.putpixel((i, j), (0, g, 0))
            imb.putpixel((i, j), (0, 0, b))
    print("acabou o split")

    # criar with 3 times the original image size (theres no point in printing further away than that
    canvas = Image.new("RGB", (width * 3, height * 3), color=0)






    # print the original image in the canvas middle
    size2 = canvas.size
    widthc, heightc = size2
    if mulorig != 0:
        for j in range(heightc / 3, (2 * heightc) / 3):
            for i in range(widthc / 3, (2 * widthc) / 3):
                #print(str(i) + " " + str(j))
                (r2, g2, b2) = imf.getpixel((i - (widthc / 3), j - (heightc / 3)))
                r2 = r2 * mulorig
                g2 = g2 * mulorig
                b2 = b2 * mulorig
                #print(str(((r2, g2, b2))))
                canvas.putpixel((i, j), (r2, g2, b2))


    #acertar os x e y de acordo com as  coordenadas polares, os angulos sao em radianos (float) e a distancia em pixel

    x = widthc/3
    y = heightc/3

    xr = x + numpy.cos(angler)*valr
    yr = y + numpy.sin(angler)*valr

    xg = x + numpy.cos(angleg) * valg
    yg = y + numpy.sin(angleg) * valg

    xb = x + numpy.cos(angleb) * valb
    yb = y + numpy.sin(angleb) * valb

    #somar cada layer separada
    for j in range(0, height):
        for i in range(0, width):

            (rr, gr, br) = imr.getpixel((i,j))
            tur =canvas.getpixel((xr+i, yr+j))
            saver = tuple(map(operator.add, (rr, gr, br), tur))
            canvas.putpixel((int(xr+i),int(yr+j)),saver)

            (rb, gb, bb) = imb.getpixel((i, j))
            tub = canvas.getpixel((xb + i, yb + j))
            saveb = tuple(map(operator.add, (rb, gb, bb), tub))
            canvas.putpixel((int(xb + i), int(yb + j)), saveb)

            (rg, gg, bg) = img.getpixel((i, j))
            tug = canvas.getpixel((xg + i, yg + j))
            saveg = tuple(map(operator.add, (rg, gg, bg), tug))
            canvas.putpixel((int(xg + i), int(yg + j)), saveg)

    #copiar o canvas pro original
    for j in range(0, height):
        for i in range(0, width):
            tuple2 = canvas.getpixel((i+widthc/3,j+heightc/3))
            imf.putpixel((i,j),tuple2)


    fcalled = fcalled + "disl"
    print("done displace")


def glitch(imf, pct, val):
    global fcalled
    size = imf.size
    width, height = size

    # criar with 3 times the original image size (theres no point in printing further away than that
    canvas = Image.new("RGB", (width * 3, height * 3), color=0)

    # print the original image in the canvas middle
    size2 = canvas.size
    widthc, heightc = size2
    #if mulorig != 0:
     #   for i in range(widthc / 3, (2 * widthc) / 3):
      #      for j in range(heightc / 3, (2 * heightc) / 3):
       #         # print(str(i) + " " + str(j))
        #        (r2, g2, b2) = imf.getpixel((i - (widthc / 3), j - (heightc / 3)))
         #       # print(str(((r2, g2, b2))))
          #      canvas.putpixel((i, j), (r2, g2, b2))

    #use the pct as % chance of dislodging a  line by the val value
    randomvalue = random.random()*100
    randompct = random.random()*pct
    for i in range(heightc / 3, (2 * heightc) / 3):
        randomvalue = random.random() * 100
        randompct = random.random() * pct
        if randomvalue > randompct:
            for j in range(widthc / 3, (2 *widthc) / 3):
                tupleimf = imf.getpixel((j-(widthc/3),i-(heightc/3)))
                canvas.putpixel((j,i), tupleimf)
        else:
            for j in range(widthc / 3, (2 * widthc) / 3):
                tupleimf = imf.getpixel((j - (widthc / 3), i - (heightc / 3)))
                canvas.putpixel((int((j+(val*numpy.sin(i)))), i), tupleimf)
    #done glitch
    #now just copy canvas to the original image

    for i in range(0, width):
        for j in range(0, height):
            tuple2 = canvas.getpixel((i+widthc/3,j+heightc/3))
            imf.putpixel((i,j),tuple2)

    fcalled = fcalled + "glitch" + str(pct)
    print("done glitch")

t0 = time.time()
imagename = "vroom.jpg"
imo = Image.open(imagename)
im = imo

valin = 2
restore(split(im,2),im,2)
displacelayer(im, 0, 0, 0, -60, 0, 60, 1, 0)
camerafilter(im, 10, 3)
glitch(im,50,100)
t1 = time.time()

print(str(t1-t0))
im.save(strftime("%Y%m%d%H%M%S", gmtime()) + imagename + ".jpeg")
