#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
# /usr/local/lib/python3.4/site-packages/PIL
from PIL import Image
import sys
from ListImage import ListImage

action_st_size = 0
action_image_size = 1
action_and_size = 2
param = {
    'st_size': 20 * 1024,
    'image_size': 100,
    'baseDir': os.path.abspath('.'),
    'action': 0
}

def is_big_st_size(image):
    return os.stat(image).st_size >= param['st_size']

def is_big_image_size(image):
    with Image.open(image) as im:
        (width, height) = im.size
        return width >= param['image_size'] and height >= param['image_size']

def is_and_big_size(image):
    return is_big_st_size(image) and is_big_image_size(image)

if __name__ == '__main__':
    
    paramDir = input('please enter baseDir: ')
    if paramDir:
        param['baseDir'] = paramDir

    param['action'] = int(input('please enter action, 0: st_size, 1: image_size, 2: 0 and 1 >>> '))
    if param['action'] == action_st_size:
        try:
            param['st_size'] = int(input('please enter st_size: ')) * 1024
        except Exception as e:
            pass

    if param['action'] == action_image_size:
        try:
            param['image_size'] = int(input('please enter image_size: '))
        except Exception as e:
            pass

    if param['action'] == action_and_size:
        try:
            param['st_size'] = int(input('please enter st_size: ')) * 1024
        except Exception as e:
            pass
        
        try:
            param['image_size'] = int(input('please enter image_size: '))
        except Exception as e:
            pass
    
    print('===params baseDir: %s, action:%d, st_size:%d, image_size:%d' % (param['baseDir'], param['action'], param['st_size']/1024, param['image_size']))
    listImage = ListImage(param['baseDir'])

    imageFiles = listImage.images()

    if param['action'] == action_st_size:
        imageFiles = list(filter(is_big_st_size, imageFiles))

    elif param['action'] == action_image_size:
        imageFiles = list(filter(is_big_image_size, imageFiles))

    else:
        imageFiles = list(filter(is_and_big_size, imageFiles))


    print('===jpg or webp %d files ------------------------->' % len(imageFiles))
    print(imageFiles)


