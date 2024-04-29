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
#                                                         #
#            Date de création: 27/04/2024                 #
#                                                         #
#            Description :                                #
#            - Description brève du projet                #
#                                                         #
###########################################################


# -------------------------------------------------------------- #
##### --------------------- LIBRAIRIES --------------------- #####
# -------------------------------------------------------------- #

import io  # Pour gérer les flux d'octets en mémoire -- Documentation : https://docs.python.org/3/library/io.html
import picamera as cam  # Pour utiliser la caméra Raspberry Pi -- Documentation : https://picamera.readthedocs.io/en/release-1.13/
import time as t  # Pour introduire des délais -- Documentation : https://docs.python.org/fr/3/library/time.html
import RPi.GPIO as GPIO # Librairie pour gérer les GPIO du Raspberry Pi -- Documentation : http://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
# Si jamais on veut, pour implémenter une interface homme-machine via la raspi: https://wiki.python.org/moin/PyQt


# -------------------------------------------------------------- #
##### ---------- LECTURE DE LA MATRICE DE DONNEES ---------- #####
# -------------------------------------------------------------- #

lines = open("./data.txt").read().splitlines() # Ouverture du fichier et récupération du tableau des lignes
lines = lines[1:] # Retrait des en-têtes situés à la première ligne du fichier (alpha,beta,AngleservoA,AngleservoB,AngleservoC)


# -------------------------------------------------------------- #
##### --------------- CONFIGURATION DES PINS --------------- #####
# -------------------------------------------------------------- #
# Datasheet du Raspberry avec pin layout: https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf
# Note: Le Raspberry Pi 4 Model B ne dispose que de deux PWM hardware. Nous utiliserons la librairie RPi.GPIO
# pour en créer une de manière logicielle

# Assignation des pins pour les servomoteurs et définition de la fréquence des PWM
servo0 = 13
servo1 = 26
servo2 = 19
pwmFrequency = 200

# Configuration des GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(servo0, GPIO.OUT)
GPIO.setup(servo1, GPIO.OUT)
GPIO.setup(servo2, GPIO.OUT)

# Initialisation des objets PWM pour chaque servo --> pour changer le rapport cyclique: pwm.changeDutyCycle(rapportCyclique)
pwm0 = GPIO.PWM(servo0, pwmFrequency)
pwm1 = GPIO.PWM(servo1, pwmFrequency)
pwm2 = GPIO.PWM(servo2, pwmFrequency)

# Démarrage des signaux PWM
pwm0.start(0)
pwm1.start(0)
pwm2.start(0)

# -------------------------------------------------------------- #
##### --------------- ACQUISITION DE L'IMAGE --------------- #####
# -------------------------------------------------------------- #

# Initialisation d'un flux pour stocker la vidéo en mémoire
stream = io.BytesIO()

# Instanciation de l'objet caméra
camera = cam.PiCamera()
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
        





