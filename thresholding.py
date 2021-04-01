
import numpy as np
from PIL import Image
import sys
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#create grayscale image
def greyscale(threshold,B,checkRGB,output):
	
	#run the np array of input photo to give new grayscale value to each pixel
	for y in range(len(B)):
		for x in range(len(B[y])):
			if len(checkRGB)==3: # CheeckRGb=input image shape.If CheckRGB is equal to 3 that means that the input image is colorful
				colorCode=(int(B[y][x][0])+int(B[y][x][1])+int(B[y][x][2]))/3 #store the avergare of blue red and green.
																			  #if R=G=B that means thah the pixel is grayscale
			else:
				colorCode=B[y][x] #store the value of pixel
			if colorCode>=threshold: #if the value of pixel is >= threshold then make it equal to white(255)
				B[y][x]=255
			else:					 #if the value of pixel is < threshold then make it equal to black(0)
				B[y][x]=0

	plt.imshow(B, cmap="gray")
	Image.fromarray(B).save(output)
	plt.show()
	return;

#open and store the input image to np array
B = np.array(Image.open(sys.argv[1]))

#store the shape of image to chech if the image is grayscale(shape=2) or colorul(shape=3)
checkRGB=np.array(B.shape)

output=sys.argv[2]
greyscale((int(sys.argv[3])),B,checkRGB,output)
