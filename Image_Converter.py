from PIL import Image
import re
import os

# Open the path given by the user
# img = Image.open('./eevee.jpg')
# print(img)

# print(os.listdir('.\\'))

new_dir = os.path.relpath('.\\new\\')
main_dir = os.listdir('.\\')
pokedex = os.listdir('.\\pokedex\\')
dir_path = 'D:\\Learn Python\images\\image_playground\\pokemon\\pokedex\\new\\'

print(pokedex)
#
# try:
#     if new_dir in main_dir:
#         pass
#     else:
#         os.mkdir('.\\new\\')
# except FileExistsError as err:
#     print('The file already exist.')
#
for images in pokedex:
    img = Image.open(f'{pokedex}{images}')
    img.save(dir_path, "png")
