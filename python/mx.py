# MX record lookup tool - Prototype
# Version 0.0.1
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
    
except dns.resolver.NoAnswer as err:
    sys.exit(err)

except dns.resolver.NXDOMAIN as err:
    sys.exit(err)

except dns.resolver.YXDOMAIN as err:
    sys.exit(err)

except dns.resolver.NoNameservers as err:
    sys.exit(err)

except dns.resolver.Timeout as err:
    sys.exit(err)
