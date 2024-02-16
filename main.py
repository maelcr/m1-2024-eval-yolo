from camera import VideoCapture
from classe_yolo import Yolo
from app import lancement_app

flux_camera=VideoCapture("camera1")
flux_camera.run()
modele_yolo=Yolo('ultralytics/yolov5')

lancement_app(flux_camera, modele_yolo)

