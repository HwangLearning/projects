import cv2
from djitellopy import tello
from time import time
import KeyModule as kp

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamon()

def KeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0

    speed = 50
    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed

    if kp.getKey("q"): me.land()
    time.sleep(3)
    if kp.getKey("e"):  me.takeoff()

    if kp.getKey('z'):
        tm = time.localtime(time.time())
        cv2.imwrite(f'Resources/Images/{tm.tm_mon}_{tm.tm_mday}_{tm.tm_hour}_{tm.tm_min}_{tm.tm_sec}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]


while True :
    vals = KeyboardInput()
    img = me.get_frame_read().frame
    img = cv2.resize(img, (1024,768))
    cv2.imshow('Image',img)
    cv2.waitKey(1)
