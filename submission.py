from csv import DictReader

submission = 'submission.csv'  # path to training file
user_item_result = {}

def data(path):
	#count = 0

	for t, row in enumerate(DictReader(open(path))):
		#count += 1
		Eid = []
		Eid.append(row['user_id'])
		Eid.append(row['item_id'])
		Eid = tuple(Eid)

		user_item_result[Eid] = float(row['click'])		
		
	user_item = sorted(user_item_result.items(), key = lambda d:d[1], reverse = True)
	

	count = 0

	with open('submission_sort.csv', 'w') as submission:
		submission.write('user_id,item_id\n')
		for key in user_item:
			user_id = key[0][0]
			item_id = key[0][1]
			rate = key[1]
			if(rate >= 0.016):
				count  += 1
				submission.write('%s,%s\n' % (user_id,item_id))

	print count

data(submission)
