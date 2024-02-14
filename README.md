# PIR 2023-2024 | Stabilisation d'une balle
OLIVEIRA LOPES Maxime - NAJI Inès - COUSTON Emma - BIGOT Timothé - BEGHIN Léa - VORMS Lucie

![20240202_145909 (1)](https://github.com/Moliveiralo/PIR-2324-StabilisationBalle/assets/133717115/8f52fa8f-02b0-4ea9-83f4-4813ad36bbab)

## Trello
Accessible via le lien suivant: https://trello.com/invite/b/O5i0e5QD/ATTIa336ba5bb40d894ab62b6f74e209b60c67E6674F/pir-stabilisation-de-balle-2023-2024

## Google Drive
Accessible via le lien suivant: https://drive.google.com/drive/folders/1lspng91aXL2b5Bw1NwQdorwPViMi5FDo?usp=sharing

## Github de l'an dernier
Accessible via le lien suivant: https://github.com/TacTac315/PIR_Ball_Balancing

## Guide du PIR
Accessible via le lien suivant: https://docs.google.com/presentation/d/1oQSozAxNd_onhYN5Y_eiVXRHdkCVRMCHHFUxAfs1lPQ/edit?usp=sharing

## Informations techniques carte raspberrypi
Accessible via le lien suivant : https://www.raspberrypi.com/documentation/computers/raspberry-pi.html

## Erreur matlab
warning :
Error evaluating 'PostLoadFcn' callback of block_diagram 'instrumentlib'. 
Callback string is 'instrumentslgate('privateinstrumentslinitlib')'
Caused by:
License checkout failed.
License Manager Error -10
Your license for Instr_Control_Toolbox has expired. 
If you are not using a trial license contact your License Administrator to obtain an updated license. 
Otherwise, contact your Sales Representative for a trial extension.

Troubleshoot this issue by visiting: 
https://www.mathworks.com/support/lme/R2020a/10

Diagnostic Information:
Feature: Instr_Control_Toolbox 
License path: C:\Users\vorms\AppData\Roaming\MathWorks\MATLAB\R2020a_licenses;C:\Program Files\MATLAB\R2020a\licenses\license.dat;C:\Program Files\MATLAB\R2020a\licenses\network.lic;C:\Program Files\MATLAB\R2020a\licenses\trial_11202164_R2020a.lic 
Licensing error: -10,32. 

warning :
Parameter precision loss occurred for 'opacity' of 'Ball_Detection_and_PID/Draw Shapes'. The parameter's value cannot be represented exactly using the run-time data type. A small quantization error has occurred. To disable this warning or error, in the Configuration Parameters > Diagnostics > Data Validity pane, set the 'Detect precision loss' option in the Parameters group to 'none'. [3 similar]

erreur :
An error occurred while running the simulation and the simulation was terminated
Caused by:
Domain error. To compute complex results from real x, use 'asin(complex(x))'.
	Error in asin.m (line 14)
		        coder.internal.error('Coder:toolbox:ElFunDomainError',mfilename);
	Error in 'Ball_Detection_and_PID/PosToPlateAngle' (line 3) 
