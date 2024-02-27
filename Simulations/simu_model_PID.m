%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Simulation du système plateau + ball %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all
close all 

% Données du système 
 m = 2.7; % Masse de la balle en g
 r = 0.022; % Rayon de la balle en m
 g = 9.81; % en m.s^-2
 R = 26.8/2;% Rayon du plateau
 %I = 2/5*m*r^2*(1-(1-exp(1)/r)^5)/(1-(1-exp(1)/r)^3); %moment d'inertie de la balle
 I = 2/3*m*r^2; 
 
 % Fonctions de transfert du système 
 %numx = -2*m*g*R*r^2;
 %denx = [R*2*(m*r^2+I) 0 0]; 
 
 numx = 5/7*g; 
 denx = [1 0 0];
 
 %numx = m*g;
% denx = [(m+I/r^2) 0 0]; 
 
 deny = denx; 
 numy = numx; 
 
 
 aff=sim('simu_pid.slx')
 plot(aff.entree)
 hold on
 plot(aff.sortie)
 
