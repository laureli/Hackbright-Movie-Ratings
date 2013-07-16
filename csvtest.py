import csv


with open('seed_data/u.data', 'rb') as csvfile:
	f = csv.reader(csvfile, delimiter = '	', quotechar='|')
	for row in f:
		#i made some loops for dubugging purposes.  check them out!
		print 'this is a user_id->',row[0]
		print 'this is item_id ->', row[1]
		print 'this is rating ->', row[2]
		print 'this is timestam ->', row[3]
# #i removed the .join function from the above loop for debugging purposes
# #and because i think we want to information in discrete chunks
# 		print ', '.join(row)




# from model import Rating 
# import csv

# with open('seed_data/u.data', 'rb') as csvfile:
# 	f = csv.reader(csvfile, delimiter = '	', quotechar='|')
# 	for row in f:
# 		rating = Ratings(movie_id=row[1], user_id=row[0], rating=row[2])
# 		session.add(rating)

# # 		session.commit()


# with open('seed_data/u.user', 'rb') as csvfile:
#     f = csv.reader(csvfile, delimiter = "  ", quotechar='|')
#     for row in f:
#     	print row 
#     	# print row[1][0]
#     	# print row[3]
#     	# print row[4]
        #     user = User(age=row[1], zipcode=row[4])
        #     session.add(user)
        # session.commit()