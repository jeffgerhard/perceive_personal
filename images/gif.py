# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:44:22 2017

@author: jcg
"""

import imageio
import pyperclip
import os

pause = input('select files')
filenames = pyperclip.paste().splitlines()
images = []
for filename in filenames:
    f = filename.strip('"')
    images.append(imageio.imread(f))
name = input('name this gif:')
imageio.mimsave(name, images, duration=5)