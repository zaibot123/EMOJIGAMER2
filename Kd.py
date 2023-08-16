import numpy as np
import cv2
from screeninfo import get_monitors
from mss import mss
from PIL import Image

lower_red = np.array([0, 0, 0], dtype = "uint8") 

upper_red= np.array([255, 255, 255], dtype = "uint8")
height=0
width=0
monitor=""
for m in get_monitors():
    height=m.height
    width=m.width


with mss() as sct:
    while True:
        monitor_number = 1
        monitor = sct.monitors[monitor_number]
        print(monitor)
        
        mon = {'left': 0, 'top': 0, 'width': width, 'height': height, "mon":monitor}
        screenShot = sct.grab(mon)
        img = Image.frombytes(
            'RGB', 
            (screenShot.width, screenShot.height), 
            screenShot.rgb, 
        )

        img=np.array(img)
        mask = cv2.inRange(img, lower_red, upper_red)

        detected_output = cv2.bitwise_and(img, img, mask =  mask) 
 

        cv2.imshow("red color detection", detected_output) 
        print(detected_output)
       
        if cv2.waitKey(33) & 0xFF in (
            ord('q'), 
            27, 
        ):
            break
