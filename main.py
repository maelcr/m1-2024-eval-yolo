from camera import VideoCapture
from classe_yolo import Yolo
from app import lancement_app

flux_camera=VideoCapture(0)
yolo=Yolo('ultralytics/yolov5')

lancement_app(flux_camera, yolo)

