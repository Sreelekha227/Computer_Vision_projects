# Importing Libraries
import numpy as np
import cv2
import imutils


# Read the Image
Original_image = cv2.imread(r"Computer_Vision_projects\CV Basics\CV Basic Program Images\Dog.jpeg")
print(Original_image)

# Write Image
cv2.imwrite("Org Image copy 1.jpg",Original_image)

# Show Image
cv2.imshow("Original Image",Original_image)


# Image properties
print("\n Shape is :" , Original_image.shape)
print("\n Size is :" ,Original_image.size)


# Convert Original Image to Grey Image
Grey_Image = cv2.cvtColor(Original_image, cv2.COLOR_BGR2GRAY)
print(Grey_Image)

# write Greyscale Image
cv2.imwrite("GreyImage.jpg",Grey_Image)

# Show Greyscale Image
cv2.imshow("Grey scale Image",Grey_Image)


# Resize  -> Original Image
Resized_image1 = imutils.resize(Original_image, width = 1000)
print(Resized_image1)

# save resized image
cv2.imwrite("Resized Original Image.jpg",Resized_image1)

# Show resized image
cv2.imshow("Resized Original Image",Resized_image1)


# Resize  -> Grey Image
Resized_image2 = imutils.resize(Grey_Image, width = 500)
print(Resized_image2)

# save resized image
cv2.imwrite("Resized Grey Image.jpg",Resized_image2)

# Show resized image
cv2.imshow("Resized Grey Image",Resized_image2)


# Gaussian Blur - Smoothening  -> Original Image
Gaussian_Img1 = cv2.GaussianBlur(Original_image, (21,21), 0)
print(Gaussian_Img1)

# save Gaussian Blur image
cv2.imwrite("Gaussian Image-Original.jpg",Gaussian_Img1)

# Show Gaussian Blur image
cv2.imshow("Gaussian Image-Original",Gaussian_Img1)


# Gaussian Blur - Smoothening  -> Grey Image
Gaussian_Img2 = cv2.GaussianBlur(Grey_Image, (21,21), 0)
print(Gaussian_Img2)

# save Gaussian Blur image
cv2.imwrite("Gaussian Image-Grey.jpg",Gaussian_Img2)

# Show Gaussian Blur image
cv2.imshow("Gaussian Image-Grey",Gaussian_Img2)

# Threshold Image
#Grey -> Black & White
threshold_img = cv2.threshold(Grey_Image, 150, 255, cv2.THRESH_BINARY)[1]
print(threshold_img)

cv2.imwrite("Threshold Image.jpg",threshold_img)

cv2.imshow("Threshold Image",threshold_img)


cv2.waitKey(0)
cv2.destroyAllWindows()