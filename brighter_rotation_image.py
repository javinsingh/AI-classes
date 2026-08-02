import cv2
import matplotlib.pyplot as plt
import numpy as np
from google.colab import files

file = files.upload()
image = cv2.imread("example.jpg")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(w, h) = image.shape[:2]
center = (w//2, h//2)
m = cv2.getRotationMatrix2D(center, 89, 1.0)
rotated = cv2.warpAffine(image, m, (w, h))

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("rotated image")
plt.show()

brightness_matrix = np.ones(image.shape, dtype="uint8") * 100
brighter = cv2.add(rgb_image, brightness_matrix)

plt.imshow(brighter)
plt.title("brighter image"
)
plt.show()
