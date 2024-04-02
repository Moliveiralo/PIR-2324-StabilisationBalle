% This will clear both rpi and cam variables
clear rpi
clear cam

rpi = raspi('10.105.1.112', 'pi', 'raspberry'); % Creation of the raspberry object

cam = cameraboard(rpi,'Resolution','640x480'); % Creation of the camera object

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
XCenter = 0; 
YCenter = 0; 

%Where we want the ball to be at the end (in the center to be stable)
Xconsigne = 0;
Yconsigne = 0;

%Gain to normalise the position of the ball
normX=1/640;
normY=-1/640;

%Gain......
AreaCoeff=1/400;


% The program will loop indefinitely
while 1
    %% ================================================================
    %                           IMAGE ACQUISITION
    %  ================================================================
    
    img = snapshot(cam); % An image is taken from the camera object
    image(img); % Convert the image into a plottable image
    drawnow; % Plot the image
    
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
    
    
    % Check if the input frame is empty
    if isempty(img)
        ballX = DefaultX;
        ballY = DefaultY;
        ballArea = int32(0);
    end
    
    % Convert the frame to HSV color space
    hsv = rgb2hsv(img);
    
    print = "hsv ça a marché"
    
    % Create a mask for the orange color
    mask = (hsv(:,:,1) >= orangeMin(1)) & (hsv(:,:,1) <= orangeMax(1)) & ...
        (hsv(:,:,2) >= orangeMin(2)) & (hsv(:,:,2) <= orangeMax(2)) & ...
        (hsv(:,:,3) >= orangeMin(3)) & (hsv(:,:,3) <= orangeMax(3));
    
    print = "avant"
    % Perform blob analysis on the mask
    [areas, centroids] = step(blobAnalyzer, mask);
    print = "après"
    
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
    end
    
    print = "après après"
    
    % Output the centroid and area of the largest blob
    if ~isempty(centroids)
        tempX = int32(centroids(index, 1));
        ballX = tempX(1);
        tempY = int32(centroids(index, 2));
        ballY = tempY(1);
        ballArea = areas(index);
    end
    
    print = "après après après"

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
    Shape = [int32(X_ball(1)), int32(Y_ball(1)), int32(Area(1))]; 
    
    
    
    
    
    
    
    
    
    
    
    
    % ICI IL MANQUE LA PARTIE OU ON GENERE LA FORME DU CERCLE
    % ET OU ON L'AFFICHE SUR UN PLOT AVEC L'IMAGE INITIALE
    
    
    
    
    
    
    
    
    
    
    
    print = "après après après après"


    %% ================================================================
    %                              PIDs
    %  ================================================================
    epsilonX = Xconsigne - X_ball;
    epsilonY = Yconsigne - Y_ball;

    
    %Parameters of the PID for x and y axes 
    %To determinate
    Kp_x=1;
    Ti_x=1;
    Td_x=1;

    Kp_y=1;
    Ti_y=1;
    Td_y=1;

    %Transfert fonction of the PID
    PID_x = Kp_x*tf([Td_x*Ti_x Ti_x 1], [Ti_x 0]);
    PID_y = Kp_y*tf([Td_y*Ti_y Ti_y 1], [Ti_y 0]);
    
    print = "après après après après après"


    %% ================================================================
    %                    POSITION TO PLATE ANGLE
    %  ================================================================
    
    %Bound between PID and PosToPlateAngle
%     x=PID_x;
%     y=PID_y;

    x = PID_x*epsilonX;
    y = PID_y*epsilonY;

    
    
    
    
    
    
    
    
    %%%%%% LE CODE IL BLOQUE A CE NIVEAU LA
    
    % EN REALITE SI ON REGARDE LE SIMULINK X ET Y C'EST LA COMMANDE EN
    % SORTIE DES PID ET NON PAS LA FONCTION DE TRANSFERT 
    % DU COUP CA BLOQUE AU NIVEAU DE L'ARCTAN VU QU'IL PEUT PAS PROCESS DES
    % FONCTIONS DE TRANSFERT
    
    
    
    
    
    
    
    
    
    
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

    print = "après après après après après après"
    
    %Saturation of alpha
    if (alpha_query >35)
        alpha_query=35;
    end

    %% ================================================================
    %                      SEARCH INTO THE LOOKUP TABLE
    %  ================================================================

    % Avalues , Bvalues and Cvalues are matrices of angles for the servo motors
    % depending on Alpha (abscissa) and Beta (ordonates)
    % interp2 search into these matrices for the indexes alpha and beta
    AngleServo1=interp2(Alpha,Beta,AValues,alpha_query,beta_query);
    AngleServo2=interp2(Alpha,Beta,BValues,alpha_query,beta_query);
    AngleServo3=interp2(Alpha,Beta,CValues,alpha_query,beta_query);

    print = "après après après après après après après"

    %% ================================================================
    %                      UPDATING THE ACTUATORS
    %  ================================================================

    % PIN LAYOUT ON THE RASPBERRY
    % GPIO 13 --> SERVO 0
    % GPIO 26 --> SERVO 1
    % GPIO 19 --> SERVO 2

    %Declration des pins en fonction du servomoteur
    servo0=13;
    servo1=26;
    servo2=19;


    %Configuration des PIN en PWM
    configurePin(r, servo1, 'PWM')
    configurePin(r, servo2, 'PWM')
    configurePin(r, servo0, 'PWM')

    print = "bientot a la fin"
    
    %Configuration de la fréquence des PWM
    writePWMFrequency(r, servo1, 200)
    writePWMFrequency(r, servo2, 200)
    writePWMFrequency(r, servo0, 200)

    %Fonction pour trouver la valeur du duty cycle
        %Fonction affine : ax+b = y
    a = 5.406;
    b = -48.65;
    alpha0 = (AngleServo1-b)/a;
    alpha1 = (AngleServo2-b)/a;
    alpha2 = (AngleServo3-b)/a;
    
    print = "c'est bientot fini"

    %Configuration du duty cycle sur les PWM
    writePWMDutyCycle(r, servo0, alpha0)
    writePWMDutyCycle(r, servo1, alpha1)
    writePWMDutyCycle(r, servo2, alpha2)
    
    print = "c'est fini"
end





