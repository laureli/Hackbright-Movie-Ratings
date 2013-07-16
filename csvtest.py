import csv


with open('seed_data/u.data', 'rb') as csvfile:
	f = csv.reader(csvfile, delimiter = '	', quotechar='|')
	for row in f:
		#i made some loops for dubugging purposes.  check them out!
		print 'this is a user_id->',row[0]
		print 'this is item_id ->', row[1]
		print 'this is rating ->', row[2]
		print 'this is timestam ->', row[3]

#i removed the .join function from the above loop for debugging purposes
#and because i think we want to information in discrete chunks
		print ', '.join(row)




# with open('seed_data/u.data', 'rb') as csvfile:
# 	f = csv.reader(csvfile, delimiter = '	', quotechar='|')
# 	counter = 10
# 	while counter >0:
# 		for row in f:
# 			print ',  '.join(row)
# 		counter = counter - 1

