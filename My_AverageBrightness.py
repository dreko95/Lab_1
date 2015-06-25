# coding=utf-8
import PIL.Image
import urllib


def Getting_otrybutov(http_img):
    if '.jpg' in http_img:
        imgs = PIL.Image.open("logo.jpg")
    else:
        imgs = PIL.Image.open("logo.png")
    width = imgs.size[0]
    height = imgs.size[1]
    pix = imgs.load()
    return AverageBrightness(pix, width, height)


def Upload_pictures(http_img):
    logo = urllib.urlopen(http_img).read()
    if '.jpg' in http_img:
        f = open("logo.jpg", "wb")
    else:
        f = open("logo.png", "wb")
    f.write(logo)
    f.close()


def AverageBrightness(pix, width, height):
    S = 0
    # print "::::::::::::::::", pix
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = ((a + b + c) // 3) + S
    S = S // (width * height)
    return S
