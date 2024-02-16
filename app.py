def lancement_app(flux_camera, yolo, modele_yolo):
    while True:
        image_cam=flux_camera.read()
        yolo.predict(image_cam, modele_yolo)