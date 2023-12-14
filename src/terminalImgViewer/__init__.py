from colored import fg
from PIL import Image
from terminalImgViewer.lib import reduce_resolution

CHAR = "■"

def getTerminalImage(image_path: str, width: int) -> str:
    im = reduce_resolution(Image.open(image_path).getdata().convert("RGB"), width)
    result = ""

    for i, pixel in enumerate(im):
        color = fg('#%02x%02x%02x' % pixel)
        result += color + CHAR * 2

        if (i + 1) % im.size[0] == 0:
            result += "\n"

    return result
