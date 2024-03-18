clear rpi
clear cam

rpi = raspi('10.105.1.112', 'pi', 'raspberry');

cam = cameraboard(rpi,'Resolution','1280x720');

img = snapshot(cam);
image(img);
drawnow;

%% ================================================================
%                        DATA LOOKUP TABLE : load before everything else
%  ================================================================
% Documentation: https://www.mathworks.com/help/ecoder/ug/lookup-table-function-code-replacement-sc.html
%The function of this program is to : 
% - Load the AnglePlateau->AngleServos correspondence file generated
% using Johan Link's Python program
% - Convert the data into a Lookup Table to make them usable
% by Simulink
load('data.mat');
xrange = min(data.alpha):0.2:max(data.alpha);
yrange = min(data.beta):0.2:max(data.beta);

[Alpha,Beta]=meshgrid(xrange,yrange);

AValues=griddata(data.alpha,data.beta,data.AngleservoA,Alpha,Beta);
BValues=griddata(data.alpha,data.beta,data.AngleservoB,Alpha,Beta);
CValues=griddata(data.alpha,data.beta,data.AngleservoC,Alpha,Beta);


%% ================================================================
%                               DATA
%  ================================================================
%Set the coordonates of the center of the plate 
Xcenter = 0; 
Ycenter = 0; 

%Where we want the ball to be at the end (in the center to be stable)
Xconsigne = 0;
Yconsigne = 0;

%Gain to normalise the position of the ball
NormX=1/640;
NormY=-1/640;

%Gain......
AreaCoeff=1/400;


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
%                    THE DISTANCE TO THE CENTER (NORMALISE)
%  ================================================================
X_ball = ballX*normX- XCenter; 
Y_ball = ballY*normY - YCenter;


%% ================================================================
%                           CONCATENATE
%  ================================================================
% Block divide (Bound between detect orange ball and input Area of block Concatenate )
Area(1) = ballArea*AreaCoeff; 
%Block Concatenate
Shape = [int32(X(1)), int32(Y(1)), int32(Area(1))]; 



%% ================================================================
%                              PIDs
%  ================================================================
epsilonX = Xconsigne - X_ball;
epsilonY = Yconsigne - Y_ball;

%Parameters of the PID for x and y axes 
%To determinate
Kp_x=0;
Ti_x=0;
Td_x=0;

Kp_y=0;
Ti_y=0;
Td_y=0;

%Transfert fonction of the PID
PID_x = Kp_x*tf([Td_x*Ti_x Ti_x 1], [Ti_x 0]);
PID_y = Kp_y*tf([Td_y*Ti_y Ti_y 1], [Ti_y 0]);

%% ================================================================
%                    POSITION TO PLATE ANGLE
%  ================================================================
%Bound between PID and PosToPlateAngle
x= PID_x;
y=PID_y;

toDeg=180/pi;

gamma = atan(y/x)*toDeg;

if (x>0 && y>=0)
    beta_query=180-abs(gamma);
 elseif (x>0 && y<=0)
     beta_query=180+abs(gamma);
 elseif(x<0 && y>=0)
    beta_query=abs(gamma);
elseif(x<0 && y<=0)
    beta_query=360-abs(gamma);
elseif(x==0 && y>= 0)
    beta_query=90;
else
    beta_query=270;
end

if (sqrt(x^2+y^2)>1)
    alpha_query = 35; 
else
    alpha_query=asin(sqrt(x^2+y^2))*toDeg;
end


%Saturation of alpha
if (alpha_query >35)
    alpha_query=35;
end
%% ================================================================
%                      SEARCH INTO THE LOOKUP TABLE
%  ================================================================
%Test fonctionnel après vérification sur le lookup table editor pour les 3
%servo
%alpha_query=1.8; 
%beta_query=4.6;

% Avalues , Bvalues and Cvalues are matrices of angles for the servo motors
% depending on Alpha (abscissa) and Beta (ordonates)
% interp2 search into these matrices for the indexes alpha and beta
AngleServo1=interp2(Alpha,Beta,AValues,alpha_query,beta_query);
AngleServo2=interp2(Alpha,Beta,BValues,alpha_query,beta_query);
AngleServo3=interp2(Alpha,Beta,CValues,alpha_query,beta_query);

%% ================================================================
%                      UPDATING THE ACTUATORS
%  ================================================================
%Vector concatenate
Vector_ABC=[AValues, BValues, CValues];

%Zero Order Hold


