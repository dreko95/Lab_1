# coding=utf-8
from xml.etree import ElementTree
import time
import urllib
import xml.etree.cElementTree as ET
import pydoc
import BeautifulSoup
import My_AverageBrightness


def shades_of_brightness_funk(brightness, shades_of_brightness):
    if brightness < 50:
        shades_of_brightness[0] = shades_of_brightness[0] + 1
    elif brightness < 100:
        shades_of_brightness[1] = shades_of_brightness[1] + 1
    elif brightness < 150:
        shades_of_brightness[2] = shades_of_brightness[2] + 1
    elif brightness < 200:
        shades_of_brightness[3] = shades_of_brightness[3] + 1
    elif brightness < 255:
        shades_of_brightness[4] = shades_of_brightness[4] + 1


# parse sait
def parse(html):
    shades_of_brightness = [0, 0, 0, 0, 0]
    soup = BeautifulSoup.BeautifulSoup(html)
    for img in soup.findAll('img'):
        if '.jpg' in img['src'] or '.png' in img['src']:
            My_AverageBrightness.Upload_pictures(img['src'])
            Bright = My_AverageBrightness.Getting_otrybutov(img['src'])
            shades_of_brightness_funk(Bright, shades_of_brightness)
    return shades_of_brightness


def get_html(url):
    response = urllib.urlopen(url).read()
    return response


def read_xml():
    e = ElementTree.parse('url_site.xml').getroot()
    print "e = ", e
    return [atype.text for atype in e.findall('url')]


def write_xml(html, brightness):
    root = ET.Element("root")

    for i, j in zip(html, brightness):
        url = ET.SubElement(root, "url")
        ET.SubElement(url, "text").text = i
        ET.SubElement(url, "diapason").text = '[<50,<100,<150,<200,<255]'
        ET.SubElement(url, "bright").text = str(j)

    tree = ET.ElementTree(root)
    tree.write("out_xml.xml")


def main():
    shades_of_brightness = []
    for html in read_xml():
        print('The site -- ', html)
        shades_of_brightness.append(parse(get_html(html)))
        print('pictures with the brightness')
        print('[<50,<100,<150,<200,<255]')
        print(shades_of_brightness)
    write_xml(read_xml(), shades_of_brightness)


if __name__ == '__main__':
    start = time.time()
    main()
    print ("program worker for ", time.time() - start)
