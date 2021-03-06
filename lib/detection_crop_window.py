import os
import cv2
import glob
import pickle

'''
This script is to get windows in the images after clustring the ships
'''

# <=====================================================================================>
# utils
def click_and_crop(event, x, y, flags, param):
    global refPt, cropping
    if event == cv2.EVENT_LBUTTONDOWN:    # indicates that the left mouse button is pressed
        refPt = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_RBUTTONDOWN:   # indicates that the right mouse button is pressed
        refPt.append((x, y))
        cropping = False
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


# <=====================================================================================>
# Here is the process to crop the window and get the position of the graph
# after the classification of the fish boat

label = range(-1,27)  # we have 27 cluster of ships
sample_path = [glob.glob('/Users/pengfeiwang/Desktop/c1/%s/*.jpg' %i)[0] for i in label]

location = dict()
for j,i in enumerate(sample_path):
    image = cv2.imread(i)
    clone = image.copy()
    cv2.namedWindow("image")
    refPt = [];
    cropping = False
    cv2.setMouseCallback("image", click_and_crop)
    while True:
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("r"):
            image = clone.copy()
        elif key == ord("c"):
            break
    if len(refPt) == 2:
        print j+"  ===>  " + refPt[0][1], refPt[1][1], refPt[0][0], refPt[1][0]
        location['c'+str(j)] = [(refPt[0][1], refPt[1][1]),(refPt[0][0], refPt[1][0])]
    cv2.destroyAllWindows()

# location
pickle.dump(location,open('/Users/pengfeiwang/Desktop/location.pkl', 'wb'))




