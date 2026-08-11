import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

file = files.upload()

def show_image(title, image):
  plt.figure(figsize=(8, 8))
  if len(image.shape) == 2:
    plt.imshow(image, cmap="gray")
  else:
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  plt.title(title)
  plt.axis("off")
  plt.show()

def interactive_edge_detection(image_path):
  image = cv2.imread(image_path)
  if image is None:
    print("error! no image selected")
  image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  show_image("Original grayscale image", image_gray)

  print("select one option")
  print("1: canny edge detection")
  print("2: sobel edge detection")
  print("3: laplacian edge detection")
  print("4: gausian smoothing edge detection")
  print("5: median smoothing edge detection")
  print("6: exit")

  while True:
     option = int(input("enter your option: "))
     if option == "1":
      canny_detection = cv2.Canny(image_gray, 100, 200)
      show_image("Canny edge detection", canny_detection)
     elif option == "2":
      sobel_x = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=5)
      sobel_y = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=5)
      combined_sobel = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
      show_image("sobel edge detection", combined_sobel)
     elif option == "3":
      Laplation = cv2.Laplacian(image_gray, cv2.CV_64F)
      show_image("laplatoin edge detection", Laplation)
     elif option == "4":
      gaussian_smoothing = cv2.GaussianBlur(image_gray, (5, 5), 0)
      show_image("gaussian edge detection", gaussian_smoothing)
     elif option == "5":
      median_smoothing = cv2.medianBlur(image_gray, 5)
      show_image("median_smoothing", median_smoothing)
     elif option == "6":
      print("ok, bye!")
      break

     else:
      print("invalid choice")

interactive_edge_detection("example.jpg")
