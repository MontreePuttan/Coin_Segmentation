import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv

from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

image = cv2.imread("image/car_1.jpg")
plt.imshow(image)

box,label,count = cv.detect_common_objects(image)
output = draw_bbox(image,box,label,count)
plt.imshow(output)

#print("label : " , label)
removeLabel = list(set(label))
 
# printing list after removal
print ("The list after removing duplicates label : " + str(removeLabel))

print("car : " , label.count('car'))
print("person : " , label.count('person'))

plt.show()

if cv2.waitKey(1) & 0xFF==ord('q'):
    cv2.destroyAllWindows()
