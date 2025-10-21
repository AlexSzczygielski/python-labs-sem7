from PIL import Image

def create_jpg(quantity):
    for i in range(quantity):
        im = Image.new(mode="RGB", size=(200, 200))
        im.save(f"test_pic{i+1}.jpg")

def convert_png(path,number):
    im = Image.open(path)
    png_img = im.convert('RGB')
    png_img.save(f"converted{number+1}.png")



if __name__ == "__main__":
    quantity = 4
    create_jpg(quantity)
    for i in range(quantity):
        convert_png(f"test_pic{i+1}.jpg",i)
    
