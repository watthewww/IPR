from PIL import Image
def crop_by_half(image_path, output_path):
    image = Image.open(image_path)
    left = 40
    top = 40
    right = 100
    bottom = 100
    cropped_img = image.crop((left, top, right, bottom))
    cropped_img.save(output_path)
    
crop_by_half('6103.png', 'cropped.png')