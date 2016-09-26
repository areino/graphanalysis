#!/usr/bin/python

import string
import array

#inputfile = "testinput.csv"
inputfile = "graph-summary.csv"
outputfile = "cluster.csv"
k = 0

# Load input file and load into memory array
fin = open(inputfile, "r")
fina = fin.readlines()
finb = []
for l in fina:
	finb.append(l.strip().split(","))
fin.close()


d = dict()
for l in finb:
	app = l[0]
	user = l[1]
	k = k + 1
	print str(153400-k)

	for n in finb:
		user2 = n[1]
		app2 = n[0]
		dkey = "%s|%s" % (app, app2)
		ikey = "%s|%s" % (app2, app)
		if dkey<ikey:
			key = dkey
		else:
			key = ikey

		if (user==user2) and (app!=app2):
			if d.has_key(key):
				d[key] = d[key] + 1
			else:
				new = {key: 1}
				d.update(new)

# Write output CSV
fout = open(outputfile, "w")
for s in d:
	ss = s.split("|")
	app1 = ss[0]
	app2 = ss[1]
	users = d[s]
	fout.write(app1 + "," + app2 + "," + str(users) + "\n")
fout.close()

