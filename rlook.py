# MX record lookup tool - Prototype
# Version 0.0.0
# Requires DNSPython - www.dnspython.org

import dns.resolver

hostname = ''
rec_type = '' #String of the record type: A, MX, NS
records = dns.resolver.query(hostname, rec_type)

for rec in records:
	print rec
