# Python Black List checker - Prototype
# Date 5/24/2014
# Version 0.0.9

import re, socket, sys, getopt

#globals
blacklists = []
ip = ''
ip_rev = ''
ip_valid = False
host = ''

socket.setdefaulttimeout(30)

#open file with all of the blacklist sites to check.
#turn the file into a list and remove the newline characters
def blacklist_file():
    global blacklists
    rbl_file = open('blacklist_sites', 'r')
    blacklists = rbl_file.readlines()
    rbl_file.close()
    
    for index in range(len(blacklists)):
        blacklists[index] = blacklists[index].rstrip('\n')

#check that the IP is valid & reverse it.
def ip_check():
    global ip, ip_rev, ip_valid
    result = ''
    split_ip = re.split('\.', ip)
    
    if len(split_ip) == 4:
        for x in range(len(split_ip)):
            try:
                split_ip[x] = int(split_ip[x])
                
            except:
                result = 'Invalid IP address'
                sys.exit(result)
                
            if split_ip[x] > -1 and split_ip[x] < 256:
                split_ip[x] = str(split_ip[x])
                
            else:
                result = 'Invalid IP address'
                sys.exit(result)
                
        ip = '.'.join(split_ip)
        ip_rev = '.'.join(re.split('\.', ip)[::-1])
        
        ip_valid = True
    
    else:
        result = 'Invalid IP address'
        sys.exit(result)

#Check our IP against a list of blacklists, 
#returns a message if it is on the list or if the BL hostname is invalid.
def blacklist_check():
    result = ip + '\n'
    if ip_valid:
        for blist in blacklists:
            try:
                socket.gethostbyname(ip_rev + '.' + blist)
                result += blist + '\n'
            except socket.gaierror as err:
                result += err + '\n'
            except socket.timeout:
                result += 'timeout' + blist + '\n'
        sys.exit(result)

def main():
	global ip, host
	try:
		opts, args = getopt.getopt(sys.argv[1:], "i:h:", ["ipaddress=", "hostname="])

	except getopt.GetoptError:
		sys.exit('arg error')

	for opt, arg in opts:
		if opt in ('-i', '--ipaddress'):
			ip = arg

			ip_check()
			blacklist_check()

		elif opt in ('-h', '--hostname'):
			host = arg

if __name__ == '__main__':
	blacklist_file()
	main()
  
