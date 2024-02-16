import threading
import cv2 as cv


class Camera(threading.Thread):
    def __init__(self, vid, framerate) -> None:
        """
        Initialise les parametres
        """
        super().__init__()

        self.vid = vid
        self.framerate = framerate
        self.last_img = None

        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        """
        Récupere en continu le flux vidéo pour sotcker la derniere image en date
        """
        while True:
            ret, self.last_img = self.vid.read()
            if not ret:
                break

    def read(self):
        """
        Input : rien
        Renturn : La derniere image du flux vidéo
        """
        return self.last_img
    
    def clean(self):
        """
        appeler à la fin du programe, remet la derniere image à None
        """
        self.last_img=None
