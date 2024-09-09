from PIL import Image

image = Image.open('original.jpg')
rgb_image = image.convert('RGB')
red, green, blue = rgb_image.split()

shift = 50

coordinates_red_left = (shift, 0, red.width, red.height)
coordinates_blue = (shift / 2, 0, blue.width - (shift / 2), blue.height)
red_cropped_left = red.crop(coordinates_red_left)
blue_cropped = blue.crop(coordinates_blue)
red_blend_left = Image.blend(red_cropped_left, blue_cropped, 0.3)

coordinates_blue_right = (0, 0, blue.width - shift, blue.height)
coordinates_red = (shift / 2, 0, red.width - (shift / 2), red.height)
blue_cropped_right = blue.crop(coordinates_blue_right)
red_cropped = red.crop(coordinates_red)
blue_blend_right = Image.blend(red_cropped, blue_cropped_right, 0.7)

coordinates_green = (shift / 2, 0, green.width - (shift / 2), green.height)
green_cropped = green.crop(coordinates_green)

new_image = Image.merge('RGB', (red_blend_left, green_cropped, blue_blend_right))
new_image.thumbnail((80,80))
new_image.save('result.jpg')