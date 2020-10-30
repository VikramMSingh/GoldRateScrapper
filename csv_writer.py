import os
import csv
def write_data(filename,p1,d1):
	if os.path.exists(filename):
		a_write='a'
	else:
		a_write='w'

	with open(filename,mode=a_write) as csv_file:
		fieldnames=['date','22k rate per 10g']
		writer=csv.DictWriter(csv_file, fieldnames=fieldnames)
		if a_write=='a':
			writer.writerow({'date':d1,'22k rate per 10g':p1})
		else:
			writer.writeheader()
			writer.writerow({'date':d1,'22k rate per 10g':p1})

