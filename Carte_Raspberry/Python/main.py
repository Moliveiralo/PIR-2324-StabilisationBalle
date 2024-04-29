###########################################################
#                                                         #
#                 Stabilisation de balle                  #
#                                                         #
#            Auteurs : OLIVEIRA LOPES Maxime              #
#            NAJI Inès                                    #
#            COUSTON Emma                                 #
#            BIGOT Timothé                                #
#            VORMS Lucie                                  #
#            BEGHIN Léa                                   #
#            Date de création: 27/04/2024                 #
#            Description :                                #
#            - Description brève du projet                #
#                                                         #
###########################################################


# -------------------------------------------------------------- #
##### --------------------- LIBRAIRIES --------------------- #####
# -------------------------------------------------------------- #

import io  # Pour gérer les flux d'octets en mémoire -- Documentation : https://docs.python.org/3/library/io.html
from picamera import PiCamera  # Pour utiliser la caméra Raspberry Pi -- Documentation : https://picamera.readthedocs.io/en/release-1.13/
import time as t  # Pour introduire des délais -- Documentation : https://docs.python.org/fr/3/library/time.html
import PiGPIO as gpio # Librairie pour gérer les GPIO du Raspberry Pi -- Documentation : https://github.com/joan2937/pigpio
# Si jamais on veut, pour implémenter une interface homme-machine via la raspi: https://wiki.python.org/moin/PyQt


# -------------------------------------------------------------- #
##### --------------- ACQUISITION DE L'IMAGE --------------- #####
# -------------------------------------------------------------- #

# Initialisation d'un flux pour stocker la vidéo en mémoire
stream = io.BytesIO()

# Instanciation de l'objet caméra
camera = PiCamera()
camera.resolution = (640, 480)  # Définition de la résolution de la caméra

# Activation de l'aperçu pour visualiser ce que la caméra capte
camera.start_preview()

# Démarrage de l'enregistrement vidéo
camera.start_recording(stream, format='h264', quality=23)  # Format h264 avec une qualité de 23
camera.wait_recording(15)  # Enregistrement pendant 15 secondes
camera.stop_recording()  # Arrêt de l'enregistrement
t.sleep(5)  # Pause de 5 secondes
camera.stop_preview()  # Fermeture de l'aperçu




##Les sliders du code de JohanLink servent à modifier sur une interface les coefs du PID, possibilité de l'implémenter plus tard mais c'est pas la priorité
def PIDcontrol(X_ball, Y_ball, Xball_precedente, Yball_precedente, Xconsigne, Yconsigne):
    # C(s) = Kp * e(s) + Ki/s * e(s) + Kd * s * e(s) --> Kp, Ki et Kd sont les coefficients du PID, que l'on peut ajuster
    Kp = 1
    Ki = 0
    Kd = 0

    S_erreurX += Xconsigne - X_ball # Mise à jour de la somme de l'erreur selon l'axe X
    S_erreurY += Yconsigne - Y_ball # Mise à jour de la somme de l'erreur selon l'axe Y

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
        





