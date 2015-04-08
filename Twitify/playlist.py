#!/usr/bin/env python

import sys
import json
import cgi
fs = cgi.FieldStorage()

print "Content-Type: application/json"

print "\n"
print "\n"


result = {}
d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

print json.dumps(d,indent=1)
print "\n"

sys.stdout.close()