from PIL import Image


def convert_image_black_white(path, new_name):
    """The function take the photo and convert you black and white"""
    open_file = Image.open(path)  # i get the path and open the file
    img = open_file.convert("L")  # after i get the file i convert
    img.save(f'{new_name}.jpg')  # save new photo


print(convert_image_black_white('Flowers.png', 'BlackWhite'))
