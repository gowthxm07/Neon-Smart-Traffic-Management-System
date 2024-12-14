import cv2
from datetime import datetime
import time

class MDetector():
    
    def change(self, val):
        self.threshold = val
    
    def __init__(self, threshold=10, doRecord=True, sW=True):
        self.writer = None
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.doRecord = doRecord
        self.show = sW
        self.frame = None
        self.count = 0
        self.capture = cv2.VideoCapture(0)
        
        if not self.capture.isOpened():
            print("Error: Unable to access the camera.")
            return
        
        self.frame = self.capture.read()[1]
        self.width = self.frame.shape[1]
        self.height = self.frame.shape[0]
        
        if doRecord:
            self.initRecorder()
        
        self.frame1gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        self.res = None
        self.avg = 0
        self.threshold = threshold
        self.pixels = self.width * self.height
        self.isRecording = False
        self.tt = 0
        
        if sW:
            cv2.namedWindow("Image")
            cv2.createTrackbar("Detection threshold: ", "Image", self.threshold, 100, self.change)
        
    def initRecorder(self):
        codec = cv2.VideoWriter_fourcc(*'XVID')
        self.writer = cv2.VideoWriter(datetime.now().strftime("%b-%d_%H_%M_%S") + ".avi", codec, 20, (self.width, self.height))

    def run(self):
        started = time.time()
        i = 0
        while True:
            ret, curframe = self.capture.read()
            if not ret:
                print("Failed to capture image.")
                break
            
            instant = time.time()
            
            self.processImage(curframe)
            
            if not self.isRecording:
                if self.somethingHasMoved():
                    self.tt = instant
                    if instant > started + 3:
                        i += 1
                        if i == 1:
                            print("The camera has started")
                        self.count += 1
                        if self.tt > started + 10:
                            self.avg = self.count / (instant - started)
                            if (self.avg * 100) > 60:
                                print("This lane is having light traffic")
                                print("The density is light (cars per minute):", (1 / self.avg) * 60)
                            elif (self.avg * 100) > 40 and (self.avg * 100) < 60:
                                print("This lane is having moderate traffic")
                                print("The density is moderate (cars per minute):", (1 / self.avg) * 60)
                            elif (self.avg * 100) < 40:
                                print("This lane is having heavy traffic")
                                print("The density is heavy (cars per minute):", (1 / self.avg) * 60)
                        if self.doRecord:
                            self.isRecording = True
            else:
                if instant >= self.tt + 0.5:
                    self.isRecording = False
                else:
                    cv2.putText(curframe, datetime.now().strftime("%b %d, %H:%M:%S"), (25, 30), self.font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                    self.writer.write(curframe)
            
            if self.show:
                cv2.imshow("Image", curframe)
                cv2.imshow("Res", self.res)
            
            self.frame1gray = cv2.cvtColor(curframe, cv2.COLOR_BGR2GRAY)
            c = cv2.waitKey(1) % 0x100
            if c == 27 or c == 10:
                break

    def processImage(self, frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.res = cv2.absdiff(self.frame1gray, frame_gray)
        self.res = cv2.blur(self.res, (5, 5))
        _, self.res = cv2.threshold(self.res, 10, 255, cv2.THRESH_BINARY_INV)
        self.res = cv2.morphologyEx(self.res, cv2.MORPH_OPEN, None)
        self.res = cv2.morphologyEx(self.res, cv2.MORPH_CLOSE, None)

    def somethingHasMoved(self):
        nb = 0
        min_threshold = (self.pixels / 100) * self.threshold
        nb = self.pixels - cv2.countNonZero(self.res)
        if nb > min_threshold:
            return True
        else:
            return False
        
if __name__ == "__main__":
    detect = MDetector(doRecord=True)
    detect.run()

