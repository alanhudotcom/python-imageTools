#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
# /usr/local/lib/python3.4/site-packages/PIL
from PIL import Image
import sys
from ListImage import ListImage

param = {
    'bigSize': 20 * 1024,
    'baseDir': os.path.abspath('.')
}

def is_big_image(image):
    with Image.open(image) as im:
        return os.stat(image).st_size >= param['bigSize']

if __name__ == '__main__':
    
    def paseBaseDirParm(args):
        if len(args) >= 2:
            param['baseDir'] = args[1]
            print("from input baseDir: %s" % param['baseDir'])

    def parseBigSizePram(args):
        if len(args) >= 3:
            in_size = int(args[2])
            param['bigSize'] = in_size * 1024
            print("from input bigSize: %d" % in_size)

    paseBaseDirParm(sys.argv)
    parseBigSizePram(sys.argv)
    
    print('===params baseDir: %s, bigSize:%d' % (param['baseDir'], param['bigSize']/1024))
    listImage = ListImage(param['baseDir'])

    imageFiles = listImage.images()

    bigSizeFiles = list(filter(is_big_image, imageFiles))

    print('===jpg or webp %d files ------------------------->' % len(bigSizeFiles))
    print(bigSizeFiles)


