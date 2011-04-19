import sys;

#Checks arguments
if (len(sys.argv) > 2):
	sys.exit("Error: see arguments");
arg = sys.argv[1];
try: #Start of try
	fp = open(arg, 'r'); #Opens input file
	try:
		value = int(fp.readline());
		for x in xrange(1,value+1): #Loops through value from 1 to value
			if(x % 5 == 0 and x % 3 == 0):
				print("Hop\n");
			elif(x % 5 == 0):
				print("HopHop\n");
			elif(x %3 == 0):
				print("Hoppity\n");
	finally:                                    
		fp.close(); #Close file pointer
except IOError: #If filename in argument doesn't exist it errors out
      sys.exit("cannot open " + arg);
	

