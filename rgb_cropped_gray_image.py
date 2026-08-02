import cv2
import matplotlib.pyplot as plt
from google.colab import files
file = files.upload()

image = cv2.imread("example.jpg")

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
plt.title("rgb image")
plt.show()

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grey_image, cmap="gray")
plt.title("grey image")
plt.show()

cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("cropped image")
plt.show()

