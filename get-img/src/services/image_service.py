from PIL import Image
import io
import os
from config import IMAGES_DIR, IMAGE_SIZE

def get_image_path(image_name):
    return os.path.join(IMAGES_DIR, image_name)

def resize_image(image_path):
    with Image.open(image_path) as img:
        img = img.resize(IMAGE_SIZE)
        img_io = io.BytesIO()
        img.save(img_io, 'JPEG')
        img_io.seek(0)
        return img_io
