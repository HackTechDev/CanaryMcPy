#!/bin/sh

echo Minecraft

cd Serveur.1710
xterm -sb -geometry 100x30+0+0 -title ServeurMinecraft -e ./lancerServeurMinecraft.Canary.sh &
