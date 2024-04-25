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



##Les sliders du code de JohanLink servent à modifier sur une interface les coefs du PID, possibilité de l'implémenter plus tard mais c'est pas la priorité
def PIDcontrol(X_ball, Y_ball, Xball_precedente, Yball_precedente, Xconsigne, Yconsigne):
    Kp = 0
    Ki = 0
    Kd = 0

    S_erreurX += Xconsigne - X_ball
    S_erreurY += Yconsigne - Y_ball

    Ix=Kp*(Xconsigne - X_ball) + Ki*S_erreurX + Kd*((Xball_precedente - X_ball)/0.0333)
    Iy=Kp*(Yconsigne - Y_ball) + Ki*S_erreurY + Kd*((Yball_precedente - Y_ball)/0.0333)

    Ix = round(Ix / 10000, 4)
    Iy = round(Iy / 10000, 4)

    gamma = degrees(atan(Iy/Ix))

    if Ix == 0 and Iy == 0:
        alpha_query = 0
        beta_query = 0

    elif Ix > 0 and Iy >= 0:
        beta_query = 180 - abs(gamma)
    elif Ix > 0 and Iy <= 0:
        beta_query = 180 + abs(gamma)
    elif Ix< 0 and Iy >= 0:
        beta_query = abs(gamma)
    elif Ix < 0 and Iy <= 0:
        beta_query = 360 - abs(gamma)
    elif Ix == 0 and Iy > 0:
        beta_query = 90
    else:
        beta_query = 270

    if sqrt(Ix**2 + Iy**2) > 1:
        alpha_query = 35
    else:
        alpha_query = degrees(asin(sqrt(Ix**2 + Iy**2)))


    ## Saturation d'alpha
    if alpha_query > 35:
        alpha_query = 35
        





