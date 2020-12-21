from PIL import Image

mac = Image.open('example.jpg')

mac
mac.size

## CROPPING IMAGES  ##
mac.crop((0,0,100,100))

pencils = Image.open('pencils.jpg')

pencils.size
pencils.crop((0,1100,800,1300))

computer = mac.crop((1993/2-200, 800, 1993/2+200, 1257))

red = Image.open("red_color.jpg")
blue = Image.open("blue_color.png")
red
blue
red.putalpha(255)
blue.putalpha(255)
blue.show()
blue.paste(im=red,box=(0,0), mask=red)

###     IMAGE EXERCISE      ###

word_matrix = Image.open("word_matrix.png")
mask = Image.open("mask.png")
word_matrix.size
mask.size
mask = mask.resize(word_matrix.size) #resize the mask to the same size as the word matrix
mask.size
mask.putalpha(128)# makes the mask transparent so that you can see the words that are in the gaps
word_matrix.paste(mask,box=(0,0), mask=mask) # past the mask on top of the word matrix so that it shows the hidden message
word_matrix
