from PIL import Image
def resize(height, width, image_path, output_path):
    image = Image.open(image_path)
    resized_image = image.resize((height, width))
    resized_image.save(output_path)
resize(100, 100, '6103.png', 'resized.png')