# Python Black List checker - Prototype
# Version 0.0.1

import socket, re

blacklists = ['b.barracudacentral.org', 'dnsbl.anticaptcha.net']
ip = raw_input('Enter an IP address: ')
ip_rev = ''

def reverse_ip(ip):
	global ip_rev
	ip_rev = '.'.join(re.split('\.', ip)[::-1])

def blacklist_check(ip, ip_rev):
	for blist in blacklists:
		try:
			socket.gethostbyname(ip_rev + '.' + blist)
			print 'IP: ' + ip + ' is on the ' + blist + ' blacklist.'
			
		except socket.gaierror:
			pass

reverse_ip(ip)
blacklist_check(ip, ip_rev)
