#import PIL             #PIL.Image
from PIL import Image   #Image

#Image.open("starr_bears.jpg")
filepath = "starr_bears.jpg"
orig_img = Image.open(filepath)

#print(orig_img.size)
#img_size = orig_img.size   (1560, 811)
#print(img_size[0])
#print(img_size[1])
width, height = orig_img.size
mode = orig_img.mode

orig_img_map = orig_img.load()

# Create a new image
new_img = Image.new(mode, (width, height))
new_img_map = new_img.load()

brightness = 2
for x in range(width):
    for y in range(height):
        orig_r, orig_g, orig_b = orig_img_map[x, y]
        new_pixel = (int(brightness * orig_r), \
                     int(brightness * orig_g), \
                     int(brightness * orig_b))
        new_img_map[x, y] = new_pixel

# Display the temporary image
new_img.show()

