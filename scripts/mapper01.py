#!/usr/bin/env python
import sys                                                                                                
for oneTorn in sys.stdin:                                                                            
  oneTorn = oneTorn.strip()                                                  
  tornInfo = oneTorn.split(",")                                                                       
  tornID = tornInfo[0]                                                                               
  tz = tornInfo[6]                                                                                 
  print ('%s\t%s' % (tornID, tz)) 
