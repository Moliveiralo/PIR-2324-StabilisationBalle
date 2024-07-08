##################################################################
#                                                                #
#                    Stabilisation de balle                      #
#                                                                #
#               Auteurs :                                        #
#               OLIVEIRA LOPES Maxime                            #
#               NAJI Inès                                        #
#               COUSTON Emma                                     #
#               BIGOT Timothé                                    #
#               VORMS Lucie                                      #
#               BEGHIN Léa                                       #
#                                                                #
#               Date de création: 27/04/2024                     #
#                                                                #
#               Description :                                    #
#               Description brève du projet                      #
#                                                                #
##################################################################

# Pour pouvoir run le code depuis Pycharm sur un ordinateur windows sur le raspberry:
# https://medium.com/@sadeepari/access-raspberry-pi-with-ssh-in-pycharm-848df6d31e8a#:~:text=To%20execute%20code%20on%20your,displayed%20in%20the%20PyCharm%20console.


# -------------------------------------------------------------- #
##### --------------------- LIBRAIRIES --------------------- #####
# -------------------------------------------------------------- #

import io  # Pour gérer les flux d'octets en mémoire -- Documentation : https://docs.python.org/3/library/io.html
import time as t  # Pour introduire des délais -- Documentation : https://docs.python.org/fr/3/library/time.html
import RPi.GPIO as GPIO   # Librairie pour gérer les GPIO du Raspberry Pi -- Documentation : http://sourceforge.net/p/raspberry-gpio-python/wiki/Ho
import cv2 as cv   # Librairie pour l'acquisition d'image avec la caméra --Documentation : https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
# Documentation vidéo OpenCV : https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# Documentation retouche image OpenCV : https://docs.opencv.org/3.4/df/d9d/tutorial_py_colorspaces.html
# Documentation contour OpenCV : https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
import numpy as np  # Librairie pour .....
import math as m


# Si jamais on veut, pour implémenter une interface homme-machine via la raspi: https://wiki.python.org/moin/PyQt


# -------------------------------------------------------------- #
##### ---------- LECTURE DE LA MATRICE DE DONNEES ---------- #####
# -------------------------------------------------------------- #

# Initialisation du dictionnaire de données
data = {}

lines = open("./data.txt").read().splitlines()  # Ouverture du fichier et récupération du tableau des lignes
lines = lines[1:]  # Retrait des en-têtes situés à la première ligne du fichier (alpha,beta,AngleservoA,AngleservoB,AngleservoC)

# On parcourt l'intégralité des lignes du fichier data.txt
for i in range(0, len(lines)):
    # On sépare les valeurs de chaque ligne en une liste
    values = lines[i].strip().split(',')

    # Ajout des données dans le dictionnaire sous le format suivant:
    # data[alpha,beta]=(angleServoA, angleServoB, angleServoC)
    data[float(values[0]),float(values[1])]=(float(values[2]),float(values[3]),float(values[4]))

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

pwm0.ChangeDutyCycle(50)
pwm1.ChangeDutyCycle(50)
pwm2.ChangeDutyCycle(50)

# Démarrage des signaux PWM
pwm0.start(0)
pwm1.start(0)
pwm2.start(0)


# -------------------------------------------------------------- #
##### --------------- ACQUISITION DE L'IMAGE --------------- #####
# -------------------------------------------------------------- #
# Démarrer la prise de vidéo
cap = cv.VideoCapture(0)

# Trouver le centre de la balle
#def DetectOrangeBall():
    #if not cap.isOpened():
        #print("Cannot open camera")
        #exit()

    # Capture frame-by-frame
    #ret, frame = cap.read()

    # if frame is read correctly ret is True
    #if not ret:
        #print("Can't receive frame (stream end?). Exiting ...")
        # break
