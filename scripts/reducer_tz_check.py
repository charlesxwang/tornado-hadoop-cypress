#!/usr/bin/env python
import sys

current_torn = None
current_tz_sum = 0
current_tz_count = 0

#torns = sys.stdin
#torns.sort(key=lambda x:x[2])
#print(torns[0].strip())

for line in sys.stdin:
  line = line.strip()
  tornID, tz = line.split("\t", 1)
  try:
    tz = float(tz)
  except ValueError:
    continue

  if current_tz_count < 1:
	startID = tornID    
	current_tz = tz

  if  current_tz == tz:
	endID = tornID
	current_tz_count += 1
  else:
    if tornID:
      #rating_average = current_rating_sum / current_rating_count
      print ("%s\t%s\t%s\t%s" % (startID, endID, tz, current_tz_count))
    startID = tornID
    endID = tornID
    current_tz = tz
    current_tz_count = 1

print ("%s\t%s\t%s\t%s" % (startID, endID, tz, current_tz_count))
#if current_movie == movie:
#  rating_average = current_rating_sum / current_rating_count
#  print ("%s\t%s" % (current_movie, rating_average))  
#print ("%s\t%s\t%s\t%s" % (current_movie, rating_average, current_rating_sum, current_rating_count))
