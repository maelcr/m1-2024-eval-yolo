

def lancement_app(flux_camera, yolo):
    """
    Input : flux_camera, une instance de classe caméra
            yolo, une instance de classe classe_yolo
    Cette fonction prend en boucle la derniere image du flux vidéo et la fait passer dans le modèle yolo pour prédiction
    """
    
    modele_yolo=yolo.build()
    while True:
        image_cam=flux_camera.read()
        yolo.predict(image_cam, modele_yolo)
            
        

