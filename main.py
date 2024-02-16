from camera import Camera
from classe_yolo import Yolo
from app import lancement_app
import cv2

import keyboard
import time

#Instanciation des classes :
video=cv2.VideoCapture(0)
flux_camera=Camera(video, 10)
yolo=Yolo('ultralytics/yolov5')

print("\n####################\nSuite à certain antivirus demandant de confirmer l'utilisation de la caméra, merci d'apuyer sur la fleche directionel gauche après avoir acepter l'utilisation de votre caméra.\n####################")
while True:
    if keyboard.is_pressed("LEFT"):
        print("input")
        lancement_app(flux_camera, yolo)
        while keyboard.is_pressed("RIGHT"):
            time.sleep(0.01)

