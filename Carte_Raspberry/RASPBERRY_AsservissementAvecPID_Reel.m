clear rpi
clear cam

rpi = raspi('10.105.1.112', 'pi', 'raspberry');

cam = cameraboard(rpi,'Resolution','1280x720');

img = snapshot(cam);
image(img);
drawnow;


%% ================================================================
%                               DATA
%  ================================================================
Xcenter = 0;
Xconsigne = 0;
Ycenter = 0;
Yconsigne = 0;
Kx=1/640;
Ky=-1/640;
AreaCoeff=400;


%% ================================================================
%                       DETECT ORANGE BALL
%  ================================================================

% Create the default minimum and maximum HSV values for orange color
orangeMin =  [0.05 0.4 0.5];
orangeMax =  [0.15 1.0 1.0];
ballArea = int32(0); % Fixed size for Simulink
DefaultX= int32(297.4);
DefaultY= int32(198.5);
% Create a blob analysis object
blobAnalyzer = vision.BlobAnalysis('MinimumBlobArea', 100, 'MaximumBlobArea', 10000);
ballX = int32(zeros(1));
ballY = int32(zeros(1));
while true
    % Check if the input frame is empty
    if isempty(frame)
        ballX = DefaultX;
        ballY = DefaultY;
        ballArea = int32(0);
        break;
    end
    
    % Convert the frame to HSV color space
    hsv = rgb2hsv(frame);
    
    % Create a mask for the orange color
    mask = (hsv(:,:,1) >= orangeMin(1)) & (hsv(:,:,1) <= orangeMax(1)) & ...
           (hsv(:,:,2) >= orangeMin(2)) & (hsv(:,:,2) <= orangeMax(2)) & ...
           (hsv(:,:,3) >= orangeMin(3)) & (hsv(:,:,3) <= orangeMax(3));
       
    % Perform blob analysis on the mask
    [areas, centroids] = step(blobAnalyzer, mask);
    
    % Find the largest blob in the image
    index = [];
    if ~isempty(areas)
        [~, index] = max(areas);
        tempX= int32(centroids(index, 1));
        ballX = tempX(1);
        tempY = int32(centroids(index, 2));
        ballY = tempY(1);
        ballArea = areas(index);
    else
        ballX = DefaultX;
        ballY = DefaultY;
        ballArea = int32(0);
        break; % No ball has been found
    end
    
    % Output the centroid and area of the largest blob
    if ~isempty(centroids)
        tempX = int32(centroids(index, 1));
        ballX = tempX(1);
        tempY = int32(centroids(index, 2));
        ballY = tempY(1);
        ballArea = areas(index);
        break;
    end
end



%% ================================================================
%                           CONCATENATE
%  ================================================================

Shape=[int32(X(1)), int32(Y(1)), int32(Area(1))];



%% ================================================================
%                              PIDs
%  ================================================================
Px=0;
Ix=0;
Dx=0;

Py=0;
Iy=0;
Dy=0;


%% ================================================================
%                    POSITION TO PLATE ANGLE
%  ================================================================

toDeg=180/pi;
%%alpha=asin(sqrt(x^2+y^2))*toDeg;

%alpha = asin(x)*toDeg;;
% gamma = atan(y)*toDeg;

gamma = atan(y/x)*toDeg;

if (x>0 && y>=0)
    beta=180-abs(gamma);
 elseif (x>0 && y<=0)
     beta=180+abs(gamma);
 elseif(x<0 && y>=0)
    beta=abs(gamma);
elseif(x<0 && y<=0)
    beta=360-abs(gamma);
elseif(x==0 && y>= 0)
    beta=90;
else
    beta=270;
end

%beta = asin(y)*toDeg;;    

if (sqrt(x^2+y^2)>1)
    alpha = 35; 
else
    alpha=asin(sqrt(x^2+y^2))*toDeg;
end


%% ================================================================
%                        DATA LOOKUP TABLE
%  ================================================================
% Documentation: https://www.mathworks.com/help/ecoder/ug/lookup-table-function-code-replacement-sc.html



%% ================================================================
%                      UPDATING THE ACTUATORS
%  ================================================================