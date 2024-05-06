import RPi.GPIO as GPIO # Librairie pour gérer les GPIO du Raspberry Pi -- Documentation : http://sourceforge.net/p/raspberry-gpio-python/wiki/Ho


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
