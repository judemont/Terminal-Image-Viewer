from colored import fg
from PIL import Image
from terminalImgViewer.lib import reduce_resolution

CHAR = "■"

def display(image_name, width):
    im = reduce_resolution(Image.open(image_name).getdata().convert("RGB"), width)
    result = ""

    for i, pixel in enumerate(im):
        color = fg('#%02x%02x%02x' % pixel)
        result += color + CHAR * 2

        if (i + 1) % im.size[0] == 0:
            result += "\n"

    print(result)
