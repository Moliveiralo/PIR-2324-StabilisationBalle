% This will clear both rpi and cam variables
clear rpi
clear cam

rpi = raspi('10.105.1.112', 'pi', 'raspberry'); %Creation of the raspberry object

%Declration des pins en fonction du servomoteur
servo0=13;
servo1=26;
servo2=19;


%Configuration des PIN en PWM
configurePin(rpi, servo1, 'PWM');
configurePin(rpi, servo2, 'PWM');
configurePin(rpi, servo0, 'PWM');

%Configuration de la fréquence des PWM
writePWMFrequency(rpi, servo1, 200);
writePWMFrequency(rpi, servo2, 200);
writePWMFrequency(rpi, servo0, 200);

%Configuration du duty cycle sur les PWM
writePWMDutyCycle(rpi, servo0, 0.178);
writePWMDutyCycle(rpi, servo1, 0.17);
writePWMDutyCycle(rpi, servo2, 0.165);
