import sys
import os
from PIL import Image


# sys.path.append(os.getcwd() + '/your/subfolder/of/choice')
width = 1000
height = 500
# image name should be with extension. test.jpeg
image = raw_input('What is the image name (with extension): ')
# directory name should be like: /Users/syedatique/Desktop
directory = raw_input('what is the directory path to scan: directory name should be like: /Users/syedatique/Desktop ')
# Open the image file.
img = Image.open(os.path.join(directory, image))
# Resize it.
img = img.resize((width, height), Image.BILINEAR)
# Save it back to disk.
print'saving resized image in the same directory'
img.save(os.path.join(directory, 'resized-' + image))