#else:
        # Recadrer l'image
        # frame = frame[:, 93:550, :]
        # Our operations on the frame come here
        # Convert the frame to HSV color space
        #hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # define range of orange color in HSV
        lower_orange = np.array([5, 40, 50])
        upper_orange = np.array([15, 100, 100])

        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv, lower_orange, upper_orange)
        # Ajoute du flou
        mask = cv.blur(mask, (6, 6))
        # Retire les parasites
        mask = cv.erode(mask, None, iterations=2)
        mask = cv.dilate(mask, None, iterations=2)

        # Trouver le contour de la balle
        contours = cv.findContours(mask.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            # Calcul l'air a partir du contour
            ballArea = cv.contourArea(cnt)
            # Verifier que l'objet trouvé est suffisement grand
            # Pour être sûr que c'est la balle que nous avons detecté
            if ballArea > 1500:
                # We find the circumcircle.
                # It is a circle which completely covers the object with minimum area.
                (x, y), radius = cv.minEnclosingCircle(cnt)
                # (x, y) est le centre du cercle
                ballX = int(x)
                # In images, y=0 is on top, not on the bottom
                ballY = 480 - int(y)
                radius = int(radius)
                # Vérification
                if radius > 20:
                    result = (ballX, ballY)
                    return result

# -------------------------------------------------------------- #
##### ----------- PID + POSITION TO PLATE ANGLE ------------ #####
# -------------------------------------------------------------- #


# Les sliders du code de JohanLink servent à modifier sur une interface les coefs du PID, possibilité de l'implémenter plus tard mais c'est pas la priorité
def PIDcontrol(X_ball, Y_ball, Xball_precedente, Yball_precedente, Xconsigne, Yconsigne):
    global S_erreurX, S_erreurY

    # C(s) = Kp * e(s) + Ki/s * e(s) + Kd * s * e(s) --> Kp, Ki et Kd sont les coefficients du PID, que l'on peut ajuster

    #definition des coefs du PID
    Kp = 1
    Ki = 0
    Kd = 0

    #Somme des erreurs qui ont eu lieu depuis l'allumage du systeme
    S_erreurX += Xconsigne - X_ball  # Mise à jour de la somme de l'erreur selon l'axe X
    S_erreurY += Yconsigne - Y_ball  # Mise à jour de la somme de l'erreur selon l'axe Y

    #Equation des PID
    Ix = Kp * (Xconsigne - X_ball) + Ki * S_erreurX + Kd * ((Xball_precedente - X_ball) / 0.0333)
    Iy = Kp * (Yconsigne - Y_ball) + Ki * S_erreurY + Kd * ((Yball_precedente - Y_ball) / 0.0333)

    #A verifier si c'est utile, Johan Link le fait
    Ix = round(Ix / 10000, 4)
    Iy = round(Iy / 10000, 4)

    gamma = m.degrees(m.atan(Iy / Ix))

    #Détermine le alpha et le beta que l'on souhaire en fonction de Ix et Iy
    if Ix == 0 and Iy == 0:
        alpha_query = 0
        beta_query = 0
    elif Ix > 0 and Iy >= 0:
        beta_query = 180 - abs(gamma)
    elif Ix > 0 and Iy <= 0:
        beta_query = 180 + abs(gamma)
    elif Ix < 0 and Iy >= 0:
        beta_query = abs(gamma)
    elif Ix < 0 and Iy <= 0:
        beta_query = 360 - abs(gamma)
    elif Ix == 0 and Iy > 0:
        beta_query = 90
    else:
        beta_query = 270

    if m.sqrt(Ix ** 2 + Iy ** 2) > 1:
        alpha_query = 35
    else:
        alpha_query = m.degrees(m.asin(m.sqrt(Ix ** 2 + Iy ** 2)))

    ## Saturation d'alpha
    if alpha_query > 35:
        alpha_query = 35

    return alpha_query, beta_query

def main():
    XCenter = 342.0
    YCenter = 304.0
    normX = 1/640
    normY = -1/640
    Xball_precedente = 0
    Yball_precedente = 0

# -------------------------------------------------------------- #
##### ---------------  UPDATING THE ACTUATORS -------------- #####
# -------------------------------------------------------------- #
    while(1) :
        #Detect orange ball
        X, Y = DetectOrangeBall()

#Permet d'actualiser la valeur des servomoteurs en fonction des angles trouvés dans data.txt
def move_motors(AngleServo1, AngleServo2, AngleServo3):
    a = 5.406
    b = -48.65
        # Distance to the center normalise
        X_ball = (X - XCenter)*normX
        Y_ball = (Y - YCenter)*normY

    #Angleservo = a * %PWM - b
    alpha0 = (AngleServo2 - b)/(a*100)
    alpha1 = (AngleServo3 - b)/(a*100)
    alpha2 = (AngleServo1 - b)/(a*100)

        # PID Control et Pos to plate angle
        #PIDcontrol(X_ball, Y_ball, Xball_precedente, Yball_precedente, Xconsigne, Yconsigne):
        a_q, b_q = PIDcontrol(X_ball, Y_ball, Xball_precedente, Yball_precedente, 0, 0)

    #Connfiguration du duty cycle sur les PWM
    pwm1.changeDutyCycle(alpha0)
    pwm2.changeDutyCycle(alpha1)
    pwm3.changeDutyCycle(alpha2)
        Xball_precedente = X_ball
        Yball_precedente = Y_ball
        # Search into the lookup table

        # Updating the actuators












def searchInLookupTable(alpha, beta):
    return data[alpha,beta]