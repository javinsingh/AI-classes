import cv2

image = cv2.imread(r"C:\Users\konin\OneDrive\python\intro into python\Ai classes\app_img.jpg")

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(grey_image, (500, 500))

cv2.imshow("proccessed image: ", resized_image)
key = cv2.waitKey(0)
if key == ord("s"):
    cv2.imwrite("resized_image.jpg", resized_image)
    print("image saved")

else: 
    print("image not saved")

cv2.destroyAllWindows()
print(resized_image.shape)