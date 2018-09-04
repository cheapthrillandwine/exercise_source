from PIL import Image
import sys

import pyocr
import pyocr.builders
import cv2
import numpy as np
tools = pyocr.get_available_tools()
if len(tools) == 0:
   print("No OCR tool found")
   sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.

# img ='images/gauge-22.jpg'
# src = cv2.imread(img, 1)
# gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

txt = tool.image_to_string(
   Image.open('images/gauge-22.jpg'),
   lang="eng",
   builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

detect_num = []

detect_num.append(txt)

print( detect_num[0] )
# txt is a Python string
