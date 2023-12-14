from PIL import Image

def reduce_resolution(img, new_width):
    width, height = img.size
    reduction_factor = new_width / width
    new_height = int(height * reduction_factor)
    img = img.resize((new_width, new_height), Image.BOX)
    
    return img
