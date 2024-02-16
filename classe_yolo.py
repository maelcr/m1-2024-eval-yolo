import cv2
import torch
from PIL import Image

class Yolo:
    def __init__(self, chemin):
        """
        Initialisation des parametres de la classe
        """
        self.chemin=chemin

    def build(self):
        """
        On vient chercher le modele qui sera utiliser pour les prédictions
        """
        model = torch.hub.load(self.chemin, 'yolov5s')
        return model

    def predict(self, image_a_predict, model):
        """
        Input : image_a_predict, pris à partir du flux vidéo
                model, notre modèle yoloV5
        Cette fonction prend la derniere image de la caméra et vient la passer par le modele yoloV5 pour y détécter les objets
        """
        if not (image_a_predict is None):
            print(image_a_predict)
            results = model(image_a_predict)  

            results.print()
            results.save()  #On sauvegarde les résultat (sera utiliser pour l'affichage des détéctions)

            results.xyxy[0]  
            results.pandas().xyxy[0]

            #Alors cette ligne de code vient automatiquement rajouter les annotation sur l'image. Fesant automatiquement le travail de display.
            #Idéalement il faudrait la retirer pour effectuer le traitement dans display.py, mais je n'est pas eu le temps de le faire (merci kaspersky)
            im_rgb = cv2.cvtColor(results.ims[0], cv2.COLOR_BGR2RGB) # Because of OpenCV reading images as BGR
            cv2.imshow("image caméra", im_rgb)
            if cv2.waitKey(1)==27:
                return False

