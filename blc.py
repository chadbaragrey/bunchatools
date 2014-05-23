# Python Black List checker - Prototype
# Version 0.0.4

import re, socket, sys, getopt
	
#globals
blacklists = []
ip = sys.argv[1]
ip_rev = ''

#open file with all of the blacklist sites to check.
#turn the file into a list and remove the newline characters
blacklists = open('blacklist_sites', 'r').readlines()
for index in range(len(blacklists)):
	blacklists[index] = blacklists[index].rstrip('\n')
	
#Reverse IP address
def reverse_ip(ip):
	global ip_rev
	ip_rev = '.'.join(re.split('\.', ip)[::-1])

#Check our IP against a list of blacklists, 
#returns a message if it is on the list or if the BL hostname is invalid.
def blacklist_check(ip, ip_rev):

	result = ip + '\n'

	for blist in blacklists:
		try:
			socket.gethostbyname(ip_rev + '.' + blist)
			result += blist + '\n'
			
		except socket.gaierror:
			result += 'Hostname error: ' + ip + '.' + blist + ' invalid.\n' 
	sys.exit(result)
	
reverse_ip(ip)
blacklist_check(ip, ip_rev)
