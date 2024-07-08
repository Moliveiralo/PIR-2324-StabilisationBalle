# PIR 2023-2024 | Stabilisation d'une balle
OLIVEIRA LOPES Maxime - NAJI Inès - COUSTON Emma - BIGOT Timothé - BEGHIN Léa - VORMS Lucie  
This project is based on the project of [Johan Link](https://github.com/JohanLink/Ball-Balancing-PID-System?tab=readme-ov-file)   

![20240202_145909 (1)](https://github.com/Moliveiralo/PIR-2324-StabilisationBalle/assets/133717115/8f52fa8f-02b0-4ea9-83f4-4813ad36bbab)  


## Arduino [ABANDONED - SEE REPORT/POWERPOINT]
Contains the initial project based off an Arduino Board with Simulink and Matlab.  
Corrections have been made to simulink and matlab compared with the [previous year](https://github.com/TacTac315/PIR_Ball_Balancing).    
Problem with this solution: the system is too slow, the ball cannot be stabilized. Most likely caused by the fact that all the processing is made on the computer and then the instructions are sent to the Arduino to update the servomotors.
The servo-motor delay problem persisted, so we switched to a Raspberry to centralize all the information: the matlab code runs on the raspberry and the camera is connected directly to the raspberry.
Raspberry  

## Raspberry [Work In Progress]
Transposition of the initial project to a Raspberry pi microcontroller to tackle the issues we experienced on the Arduino board. The raspi's architecture allows all the processing to be made directly on it (image acquisition, analysis, update of the servomotors, ...).
2 versions :  
- Matlab (done remotely via SSH (Ips of the 2 raspis: 10.105.1.112 and 10.105.1.44)
- Python (We had very little time to work on this part, but we merged all the portions of our code together so that you can take it over. Global structure should be the approximately the same as the matlab script so you can get some inspiration in the matlab script).

## Simulations
Simulations to find an optimal PID
 
#### Github from last year
Available here : https://github.com/TacTac315/PIR_Ball_Balancing

#### Raspberry documentation
Available here : https://www.raspberrypi.com/documentation/computers/raspberry-pi.html
