Code Python

Configurer une carte Raspberry :

Pour lancer le code sur la carte Raspberry Pi il faut :
1. Se connnecter au Raspberry en SSH
- Lancer un terminal sur l'ordinateur
- Taper la commande : ssh pi@[ip_du_raspberry]

2.  Envoyer le fichier à lancer à la raspberry
  
Avec interface graphique winSCP
- Ouvrir sur windows winSCP
- Choisir la connexion FTP
- Nom d'hote = adresse ip du raspberry
- Mot de passe et Nom d'utilisateur choisi à la configuration de la carte  
  
Sans interface graphique
- Ouvrir un autre terminal
- Se placer dans le dossier où est situé le fichier à envoyer
- Tapper scp nom_fichier.py pi@[ip_du_raspberry]:/home/pi
   
3. Run le code :  Taper la commande dans le terminal ouvert précedement : sudo python nom_fichier.py
  
Pour modifier le fichier directement sur le Raspberry la commande est : nano nom_fichier.py
  
Sources interressantes  
https://github.com/nicohmje/PID-ballonplate/tree/main   
