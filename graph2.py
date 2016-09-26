#!/usr/bin/python

import datetime
import string
import sys

inputfile = "graph-sorted.csv"
outputfile = "graph-summary.csv"

fin = open(inputfile, "r")
fout = open(outputfile, "w")


csvrow = "app,user,sessions"
fout.write(csvrow)

currentapp = ""
currentuser = ""
sessions = 0

for l in fin:
	a = l.split(",")
	app = a[0].strip()
	user = a[1].strip()

	if (currentapp != app) or (currentuser != user):
		csvrow = "\n" + currentapp + "," + user + "," + str(sessions)
		fout.write(csvrow)
		print "[" + str(sessions) +"] " + app + " - " + user
		
		currentapp = app
		currentuser = user
		sessions = 0

	sessions = sessions + 1


fin.close()
fout.close()
