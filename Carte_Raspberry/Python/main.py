#Import pour la camera Raspberry
from io import BytesIO
from picamera import PiCamera
from time import sleep

#Objet permettant de stocker la video en mémoire
stream = BytesIO()

#Déclaration de la caméra
camera = PiCamera()
camera.resolution = (640, 480)

#Voir ce que la camera voit
camera.start_preview()
#Enregistrement
camera.start_recording(stream, format='h264', quality=23)
camera.wait_recording(15)
camera.stop_recording()
sleep(5)
camera.stop_preview()


