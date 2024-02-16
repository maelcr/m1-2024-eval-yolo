# Evaluation 16/02

Sans utiliser docker, implémenter le programme python permettant d'afficher et de traiter des résultats d'inférence YoloV5.

Programme à envoyer avant la fin du cours à cvrc.valentin@gmail.com

**Ne pas inclure la version locale de YoloV5 dans le programme envoyé par mail**


### Classe Camera (/5)
- Hérite de `threading.Thread` pour paralléliser la capture d'images
- Prend en argument d'entrée un flux vidéo OpenCV (le reste des arguments d'entrée est libre, par exemple un framerate etc..)
- Une méthode `run` qui lance une boucle infinie permettant de stocker l'image la plus récente du flux vidéo
- Une méthode `read` permettant depuis l'extérieur de la classe de récupérer l'image la plus récente stockée
- **Bonus:** une méthode `clean` appelée automatiquement à la fin du programme et/ou en cas de crash pour nettoyer les flux vidéos et libérer les caméras

### Classe Yolo (/5)
- Prend en argument d'entrée tous les paramétrages nécessaires à l'initialisation du modèle YoloV5 (chemin vers le modèle en local, chemin vers le fichier de poids...)
- Une méthode `build` qui initialise le modèle, en vérifiant si CUDA est disponible ou non, et en stockant le modèle avec `torch.hub.load` sur une version **locale** de Yolov5
- Une méthode `predict` qui prend en entrée une image et qui renvoie la liste des prédictions avec leurs coordonnées (indice: `resultat_inférence.pandas().xyxy` donne les résultats sous un format exploitable facilement avec la position la classe et la confiance de la prédiction, mais c'est facultatif)

### Fichier utilitaire display.py (/2)
- Une fonction `text` paramétrable qui écrit du texte directement sur l'image qu'on lui donne en entrée
- Une fonction `bbox` paramétrable qui dessine un rectangle, directement sur l'image qu'on lui donne en entrée
- Une fonction `annotate_frame` qui prend en entrée une image et une liste de prédictions, et renvoie l'image annotée avec les bounding boxes, le nom de la classe et le pourcentage de précision
- Une fonction `display_frame` qui prend en entrée une image et l'affiche avec OpenCV

### Un fichier app.py (/2)
- Une fonction `app` qui dans une boucle infinie récupère l'image de la caméra, effectue la prediction, annote l'image et l'affiche

### Un fichier main.py (/2)
- Instancie toutes les classes, et lance simplement `app()`

### Pour aller plus loin (/4)
La suite du sujet est libre toute amélioration du programme sera valorisée. En commentaire dans votre fichier main.py, écrivez une courte description de ce que vous avez choisi de faire. Voici quelques idées au cas où vous ne soyez pas inspirés :
- Modifier l'affichage des prédiction en fonction de la classe, de la position ou du degré de confiance de la prédiction
- Modifier app.py pour implémenter une vraie utilisation des résultats d'inférence dans le programme
- Implémenter de la détection de mouvements avec OpenCV
- Permettre le traitement de la caméra ou d'une vidéo (youtube ou mp4 locale)
- Créer un système de configuration (librairie configparser) avec un fichier `.ini` regroupant tous les éléments configurables du projet. Ensuite créer une classe Config qui initialise et stocke tous les champs du fichier `config.ini`
- Créer un système de logger utilisé dans tout le programme (librairie loguru intéressante) sous la forme d'une classe ou d'un fichier logger.py
- ...
