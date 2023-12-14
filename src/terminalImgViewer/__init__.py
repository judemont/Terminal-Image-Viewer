from colored import fg
from PIL import Image
from terminalImgViewer.lib import reduce_resolution

CHAR = "■"

def display(image_name, width):
    im = reduce_resolution(Image.open(image_name).getdata().convert("RGB"), width)
    result = ""

    for i in range(0, len(im)):
        color = fg('#%02x%02x%02x' % im[i])
        if i % im.size[0] == 0 and i != 0:
            result += "\n"
        else:
            result += color + CHAR * 2
    print(result)
