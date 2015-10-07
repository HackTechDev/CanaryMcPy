#!/bin/sh
while inotifywait -e modify mcpi.txt; do
	./McPi/createStructure.py
done
