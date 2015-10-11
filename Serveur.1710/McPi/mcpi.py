#!/usr/bin/python
import sys

print "[Begin] Create structure"

print ("Script name: %s" % str(sys.argv[0]))
print ("First argument: %s" % str(sys.argv[1]))
print ("Second argument: %s" % str(sys.argv[2]))

fo = open("mcpi.txt", "wb")
fo.write("mcpi " + str(sys.argv[1]) + " " + str(sys.argv[2]) + "\n")
fo.close()

print "[End] Create structure"
