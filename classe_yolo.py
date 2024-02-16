import cv2
import torch
from PIL import Image

class Yolo:
    def __init__(self, chemin):
        self.chemin=chemin

    def build():
        # Model
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        return model

    def predict(image_a_predict, model):
        # Images
        for f in 'zidane.jpg', 'bus.jpg':
            torch.hub.download_url_to_file('https://ultralytics.com/images/' + f, f)  # download 2 images
        im1 = Image.open('zidane.jpg')  # PIL image
        im2 = cv2.imread('bus.jpg')[..., ::-1]  # OpenCV image (BGR to RGB)

        # Inference
        results = model([im1, im2], size=640)  # batch of images

        # Results
        results.print()
        results.save()  # or .show()

"""import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Images
imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images

# Inference
results = model(imgs)

# Results
results.print()
results.save()  # or .show()

results.xyxy[0]  # img1 predictions (tensor)
results.pandas().xyxy[0]
"""