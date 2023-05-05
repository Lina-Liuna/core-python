import os
import cv2
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import imagehash
import time
import pysrt


def get_encode(pic_name):
    return imagehash.phash(Image.open(pic_name))


def is_similar_pic(pic1, pic2):
    hash0 = imagehash.average_hash(Image.open(pic1))
    hash1 = imagehash.average_hash(Image.open(pic2))
    cutoff = 10  # maximum bits that could be different between the hashes.
    if hash0 - hash1 < cutoff:
        return True
    else:
        return False


video = "/Users/lina/Documents/youtube/pbs/superwhy.mp4"
pic_dir = "/Users/lina/Documents/youtube/pbs/1/"
new_pic_dir = "/Users/lina/Documents/youtube/pbs/superwhy/"
srt = "/Users/lina/Documents/youtube/pbs/superwhy.srt"
ttf = "/Users/lina/Documents/youtube/ttf/Kartooni.ttf"



def write_srt_to_img(pic, ttf, text, output):
    img = Image.open(pic)
    width, height = img.size
    #print(width, height)
    draw = ImageDraw.Draw(img)
    font_size = 28
    font = ImageFont.truetype(ttf, font_size)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((55, height - 100), text, (240, 98, 242), font=font)
    img.save(output)

def write_embellish_text_to_image(pic, ttf, caption, output):
    # Open the image and grab its dimensions
    image = Image.open(pic)
    w = image.width
    h = image.height

    # Use a more interesting font
    #font = ImageFont.truetype(ttf, 80) #1080
    font = ImageFont.truetype(ttf, 50) #360

    # Instantiate draw object & be sure to set RGBA mode for transparency support
    draw_object = ImageDraw.Draw(image, 'RGBA')

    # Get the dimensions of the text for dynamic placement
    text_w, text_h = draw_object.textsize(caption, font=font)

    # Draw a rectangle and place text on it
    draw_object.rectangle([(0, 0.85 * h - 1.2 * text_h), (w, 0.85 * h + 1.2 * text_h)], fill=(255, 255, 255, 150),
                          outline=None, width=0)
    draw_object.text(xy=((w - text_w) * 0.85, (h - text_h) * 0.85), text=caption, fill=(240, 98, 242), font=font)

    # Preview the image
    #image.show()

    # Save the image
    image.save(output)

def extract_pic_by_time():
    vidcap = cv2.VideoCapture(video)

    success, image = vidcap.read()
    count = 0

    start_time = time.time()
    while success:
        success, image = vidcap.read()
        # print('Read a new frame: ', success)

        current_time = time.time()
        if (int(current_time - start_time) >= 0):
            cv2.imwrite(pic_dir + "%d.jpg" % count, image)
            count += 1
            start_time = current_time


def get_srt_milliseconds(srt):
    milliseconds = []
    sub = pysrt.open(srt)
    # Start and End time
    for i in range(0, len(sub)):
        start = sub[i].start.to_time()
        end = sub[i].end.to_time()
        if (sub[i].text == '[Music]'):
            continue
        start_millsecond = start.second * 1000 + start.minute * 1000 * 60 + start.hour * 1000 * 60 * 60
        end_millsecond = end.second * 1000 + end.minute * 1000 * 60 + end.hour * 1000 * 60 * 60
        millisecond = int((start_millsecond + end_millsecond) / 2)
        milliseconds.append(millisecond)
        # print(start.hour, start.minute, start.second, start.microsecond)
        # print(end)
    return milliseconds


def get_srt_text(srt):
    sub = pysrt.open(srt)
    texts = []
    for i in range(0, len(sub)):
        if sub[i].text == '[Music]':
            continue

        texts.append(sub[i].text)
        # print(start.hour, start.minute, start.second, start.microsecond)
        # print(end)
    return texts


def extract_pic(srt_time, srt_text, srt_ttf, output_pic_dir):
    vidcap = cv2.VideoCapture(video)
    success = True
    count = 0
    success, image = vidcap.read()
    cv2.imwrite(pic_dir + "%d.jpg" % count, image)
    second = 1
    count = count + 1

    for i in range(0, len(srt_time)):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, srt_time[i])  # optional
        success, image = vidcap.read()
        if success == True:
            cv2.imwrite(pic_dir + "%d.jpg" % (count), image)
            write_embellish_text_to_image(pic_dir + "%d.jpg" % (count), srt_ttf, srt_text[i], output_pic_dir + "%d.jpg" % (count))
        count = count + 1


time_arr = get_srt_milliseconds(srt)
text_arr = get_srt_text(srt)
print(time_arr)
extract_pic(time_arr, text_arr, ttf, new_pic_dir)
