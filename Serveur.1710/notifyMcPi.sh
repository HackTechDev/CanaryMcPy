#!/bin/sh
while inotifywait -e modify mcpi.txt; do
    mcpiScript=`./parseMcPi.py`
    eval $mcpiScript
done
