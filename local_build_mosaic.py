import sys

try:
    from PIL import Image, ImageFilter
except ImportError:
    print("error:", sys.argv[0], "requires Pillow - install it via 'pip install Pillow'")
    sys.exit(2)

outputImage = Image.new('RGB', [400, 400])
index = 0
for i in range(4):
    for j in range(4):
        inputImage = Image.open("{:04d}_sharp.jpg".format(index+1))
        box = ((i)*100, (j)*100, (i+1)*100, (j+1)*100)
        region = inputImage.crop(box)
        outputImage.paste(region, box)
        index=index+1
            
outputImage.save("mosaic.jpg", 'JPEG')

