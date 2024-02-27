clear rpi
clear cam

rpi = raspi('10.105.1.112', 'pi', 'raspberry')

cam = cameraboard(rpi,'Resolution','1280x720')

for i = 1:10000
    img = snapshot(cam);
    sim('cameraTest',0.00000001);
    image(out.simout);
    drawnow;
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
end