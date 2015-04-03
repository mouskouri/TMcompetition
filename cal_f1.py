from csv import DictReader

validation = 'validation_buy.csv'
submission = 'tianchi_mobile_recommendation_predict.csv'  # path to training file
train_item = 'train_item.csv' 

item_dic = {}
user_item = {}

def data(train_item, validation, submission):
	real_p = 0
	pre_p = 0
	tp = 0

	for t, row in enumerate(DictReader(open(train_item))):
		#count += 1
		if(row['item_id'] not in item_dic):
			item_dic[row['item_id']] = 0

	for t, row in enumerate(DictReader(open(validation))):

		if(row['item_id'] in item_dic):
			Eid = [row['user_id'], row['item_id']]
			Eid = ','.join(Eid)

			if(Eid not in user_item):
				user_item[Eid] = 0

			real_p += 1

	for t, row in enumerate(DictReader(open(submission))):

		pre_p += 1

		Eid = [row['user_id'], row['item_id']]
		Eid = ','.join(Eid)
		if(Eid in user_item):
			tp += 1

	precision = float(tp) / float(pre_p)
	recall = float(tp) / float(real_p)
	f1 = float(2*tp) / float(pre_p + real_p)
	print precision,recall,f1

data(train_item, validation, submission)
