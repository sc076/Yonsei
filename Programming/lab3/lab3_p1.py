import math

#Calculates the size of the images
def calculate_size(depth, compression):
    return (800*600*(depth/8))/compression

#Calculates how many images can be stored
def number_img(usbSize, imgSize):
    return math.floor((usbSize*(10**8))/imgSize)

#Assigns the size for each type of image
gif = calculate_size(8, 5)
jpeg = calculate_size(24, 25)
png = calculate_size(24, 8)
tiff = calculate_size(48, 1)

#Asks the user for the size of the flash memory
usbSize = int(input("Enter USB size (GB): "))

#Outputs the result
print('{:>5}'.format(number_img(usbSize, gif)), 'images in GIF format can be stored')
print('{:>5}'.format(number_img(usbSize, jpeg)), 'images in JPEG  format can be stored')
print('{:>5}'.format(number_img(usbSize, png)), 'images in PNG format can be stored')
print('{:>5}'.format(number_img(usbSize, tiff)), 'images in TIFF format can be stored')

