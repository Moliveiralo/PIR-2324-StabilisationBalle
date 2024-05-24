# PIR 2023-2024 | Stabilisation d'une balle
OLIVEIRA LOPES Maxime - NAJI Inès - COUSTON Emma - BIGOT Timothé - BEGHIN Léa - VORMS Lucie  
This project is based on the project of [Johan Link](https://github.com/JohanLink/Ball-Balancing-PID-System?tab=readme-ov-file)   

![20240202_145909 (1)](https://github.com/Moliveiralo/PIR-2324-StabilisationBalle/assets/133717115/8f52fa8f-02b0-4ea9-83f4-4813ad36bbab)  


## Arduino 
Contains the initial project based off an Arduino Board with Simulink and Matlab.  
Corrections have been made to simulink and matlab compared with the [previous year](https://github.com/TacTac315/PIR_Ball_Balancing).    
Problem with this solution: the system is too slow, the ball cannot be stabilized. Most likely caused by the fact that all the processing is made on the computer and then the instructions are sent to the Arduino to update the servomotors.
The servo-motor delay problem persisted, so we switched to a Raspberry to centralize all the information: the matlab code runs on the raspberry and the camera is connected directly to the raspberry.
Raspberry  

## Raspberry
Transposition of the initial project to a Raspberry pi microcontroller to tackle the issues we experienced on the Arduino board. The raspi's architecture allows all the processing to be made directly on it (image acquisition, analysis, update of the servomotors, ...).
2 versions :  
- Matlab (done remotely via SSH (Ips of the 2 raspis: 
- Python

## Simulations
Simulations to find an optimal PID
 
## Liens suivi de projet
#### Trello
Accessible via le lien suivant: https://trello.com/invite/b/O5i0e5QD/ATTIa336ba5bb40d894ab62b6f74e209b60c67E6674F/pir-stabilisation-de-balle-2023-2024

#### Google Drive
Accessible via le lien suivant: https://drive.google.com/drive/folders/1lspng91aXL2b5Bw1NwQdorwPViMi5FDo?usp=sharing

#### Github de l'an dernier
Accessible via le lien suivant: https://github.com/TacTac315/PIR_Ball_Balancing

#### Guide du PIR
Accessible via le lien suivant: https://docs.google.com/presentation/d/1oQSozAxNd_onhYN5Y_eiVXRHdkCVRMCHHFUxAfs1lPQ/edit?usp=sharing

#### Informations techniques carte raspberrypi
Accessible via le lien suivant : https://www.raspberrypi.com/documentation/computers/raspberry-pi.html
