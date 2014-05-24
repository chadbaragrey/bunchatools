# MX record lookup tool - Prototype
# Version 0.0.0
# Requires DNSPython - www.dnspython.org

import dns.resolver, sys

hostname = sys.argv[1]
rec_type = 'mx' #String of the record type: A, MX, NS

results = ''

try:
    records = dns.resolver.query(hostname, rec_type)
    for rec in records:
        results = results + rec.to_text() + '\n'
    sys.exit(results)
    
except dns.resolver.NoAnswer:
    pass

except dns.resolver.NXDOMAIN:
    pass

except dns.resolver.YXDOMAIN:
    pass

except dns.resolver.NoNameservers:
    pass

except dns.resolver.Timeout:
    pass