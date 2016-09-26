#!/usr/bin/python

import urllib2
import ssl
import json
import datetime
import string

step = 5000
events = 7179715
output = "export.csv"
urlbase = "https://10.200.95.192/api/v1/events?token=5ded82019a30f44c89baf19f9933798a&type=connection&timeperiod=2592000&limit=" + str(step) + "&skip="


totalcalls = int(events/step)


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


f = open(output, "w")

csvrow = "timestamp,date,user,os,browser,srcip,subnet,device,app,ccl,app_category,dstip,dstport,dst_country,req_cnt,resp_cnt,count,client_bytes,server_bytes,numbytes,conn_duration"
f.write(csvrow)

for s in range(0, totalcalls):
	url = urlbase + str(s*step)

	print (url)

	req = urllib2.Request(url)
	response = urllib2.urlopen(req, context=ctx)
	content = response.read()
	js = json.loads(content)

	for j in js["data"]:
		timestamp = str(j["timestamp"])
		date = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
		user = j["user"]
		os = j["os"]
		browser = j["browser"]
		srcip = j["srcip"]
		subnet = srcip.split(".")[0] + "." + srcip.split(".")[1]
		device = j["device"]
		app = j["app"]
		ccl = j["ccl"]
		app_category = j["appcategory"]
		dstip = j["dstip"]
		dstport = str(j["dstport"])
		dst_country = j["dst_country"]

		req_cnt = str(j["req_cnt"])
		resp_cnt = str(j["resp_cnt"])
		count = str(j["count"])
		client_bytes = str(j["client_bytes"])
		server_bytes = str(j["server_bytes"])
		numbytes = str(j["numbytes"])
		conn_duration = str(j["conn_duration"])


		csvrow = timestamp + "," + date + "," + user + "," + os + "," + browser + "," + srcip + "," + subnet + "," + device
		csvrow = csvrow + "," + app + "," + ccl + "," + app_category + "," + dstip + "," + dstport + "," + dst_country
		csvrow = csvrow + "," + req_cnt + "," + resp_cnt + "," + count + "," + client_bytes + "," + server_bytes + "," + numbytes + "," + conn_duration

		f.write('\n' + csvrow)
		

f.close()
