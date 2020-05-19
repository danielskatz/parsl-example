from PIL import Image, ImageFilter
import sys

if len(sys.argv) != 2:
    print("error - usage:", sys.argv[0], "basename")
    sys.exit(2)

basename = sys.argv[1]
input_filename = basename + '.jpg'
output_filename = basename + '_sharp.jpg'

#Read image
try:
    im = Image.open(input_filename)
except OSError:
    print("error - can't open file: ", basename, ".jpg", sep="")
    sys.exit(2)


#Applying a filter to the image
im_sharp = im.filter(ImageFilter.SHARPEN)

#Saving the filtered image to a new file
im_sharp.save(output_filename, 'JPEG')
