#!/usr/bin/env python

from operator import itemgetter
import sys

prev_department = None
prev_salary = 0
department = None

for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	department, salary = line.split('\t', 1)
	try:
		salary = float(salary)
	except ValueError:
		continue

	if prev_department == department:
		prev_salary += salary
	else:
		if prev_department:
			print ('Total salary of %s department is $%s' % (prev_department, prev_salary))
		prev_salary = salary
		prev_department = department

# do not forget to output the last curr_word if needed!
if prev_department == department:
	print ('Total salary of %s department is $%s' % (prev_department, prev_salary))
