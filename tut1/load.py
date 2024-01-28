from PIL import Image
def load_image(image_path):
    img = Image.open(image_path)
    img.show()
    
load_image('6103.png')