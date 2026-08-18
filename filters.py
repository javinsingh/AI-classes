import cv2
import numpy as np

def apply_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 1] = 0
    elif filter_type == "green":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "blue":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "red tint":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "blue decrease":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    return filtered_image

image_path = r"C:\Users\konin\OneDrive\python\intro into python\Ai classes\example.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: image not found!")
else:
    filter_type = "original"
    print("Hello! Apply a filter to this image.")
    print("press 1 for red")
    print("press 2 for green")
    print("press 3 for blue")
    print("press 4 for a red tint")
    print("press 5 to decrease blue intencity")
    print("press 6 to quit")

    while True:
        filtered_image = apply_filter(image, filter_type)
        cv2.imshow("Filtered image: ", filtered_image)
        key = cv2.waitKey(0) & 0xFF

        if key == ord("1"):
            filter_type = "red"
        elif key == ord("2"):
            filter_type = "green"
        elif key == ord("3"):
            filter_type = "blue"
        elif key == ord("4"):
            filter_type = "red tint"
        elif key == ord("5"):
            filter_type = "blue decrease"
        elif key == ord("6"):
            print("Quitting...")
            break
        else:
            print("invalid key! press 1, 2, 3, 4, 5 or 6")

cv2.destroyAllWindows()

