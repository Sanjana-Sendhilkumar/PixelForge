from PIL import Image  # importing image from pillow

# accepting the image's name
image_name = input("Enter the name of the image along with it's format: ")

# opening the original image in RGB
img = Image.open(image_name).convert("RGB")

# checking the dominant colour of the original image:
# The dominant colour is determined by comparing the average intensities of red, green, and blue values of all pixels, and selecting the highest one.
# Loads the pixel data of the image so that individual pixels can be accessed.
pixels_rgb = img.load()
width, height = img.size  # Getting the height and width of the image in pixels

total_red = total_green = total_blue = 0  # intialising the variables

for x in range(width):
    for y in range(height):
        r, g, b = pixels_rgb[x, y]
        total_red += r
        total_green += g
        total_blue += b

number_pixels = width * height  # calculates the total number of pixels in the image

avg_red = total_red / number_pixels
avg_green = total_green / number_pixels
avg_blue = total_blue / number_pixels

# checking the intensities using loops
if avg_red > avg_green and avg_red > avg_blue:
    dominant_color = "Red"
elif avg_green > avg_red and avg_green > avg_blue:
    dominant_color = "Green"
else:
    dominant_color = "Blue"

print("Dominant colour of original image:", dominant_color)

# Grayscale conversion
gray_img = img.convert("L")
gray_img.save("grayscale_image.png")

# Counting the B&W pixels
pixels_gray = gray_img.load()
black_pixels = 0
white_pixels = 0

for x in range(width):
    for y in range(height):
        if pixels_gray[x, y] == 0:
            black_pixels += 1
        elif pixels_gray[x, y] == 255:
            white_pixels += 1

print("Black pixels:", black_pixels)
print("White pixels:", white_pixels)

# Increasing the resolution using Image.Bicubic for a smoother image
high_res_img = gray_img.resize((width * 2, height * 2), Image.BICUBIC)
high_res_img.save("grayscale_high_resolution.png")

print("Grayscale and high-resolution images saved successfully.")
gray_img.show()
high_res_img.show()
img.show()
