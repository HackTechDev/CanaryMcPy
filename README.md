Canary Mod + Minecraft Python
=============================

1) Install Inotify

[~] ➔ apt-get install inotify-tools

2) Run inotify :

[~/JEUX/MINECRAFT.v4/Serveur.1710] ➔ ./notifyMcPi.sh 

3) Script to build a structure :

[~/JEUX/MINECRAFT.v4/Serveur.1710/McPi] ➔ ls -l  
total 36  
lrwxrwxrwx 1 nekrofage nekrofage     9 oct.   7 20:52 createStructure.py -> pillar.py  
-rwxrwxr-x 1 nekrofage nekrofage   552 oct.   7 20:45 pillar.py  

4) Build the Canary Mod plugin :
 
[~/JEUX/MINECRAFT.dev/CanaryMcPy/CanaryMod/McPi] ➔ ./build.sh 
 
5) Canary Mod plugin : 

[~/JEUX/MINECRAFT.v4/Serveur.1710/plugins] ➔ ls -l  
total 196  
-rw-rw-r-- 1 nekrofage nekrofage   2240 oct.   7 21:03 McPi.jar  

6) In the Minecraft client, call the plugin :

/mcpi
