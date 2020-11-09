import urllib.request
import random
import os
from PIL import Image, ImageOps, ImageDraw, ImageFont
def wrap_by_word(s, n):
    '''returns a string where \\n is inserted between every n words'''
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\n'

    return ret

def dl_image():
    img_url = "https://source.unsplash.com/random/2560x1080"
    img_name = os.path.basename(img_url)
    urllib.request.urlretrieve(img_url,img_name + '.jpg')#save pic into folder
    print('Downloading image {}'.format(img_name + '.jpg'))


def get_quote():
    quote_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'quotes.txt')
    f = open(quote_file, 'r')
    txt = f.read()
    lines = txt.split('\n.\n')
    text_out = random.choice(lines)
    print(text_out)
    return text_out

def resize_ig_image():
    image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '2560x1080.jpg')
    im = Image.open(image_file)
    out = im.resize((1080,1080))
    #save resized image
    out.save('resize-output.png')

def crop_ig_image():
    image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '2560x1080.jpg')
    im = Image.open(image_file)
    croppedImage = im.crop((1,2,1080,1080))
    croppedImage.save('cropped-output.png')


def add_border():
    image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cropped-output.png')
    im = Image.open(image_file).convert("RGBA")
    im_x, im_y = im.size

    image_file_bg = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bginsta.jpg')
    background = Image.open(image_file_bg).convert("RGBA")

    background_x, background_y = background.size

    x = int((background_x-im_x)/2)
    y = int((background_y-im_y)/2)

    background.paste(im, (x, y), im)
    background.save('overlayed_image.png',"PNG")

def greyscale_ig():
    image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cropped-output.png')
    im = Image.open(image_file).convert("RGBA")
    gray_image = ImageOps.grayscale(im)

    gray_image.save('greyscaled.png',"PNG")


def text_overlay_ig(quotation):
    image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'greyscaled.png')
    im = Image.open(image_file).convert("RGBA")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('KOMIKAX_.ttf', size=60)
    font_author = ImageFont.truetype('KOMIKAX_.ttf', size=30)
    # starting position of the message
    (quote,author) = quotation.split('- ')
    quote.strip('-')
    quote = wrap_by_word(quote, 4)
    
    (x, y) = (50, 50)
    message = quote
    color = 'rgb(206, 0, 240)' # black color
    # draw the message on the background
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (50, 1000)
    name = " - " + author
    color = 'rgb(255, 255, 255)' # white color
    draw.text((x, y), name, fill=color, font=font_author)
    im.save('text_overlay.png')

dl_image()
quotation = get_quote()
resize_ig_image()
crop_ig_image()
add_border()
greyscale_ig()
text_overlay_ig(quotation)

