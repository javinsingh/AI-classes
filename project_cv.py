
import cv2
import matplotlib.pyplot as plt
import numpy as np
from google.colab import files

file = files.upload()

image = cv2.imread("example.jpg")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
plt.title("rgb image")
plt.show()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap="gray")
plt.title("gray image")
plt.show()

cropped_image = image[300:600, 200:400]
rgb_cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_cropped_image)
plt.title("cropped image")
plt.show()

(w, h) = image.shape[:2]
center = (w//2, h//2)
m = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, m, (w, h))
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("rotated image")
plt.show()

brightness_matrix = np.ones(image.shape, dtype="uint8") * 100
brighter = cv2.add(rgb_image, brightness_matrix)

plt.imshow(brighter)
plt.title("brighter image")
plt.show()

dim_matrix = np.ones(image.shape, dtype="uint8") * 100
dimmer = cv2.subtract(rgb_image, dim_matrix)

plt.imshow(dimmer)
plt.title("dimmer image")
plt.show()
