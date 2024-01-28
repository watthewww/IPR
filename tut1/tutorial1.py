from PIL import Image, ImageEnhance, ImageFilter
# load image
def load_image(image_path):
    img = Image.open(image_path)
    img.show()

# convert image to grayscale
def convert_to_grayscale(image_path, output_path):
    image = Image.open(image_path)
    grayscale_img = image.convert('L')
    grayscale_img.save(output_path)
    
# resize image 
def resize(height, width, image_path, output_path):
    image = Image.open(image_path)
    resized_image = image.resize((height, width))
    resized_image.save(output_path)
    
# crop image
def crop(image_path, output_path):
    image = Image.open(image_path)
    left = 40
    top = 40
    right = 100
    bottom = 100
    cropped_img = image.crop((left, top, right, bottom))
    cropped_img.save(output_path)
    
# adjust brightness
def adjust_brightness(image_path, output_path, factor):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(image)
    adjusted_img = enhancer.enhance(factor)
    adjusted_img.save(output_path)
  
# adjust contrast
def adjust_contrast(image_path, output_path, factor):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    adjusted_img = enhancer.enhance(factor)
    adjusted_img.save(output_path)  

# rotate image by 90 degree
def rotate_90(image_path, output_path):
    image = Image.open(image_path)
    rotated_img = image.rotate(90, Image.NEAREST, expand = 1)
    rotated_img.save(output_path)
    
# rotate image by 180 degree
def rotate_180(image_path, output_path):
    image = Image.open(image_path)
    rotated_img = image.rotate(180, Image.NEAREST, expand=1)
    rotated_img.save(output_path)
    
# flip horizontal
def flip_horizontal(image_path, output_path):
    image = Image.open(image_path)
    flipped_img = image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_img.save(output_path)

# flip vertical
def flip_horizontal(image_path, output_path):
    image = Image.open(image_path)
    flipped_img = image.transpose(Image.FLIP_TOP_BOTTOM)
    flipped_img.save(output_path)
    
# apply blur filter
def add_blur(image_path, output_path):
    image = Image.open(image_path)
    blurred_img = image.filter(ImageFilter.BLUR)
    blurred_img.save(output_path)
    
#apply sharpening filter
def add_sharpening(image_path, output_path):
    image = Image.open(image_path)
    sharpened_img = image.filter(ImageFilter.SHARPEN)
    sharpened_img.savee(output_path)
