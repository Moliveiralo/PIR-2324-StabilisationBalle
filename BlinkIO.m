clear

A = []

blinkGPIOLEDAndPlotOutput()

A

function blinkLED()
% Create a Raspberry Pi object
r= raspi('10.105.1.112', 'pi', 'raspberry');

% Blink the LED for 100 cycles
for count = 1:100
    % Turn on the LED
    writeLED(r,"LED0", 1);
    % Pause for 0.5 seconds
    pause(0.5);
    % Turn off the LED
    writeLED(r,"LED0", 0);
    % Pause for 0.5 seconds
    pause(0.5);
end
end

function blinkGPIOLED()

r= raspi('10.105.1.112', 'pi', 'raspberry');

configurePin(r,17,'DigitalOutput');

for count = 1:100
    % Turn on the LED
    writeDigitalPin(r,17,1);
    % Pause for 0.5 seconds
    pause(0.5);
    % Turn off the LED
    writeDigitalPin(r,17,0);
    % Pause for 0.5 seconds
    pause(0.5);
end
end

function blinkLEDPWM()

r= raspi('10.105.1.112', 'pi', 'raspberry');

configurePin(r,17,'PWM');

writePWMFrequency(r, 17, 10);
writePWMDutyCycle(r, 17, 0.9);

pause(5);

writePWMDutyCycle(r, 17, 0.3);

pause(5);
end

function runServoPWM()

r= raspi('10.105.1.112', 'pi', 'raspberry');

configurePin(r, 26, 'PWM');
configurePin(r, 19, 'PWM');
configurePin(r, 13, 'PWM');

writePWMFrequency(r, 26, 200);
writePWMFrequency(r, 19, 200);
writePWMFrequency(r, 13, 200);

writePWMDutyCycle(r, 26, 0.17);
writePWMDutyCycle(r, 19, 0.17);
writePWMDutyCycle(r, 13, 0.17);

pause(10);
end