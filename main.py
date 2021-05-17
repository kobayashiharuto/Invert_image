import tkinter.messagebox
import tkinter.filedialog
import tkinter
import os
from PIL import Image, ImageFont, ImageDraw, ImageOps

tkinter.Tk().withdraw()
directory_name = tkinter.filedialog.askdirectory(
    initialdir=os.path.abspath(os.path.dirname(__file__)))

files = os.listdir(directory_name)

for file in files:
    if file == '.DS_Store':
        continue
    print(directory_name + '/' + file)
    im = Image.open(directory_name + '/' + file).convert('RGB')
    ImageOps.invert(im).save(
        directory_name + '/' + file, quality=95)
