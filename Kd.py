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
monitor=""
found=False
for m in get_monitors():
    height=m.height
    width=m.width

def search2():
     while True:
        for i in range(width): 
          win32api.SetCursorPos((i,100))
            
colors=[[[225,53,52],[228,52,51], ]]
def search(img,color=[226,53,51]):
    print("Scanning sc")
    rows, cols, _ = img.shape
    for x in range(rows):
        for y in range(cols):
            px = list(img[x, y])
            if px[0] >200 and px[1] in range(48,55) and px[2] in range(48,53) :
                    print("Color found - scanning next picture")
                    win32api.SetCursorPos((y,x))
                    return


with mss() as sct:
    while True:
        if cv2.waitKey(33) & 0xFF in (
            ord('q'), 
            27,
        ):
            break

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
        search(img)


        #cv2.imshow("red color detection", detected_output) 
   



        #print(detected_output)
       
 