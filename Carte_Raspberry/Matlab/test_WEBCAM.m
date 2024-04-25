% This will clear both rpi and cam variables
clear rpi
clear wcam

rpi = raspi('10.105.1.112', 'pi', 'raspberry'); % Creation of the raspberry object
wcam = webcam(rpi);

for i = 1:10000
    img = snapshot(wcam);
    image(img); % Convert the image into a plottable image
    drawnow; % Plot the image
end
