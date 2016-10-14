#!/usr/bin/env python
import sys

current_torn = None
current_tz_count = 0

print("startID\tendID\tTime Zone\tCount")

for line in sys.stdin:
	line = line.strip()
	tz, tornID = line.split("\t", 1)
	try:
		tz = float(tz)
	except ValueError:
		continue

	if current_tz_count < 1:
		startID = tornID
		endID = tornID    
		current_tz = tz

	if  current_tz == tz:
		endID = tornID
		current_tz_count += 1
	else:
		if tornID:
			print ("%s\t%s\t%s\t%s" % (startID, endID, current_tz, current_tz_count))
		startID = tornID
		endID = tornID
		current_tz = tz
		current_tz_count = 1

print ("%s\t%s\t%s\t%s" % (startID, endID, tz, current_tz_count))

