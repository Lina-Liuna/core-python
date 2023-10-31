from PIL import Image

def change_white_to_yellow(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    width, height = image.size

    new_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pixels = new_image.load()

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel == (255, 255, 255, 255):  # White color
                pixels[x, y] = (255, 195, 0, 255)  # Change to yellow
            else:
                pixels[x, y] = pixel

    new_image.save(output_image_path)

input_image_path = "/Users/linaliu/Documents/PGMovie.png"  # Specify your input PNG image file
output_image_path = "/Users/linaliu/Documents/PGMovie_orange_yellow.png"  # Specify the output PNG image file

change_white_to_yellow(input_image_path, output_image_path)




