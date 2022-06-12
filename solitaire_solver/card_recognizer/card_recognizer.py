from calendar import c
from fractions import Fraction
from typing import List
import cv2
from cv2 import imshow
from cv2 import imread
import numpy as np
import os
import sys

# detect the card that is in the frame and returns the card to the user

class card:
    
    save_cards_array = []
    ##structure for card and card type
    def __init__(self):
        self.contour = []
        self.width, self.height = 0, 0
        self.corner_pts = []
        self.center = 0, 0
        self.x, self.y, self.w, self.h = 0, 0, 0, 0
        self.warp = []
        self.suit_img = []
        self.rank_img = []
        self.best_rank_match = []
        self.best_suit_match = []
        self.rank_diff = []
        self.suit_diff = []
        
    
    
    
    def find_hight_Width(self):
        self.x,self.y,self.w,self.h = cv2.boundingRect(self.contour)
    
    def find_center(self):
        self.center = (self.x + self.w / 2, self.y + self.h / 2)
        
        
    
    def sort_points(self):
         cyclic_pts = [
        # Top-left
        self.corner_pts[np.where(np.logical_and(self.corner_pts[:, 0] < self.center[0], self.corner_pts[:, 1] < self.center[1]))[0][0], :],
        # Top-right
        self.corner_pts[np.where(np.logical_and(self.corner_pts[:, 0] > self.center[0], self.corner_pts[:, 1] < self.center[1]))[0][0], :],
        # Bottom-Right
        self.corner_pts[np.where(np.logical_and(self.corner_pts[:, 0] > self.center[0], self.corner_pts[:, 1] > self.center[1]))[0][0], :],
        # Bottom-Left
        self.corner_pts[np.where(np.logical_and(self.corner_pts[:, 0] < self.center[0], self.corner_pts[:, 1] > self.center[1]))[0][0], :]
    ]
         

