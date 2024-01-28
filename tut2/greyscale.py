from PIL import Image
def convert_to_grayscale(image_path, output_path):
    image = Image.open(image_path)
    grayscale_img = image.convert('L')
    grayscale_img.save(output_path)
    
convert_to_grayscale('6103.png', 'processed.png')