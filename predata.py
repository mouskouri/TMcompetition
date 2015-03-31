from csv import DictReader

train_user = 'train_user.csv'  # path to training file
test = 'train_item.csv'  # path to testing file

user_item_label = {}

splitime = '12-18-00'

#bulid label dic
def data(path):

	for t, row in enumerate(DictReader(open(path))):
		date = row['time'].split()
		date[0] = date[0][5:]
		time = '-'.join(date)   #time = 11-26-20
		row['time'] = time

		Eid = [row['user_id'], row['item_id']]
		Eid = ','.join(Eid)

		if ((time > splitime) and (row['behavior_type'] == '4')):
			if Eid not in user_item_label:
				user_item_label[Eid] = 0
			#user_item_label[Eid] += 1

#bulid train data
def construct_train(path):
	count1 = 0
	count = 0

	with open('train.csv', 'w') as train:

		train.write('user_id,item_id,label,behavior_type,user_geohash,item_category,time\n')
		for t, row in enumerate(DictReader(open(path))):
			date = row['time'].split()
			date[0] = date[0][5:]
			time = '-'.join(date)   #time = 11-26-20

			Eid = [row['user_id'], row['item_id']]
			Eid = ','.join(Eid)

			if (time <= splitime):
				count += 1
				label = '0'
				if (Eid in user_item_label):
					count1 += 1
					label = '1'
					print Eid
				train.write('%s,%s,%s,%s,%s,%s,%s\n' % (row['user_id'],row['item_id'],label,row['behavior_type'],row['user_geohash'],row['item_category'],row['time']))

	print count
	print count1


data(train_user)
construct_train(train_user)
print len(user_item_label)

