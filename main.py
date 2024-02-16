from camera import VideoCapture
from classe_yolo import Yolo
from app import lancement_app

flux_camera=VideoCapture("camera1")
flux_camera.run()
yolo=Yolo('ultralytics/yolov5')
modele_yolo=yolo.build()

lancement_app(flux_camera, yolo, modele_yolo)

