import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

ttf_dir = '/Users/linaliu/books/fonts/KGPrimaryDots/'
font_name = 'KGPrimaryDotsLinedNOSPACE.ttf'
font_size = 126
image_dir = '/Users/linaliu/books/fonts/generate/allaboutme/'
# image_dir = '/Users/linaliu/books/fonts/generate/'
my_str = "ABCDEFGHIJKLMN"
my_str = "Too Many Cats Black Gray Rich Stray Any More Slinky Stinky Silly Chilly Furry Purry Hurry Nice Mean White Green All These They like one thing All these cats they like to sing"
#my_str = "This lives planet space king They"
# font = ImageFont.truetype("Arial-Bold.ttf",14)

def split_string_into_list(input_string, words_per_item):
    words = input_string.split()
    result = []
    for i in range(0, len(words), words_per_item):
        item = " ".join(words[i:i + words_per_item])
        result.append(item)
    return result
word_count = len(my_str.split())
words_list = split_string_into_list(my_str, 5)


font = ImageFont.truetype(ttf_dir + font_name, font_size)
(width, height) = (int(font_size * 0.65) * 15, 150 * len(words_list))
img_size = (width, height)
img=Image.new("RGBA", img_size,(255,255,255))
(update_width, update_height) = (width + 440, height + 30)
update_size = (update_width, update_height)
print(update_size)
new_im = Image.new("RGB", update_size, (255,255,255))  ## luckily, this is already black!
new_im.paste(img, (int((update_width - width) // 2), int((update_height - height) // 2)))
draw = ImageDraw.Draw(new_im)


count = 0
for words in words_list:
    words = words.replace(" ", "_")
    draw.text((20, 120 *count),words,(0,0,0),font=font)
    count += 1
    draw = ImageDraw.Draw(new_im)
print(my_str)
new_im = new_im.save(image_dir + my_str + ".png")