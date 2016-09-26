#!/usr/bin/python

import datetime
import string
import sys

inputfile = "export.csv"
outputfile = "graph-unsorted.csv"

fin = open(inputfile, "r")
fout = open(outputfile, "w")

for l in fin:
	a = l.split(",")
	app = a[8]
	user = a[2]
	subnet = str(a[6])

	if (subnet=="10.200"):
		csvrow = "\n" + app + "," + user
		fout.write(csvrow)


fin.close()
fout.close()
