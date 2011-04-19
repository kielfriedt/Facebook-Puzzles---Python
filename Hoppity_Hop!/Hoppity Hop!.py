import sys;

if (len(sys.argv) > 2):
	sys.exit("Error: see arguments");
arg = sys.argv[1];
try:
	fp = open(arg, 'r');
	try:
		value = int(fp.readline());
		for x in xrange(1,value+1):
			if(x % 5 == 0 and x % 3 == 0):
				print("Hop\n");
			elif(x % 5 == 0):
				print("HopHop\n");
			elif(x %3 == 0):
				print("Hoppity\n");
	finally:                                    
		fp.close();
except IOError:
      sys.exit("cannot open " + arg);
	

