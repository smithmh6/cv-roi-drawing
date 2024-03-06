"""
Scripting to test opencv functionality.
"""

import cv2 as cv
import numpy as np

from rectangle import Point, Rectangle

drawing = False
ix, iy = -1,-1
start_point = Point(-1, -1)
end_point = Point(-1, -1)
r = Rectangle(start_point, end_point)

def draw_rectangle(event, x, y, flags, param):
    """
    Rectangular mouse callback function.
    """
    global ix, iy, drawing, start_point, end_point, r


    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        tmp = img.copy()
        cv.imshow('image', tmp)
        ix, iy = x, y

        start_point = Point(ix, iy)
        print(start_point)

    elif event == cv.EVENT_MOUSEMOVE and drawing:
        tmp = img.copy()
        cv.rectangle(tmp, (ix, iy), (x,y), (0, 255, 255), 2)
        cv.imshow('image', tmp)
        #cv.waitKey()

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        tmp = img.copy()
        cv.rectangle(tmp, (ix, iy), (x,y), (0, 255, 0), 2)
        cv.imshow('image', tmp)

        end_point = Point(x, y)
        print(end_point)

        r = Rectangle(start_point, end_point)
        print(r)


# create a black image, window, and bind function to window
#img = np.zeros((512, 512, 3), np.uint8)

# read a tif image into the window
img = cv.imread('images/NE03B_1000ms_0db.tif')
img = cv.resize(img, (1224, 1024))  # resize

#img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)  # convert to grayscale

print(type(img), np.shape(img))


cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.setMouseCallback('image', draw_rectangle)


while 1:
    cv.imshow('image', img)
    if cv.waitKey() & 0xFF == 27:
        break
cv.destroyAllWindows()

if r is not None:
    crop_img = img[
        r.top_left.y:r.bottom_left.y,
        r.top_left.x:r.top_right.x
    ]
    while 1:
        cv.imshow('cropped_image', crop_img)
        if cv.waitKey() & 0xFF == 27:
            break

cv.destroyAllWindows()


