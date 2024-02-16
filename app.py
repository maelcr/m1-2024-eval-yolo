def lancement_app(flux_camera, yolo):
    flux_camera.run()
    modele_yolo=yolo.build()
    while True:
        image_cam=flux_camera.read()
        yolo.predict(image_cam, modele_yolo)