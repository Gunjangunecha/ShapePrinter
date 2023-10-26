#Import neccessary libraries
import cv2
import numpy as np

#White Image for the background
image = np.ones((500, 500, 3), dtype=np.uint8) * 255  

#Shapes drawing
cv2.line(image, (50, 50), (450, 50), (0, 20, 25), 5)
cv2.rectangle(image, (50, 100), (450, 200), (0, 75, 7), 3)
cv2.ellipse(image, (150, 350), (100, 50), 0, 0, 360, (58, 0, 81), -1)
cv2.circle(image, (350, 300), 50, (100, 0, 0), -1)

#Display the outcome
cv2.imshow("Geometric Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
