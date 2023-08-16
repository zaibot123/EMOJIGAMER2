import numpy as np
import cv2
from screeninfo import get_monitors
from mss import mss
from PIL import Image
import win32api, win32con

lower_red = np.array([0, 0, 0], dtype = "uint8") 

upper_red= np.array([255, 255, 255], dtype = "uint8")
height=0
width=0


with mss() as sct:
    while True:
        monitor_number = 1
        monitor = sct.monitors[monitor_number]
        print(monitor)
        
        mon = {'left': 0, 'top': 0, 'width': width, 'height': height}
        screenShot = sct.grab(mon)
        img = Image.frombytes(
            'RGB', 
            (screenShot.width, screenShot.height), 
            screenShot.rgb, 
        )

        rows, cols, _ = img.shape
        for x in range(rows):
            
            for y in range(cols):
                px = list(img[x, y])
                if px == [0, 255, 0]:
                    print("GRØN")
                    win32api.SetCursorPos((y,x))



        #print(detected_output)
       
        if cv2.waitKey(33) & 0xFF in (
            ord('q'), 
            27, 
        ):
            break
