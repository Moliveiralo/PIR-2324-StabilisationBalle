Code Python

Configurer une carte Raspberry :

Pour lancer le code sur la carte Raspberry Pi il faut :
- Se connnecter au Raspberry en SSH
  1. Lancer un terminal sur l'ordinateur
  2. Taper la commande : ssh pi@[ip_du_raspberry]
- Envoyer le fichier à lancer à la raspberry  
Avec interface graphique winSCP
  1. Ouvrir sur windows winSCP
  2. Choisir la connexion FTP
  3. Nom d'hote = adresse ip du raspberry
  4. Mot de passe et Nom d'utilisateur choisi à la configuration de la carte
     
Sans interface graphique
  1. Ouvrir un autre terminal
  2. Se placer dans le dossier où est situé le fichier à envoyer
  3. Tapper scp nom_fichier.py pi@[ip_du_raspberry]:/home/pi
   
- Run le code :  Taper la commande dans le terminal ouvert précedement : sudo python nom_fichier.py
  
Pour modifier le fichier directement sur le Raspberry la commande est : nano nom_fichier.py
  
Sources interressantes  
https://github.com/nicohmje/PID-ballonplate/tree/main   
