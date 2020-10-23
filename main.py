from os import listdir
from os.path import isfile, join
import os
from PIL import Image

man_input = input('masukan nama folder: ')
main = listdir(r'{}'.format(man_input))
data = []


for i in sorted(main):
    image = Image.open(r'../{}/{}'.format(man_input,str(i)))
    im = image.convert('RGB')
    data.append(im)

im.save(r'book/{}.pdf'.format(man_input), save_all=True, append_images=data)
