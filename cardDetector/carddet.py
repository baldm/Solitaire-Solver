from typing import List
import cv2
import cv2
import numpy as np
import os
import sys

# detect the card that is in the frame and returns the card to the user


def detect_card(frame):
    # convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # blur the frame to remove noise
    blur = cv2.blur(gray, (3, 3))
    # apply edge detection to the frame
    edge = cv2.Canny(blur, 75, 200)
    # find the contours in the edge detection result
    contours, _ = cv2.findContours(
        edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # sort the contours by area and get the largest contour which will be the card
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    # initialize the card contour
    card_contour = []
    # loop over the contours
    for c in contours:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points, then we can assume that we have found our card
        if len(approx) == 4 and cv2.contourArea(c) > 100:
            card_contour.append(approx)

    # show image with squares arround cards and wait for user to press a key
    cv2.drawContours(frame, card_contour, -1, (0, 0, 255), 2)
    #cv2.imshow("Card Contour", edge)
    #cv2.imshow("Card", frame)
    # cv2.waitKey(0)

    print("Antal kort fundet: " + str(len(card_contour)))

    # return the card contour
    return card_contour


# SOURCE:
# https: // stackoverflow.com/questions/64295209/removing-background-around-contour
def remove_background(frame, contour):
    hh, ww = frame.shape[:2]

    # draw white contour on black background as mask
    mask = np.zeros((hh, ww), dtype=np.uint8)
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), cv2.FILLED)

    # invert mask so shapes are white on black background
    mask_inv = 255 - mask

    # create new (blue) background
    bckgnd = np.full_like(frame, (0, 255, 0))

    # apply mask to image
    image_masked = cv2.bitwise_and(frame, frame, mask=mask)

    # apply inverse mask to background
    bckgnd_masked = cv2.bitwise_and(bckgnd, bckgnd, mask=mask_inv)

    # add together
    result = cv2.add(image_masked, bckgnd_masked)

    # save results
#    cv2.imwrite('shapes_inverted_mask.jpg', mask_inv)
#    cv2.imwrite('shapes_masked.jpg', image_masked)
#    cv2.imwrite('shapes_bckgrnd_masked.jpg', bckgnd_masked)

    # SOURCE:
    # https://stackoverflow.com/a/28759496

    # Now crop
    (y, x) = np.where(mask == 255)
    (topy, topx) = (np.min(y), np.min(x))
    (bottomy, bottomx) = (np.max(y), np.max(x))
    result = result[topy:bottomy+1, topx:bottomx+1]

    return result


frame = cv2.imread("test/card_i.jpg")

cards: List = []

for i, contour in enumerate(detect_card(frame)):
    tempCard = remove_background(frame, contour)
    cards.append(tempCard)
    cv2.imwrite("cards/card_" + str(i) + ".jpg", tempCard)

print(len(cards))