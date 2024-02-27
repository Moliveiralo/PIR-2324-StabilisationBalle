%Ce programme a pour fonction de : 
% - Charger le fichier de correspondance AnglePlateau->AngleServos généré
%   grâce au programme Python de Johan Link
% - Convertir les données en Lookup Table afin de les rendres exploitables
%   par Simulink
load('data.mat');
xrange = min(data.alpha):0.2:max(data.alpha);
yrange = min(data.beta):0.2:max(data.beta);

[Alpha,Beta]=meshgrid(xrange,yrange);

AValues=griddata(data.alpha,data.beta,data.AngleservoA,Alpha,Beta);
BValues=griddata(data.alpha,data.beta,data.AngleservoB,Alpha,Beta);
CValues=griddata(data.alpha,data.beta,data.AngleservoC,Alpha,Beta);
