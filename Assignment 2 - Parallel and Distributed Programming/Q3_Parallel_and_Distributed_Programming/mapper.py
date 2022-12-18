#!/usr/bin/env python

import sys

for line in sys.stdin:
	line = line.strip()
	cols = line.split(',')
	department = cols[5]
	compensation = float(cols[6][1:])
	print ('%s\t%s' % (department,compensation))