class card_recognizer:
    
    def  __init__(self) -> None:
        self.saved_cards_array = []
    
    @staticmethod
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

        # return the card contour
        return card_contour


    # SOURCE:
    # https: // stackoverflow.com/questions/64295209/removing-background-around-contour
    @staticmethod
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
    ##stolen from https://github.com/EdjeElectronics/OpenCV-Playing-Card-Detector/blob/1f8365779f88f7f46634114bf2e35427bc1c00d0/Cards.py#L318
    @staticmethod
    def flattener(image, pts, w, h):
        """Flattens an image of a card into a top-down 200x300 perspective.
        Returns the flattened, re-sized, grayed image.
        See www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/"""
        temp_rect = np.zeros((4,2), dtype = "float32")
        
        s = np.sum(pts, axis = 2)

        tl = pts[np.argmin(s)]
        br = pts[np.argmax(s)]

        diff = np.diff(pts, axis = -1)
        tr = pts[np.argmin(diff)]
        bl = pts[np.argmax(diff)]

        # Need to create an array listing points in order of
        # [top left, top right, bottom right, bottom left]
        # before doing the perspective transform

        if w <= 0.8*h: # If card is vertically oriented
            temp_rect[0] = tl
            temp_rect[1] = tr
            temp_rect[2] = br
            temp_rect[3] = bl

        if w >= 1.2*h: # If card is horizontally oriented
            temp_rect[0] = bl
            temp_rect[1] = tl
            temp_rect[2] = tr
            temp_rect[3] = br

        # If the card is 'diamond' oriented, a different algorithm
        # has to be used to identify which point is top left, top right
        # bottom left, and bottom right.
        
        if w > 0.8*h and w < 1.2*h: #If card is diamond oriented
            # If furthest left point is higher than furthest right point,
            # card is tilted to the left.
            if pts[1][0][1] <= pts[3][0][1]:
                # If card is titled to the left, approxPolyDP returns points
                # in this order: top right, top left, bottom left, bottom right
                temp_rect[0] = pts[1][0] # Top left
                temp_rect[1] = pts[0][0] # Top right
                temp_rect[2] = pts[3][0] # Bottom right
                temp_rect[3] = pts[2][0] # Bottom left

            # If furthest left point is lower than furthest right point,
            # card is tilted to the right
            if pts[1][0][1] > pts[3][0][1]:
                # If card is titled to the right, approxPolyDP returns points
                # in this order: top left, bottom left, bottom right, top right
                temp_rect[0] = pts[0][0] # Top left
                temp_rect[1] = pts[3][0] # Top right
                temp_rect[2] = pts[2][0] # Bottom right
                temp_rect[3] = pts[1][0] # Bottom left
                
            
        maxWidth = 200
        maxHeight = 300

        # Create destination array, calculate perspective transform matrix,
        # and warp card image
        dst = np.array([[0,0],[maxWidth-1,0],[maxWidth-1,maxHeight-1],[0, maxHeight-1]], np.float32)
        M = cv2.getPerspectiveTransform(temp_rect,dst)
        warp = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
        warp = cv2.cvtColor(warp,cv2.COLOR_BGR2GRAY)

            

        return warp


    #used to crip all the cards in the frame and return them to the user
    @staticmethod
    def crop_image(_frame, contour):
        tempcard = card()
        
        #creates class for card
        tempcard.contour = contour
        
        #finds conors of card
        peri = cv2.arcLength(tempcard.contour, True)
        approx = cv2.approxPolyDP(tempcard.contour, 0.02 * peri, True)
        points = np.float16(approx)
        tempcard.corner_pts = points
        
        tempcard.find_hight_Width()
        
        #finds center of card
        tempcard.find_center()
        
        tempcard.warp = card_recognizer.flattener(_frame, tempcard.corner_pts, tempcard.w, tempcard.h)
        
        
        CORNER_WIDTH = 32
        CORNER_HEIGHT = 84
        #200x300
        Qcorner1 = tempcard.warp[0:CORNER_HEIGHT, 0:CORNER_WIDTH]
        Qcorner2 = tempcard.warp[0:CORNER_HEIGHT, 200-CORNER_WIDTH:200]
        Qcorner3 = cv2.rotate(tempcard.warp[300-CORNER_HEIGHT:300, 200-CORNER_WIDTH:200],cv2.ROTATE_180)
        Qcorner4 = cv2.rotate(tempcard.warp[300-CORNER_HEIGHT:300,0:CORNER_WIDTH],cv2.ROTATE_180)
        Qcards = [Qcorner1, Qcorner2, Qcorner3, Qcorner4]
        i = 0
        for Qcorner in Qcards:
            
            Qcorner_zoom = cv2.resize(Qcorner, (0,0), fx=4, fy=4)
            
            
            # Adaptive threshold levels
            BKG_THRESH = 60
            CARD_THRESH = 30
            
            white_level = Qcorner_zoom[15,int((CORNER_WIDTH*4)/2)]
            thresh_level = white_level - CARD_THRESH
            if (thresh_level <= 0):
                thresh_level = 1
            retval, query_thresh = cv2.threshold(Qcorner_zoom, thresh_level, 255, cv2. THRESH_BINARY_INV)
            
            # Split in to top and bottom half (top shows rank, bottom shows suit)
            Qrank = query_thresh[20:185, 0:128]
            Qsuit = query_thresh[186:336, 0:128]
            
            # Find rank contour and bounding rectangle, isolate and find largest contour
            Qrank_cnts, hier = cv2.findContours(Qrank, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            Qrank_cnts = sorted(Qrank_cnts, key=cv2.contourArea,reverse=True)

            # Dimensions of rank train images
            RANK_WIDTH = 70
            RANK_HEIGHT = 125
            

            if len(Qrank_cnts) != 0:
                x1,y1,w1,h1 = cv2.boundingRect(Qrank_cnts[0])
                Qrank_roi = Qrank[y1:y1+h1, x1:x1+w1]
                Qrank_sized = cv2.resize(Qrank_roi, (RANK_WIDTH,RANK_HEIGHT), 0, 0)
                tempcard.rank_img.append(Qrank_sized)

            # Find suit contour and bounding rectangle, isolate and find largest contour
            Qsuit_cnts, hier = cv2.findContours(Qsuit, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            Qsuit_cnts = sorted(Qsuit_cnts, key=cv2.contourArea,reverse=True)

            # Dimensions of suit train images
            SUIT_WIDTH = 70
            SUIT_HEIGHT = 100

            #cv2.imshow("Train Rank", tempcard.rank_img)
            #cv2.waitKey(0)

            if len(Qsuit_cnts) != 0:
                x2,y2,w2,h2 = cv2.boundingRect(Qsuit_cnts[0])
                Qsuit_roi = Qsuit[y2:y2+h2, x2:x2+w2]
                Qsuit_sized = cv2.resize(Qsuit_roi, (SUIT_WIDTH, SUIT_HEIGHT), 0, 0)
                tempcard.suit_img.append(Qsuit_sized)
            i += 1

        return tempcard
        

    @staticmethod
    def card_type(frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.blur(gray, (3, 3))
        edge = cv2.Canny(blur, 75, 200)
        contours, _ = cv2.findContours(
            edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # sort the contours by area and get the largest contour which will be the card
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        card2_contour = []
        for c in contours:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # if our approximated contour has four points, then we can assume that we have found our card
            if len(approx) == 4:
                card2_contour.append(approx)
        
        return card2_contour
        


    @staticmethod
    def match_card(qCard, train_ranks, train_suits):
        """Finds best rank and suit matches for the query card. Differences
        the query card rank and suit images with the train rank and suit images.
        The best match is the rank or suit image that has the least difference."""

        best_rank_match_diff = 10000
        best_suit_match_diff = 10000
        best_rank_match_name = "Unknown"
        best_suit_match_name = "Unknown"
        i = 0

        # If no contours were found in query card in preprocess_card function,
        # the img size is zero, so skip the differencing process
        # (card will be left as Unknown)
        if (len(qCard.rank_img) != 0) and (len(qCard.suit_img) != 0):
            
            # Difference the query card rank image from each of the train rank images,
            # and store the result with the least difference
            for rank_img in qCard.rank_img:
                for Trank in train_ranks:
                        #cv2.imshow("Query Rank", rank_img)
                        #cv2.imshow("Train Rank", Trank.img)
                        cv2.waitKey(0)
                        diff_img = cv2.absdiff(rank_img, Trank.img)
                        rank_diff = int(np.sum(diff_img)/255)
                        
                        if rank_diff < best_rank_match_diff:
                            best_rank_diff_img = diff_img
                            best_rank_match_diff = rank_diff
                            best_rank_name = Trank.name

            for suit_img in qCard.suit_img:
            # Same process with suit images
                for Tsuit in train_suits:
                        
                        diff_img = cv2.absdiff(suit_img, Tsuit.img)
                        suit_diff = int(np.sum(diff_img)/255)
                        
                        if suit_diff < best_suit_match_diff:
                            best_suit_diff_img = diff_img
                            best_suit_match_diff = suit_diff
                            best_suit_name = Tsuit.name

        # Combine best rank match and best suit match to get query card's identity.
        # If the best matches have too high of a difference value, card identity
        # is still Unknown
        
        RANK_DIFF_MAX = 2500
        SUIT_DIFF_MAX = 700
        if (best_rank_match_diff < RANK_DIFF_MAX):
            best_rank_match_name = best_rank_name

        if (best_suit_match_diff < SUIT_DIFF_MAX):
            best_suit_match_name = best_suit_name

        # Return the identiy of the card and the quality of the suit and rank match
        return best_rank_match_name, best_suit_match_name, best_rank_match_diff, best_suit_match_diff
        
        
    class Train_suits:
        """Structure to store information about train suit images."""

        def __init__(self):
            self.img = [] # Thresholded, sized suit image loaded from hard drive
            self.name = "Placeholder"
            
    class Train_ranks:
        """Structure to store information about train rank images."""

        def __init__(self):
            self.img = [] # Thresholded, sized rank image loaded from hard drive
            self.name = "Placeholder"

    @staticmethod
    def load_ranks(filepath):
        """Loads rank images from directory specified by filepath. Stores
        them in a list of Train_ranks objects."""

        train_ranks = []
        i = 0
        
        for Rank in ['A','2','3','4','5','6','7',
                    '8','9','10','J','Q','K']:
            train_ranks.append(card_recognizer.Train_ranks())
            train_ranks[i].name = Rank
            filename = Rank + '.jpg'
            train_ranks[i].img = cv2.imread(filepath+filename, cv2.IMREAD_GRAYSCALE)
            i = i + 1

        return train_ranks

    @staticmethod
    def load_suits(filepath):
        """Loads suit images from directory specified by filepath. Stores
        them in a list of Train_suits objects."""

        train_suits = []
        i = 0
        
        for Suit in ['S','D','C','H']:
            train_suits.append(card_recognizer.Train_suits())
            train_suits[i].name = Suit
            filename = Suit + '.jpg'
            train_suits[i].img = cv2.imread(filepath+filename, cv2.IMREAD_GRAYSCALE)
            i = i + 1

        return train_suits

    @staticmethod
    def detect_cards(frame): 
        cards = []   
        for i, contour in enumerate(card_recognizer.detect_card(frame)):
            temp = card_recognizer.crop_image(frame, contour)
            #best_rank_match_name, best_suit_match_name, best_rank_match_diff, best_suit_match_diff
            temp.best_rank_match,temp.best_suit_match,temp.rank_diff,temp.suit_diff= card_recognizer.match_card(temp, card_recognizer.load_ranks("cardDetector/King/"), card_recognizer.load_suits("cardDetector/King/"))
            if temp.best_rank_match != "Unknown" and temp.best_suit_match != "Unknown":
                cards.append(temp)

        return cards

    #make a string one = 1 and two = 2 and so on
    @staticmethod
    def make_string(card):
        card_number = card.best_rank_match
        card_name = card.best_suit_match
        
        return card_number + card_name
        

    

    def recognize_cards(self,frame):
        __frame = imread(frame)
        output =  []
        cards = card_recognizer.detect_cards(__frame)
        if self.saved_cards_array == []:
            firts= False
            i = 0
            for card in reversed(cards):
                self.saved_cards_array.append([])
                for j in range(0,i):
                    self.saved_cards_array[i].append('[]')
                self.saved_cards_array[i].append(card_recognizer.make_string(card))
                i += 1
            output = self.saved_cards_array
        else:
            for card in cards:
                all_cards = []
                card_str = card_recognizer.make_string(card)
                
                for blocks in self.saved_cards_array:
                    for card in blocks:
                        all_cards.append(card)
                        
                if card_str not in all_cards:
                    output.append(card_str)
        return output

