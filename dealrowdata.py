from csv import DictReader

train_user = 'train_user.csv'  # path to training file

user_item_label = {}

user_dic = {}
item_dic = {}
user_dop = []
item_dop = []

validation_time = '12-17-00'
splitime = '12-18-00'
if_validation = True

#cal user_behave_count
def cal_abnormal(path):

	for t, row in enumerate(DictReader(open(path))):

		if row['item_id'] not in item_dic:
			item_dic[row['item_id']] = [0,0,0,0]

		item_dic[row['item_id']][int(row['behavior_type'])-1] += 1

		
		if row['user_id'] not in user_dic:
			user_dic[row['user_id']] = [0,0,0,0]

		user_dic[row['user_id']][int(row['behavior_type'])-1] += 1


	userdic = sorted(user_dic.items(), key = lambda d:d[1][3], reverse = True)
	itemdic = sorted(item_dic.items(), key = lambda d:d[1][3], reverse = True)

	for user in userdic:
		if(((user[1][0] > 1000) and (user[1][3] == 0)) or (user[1][0] > 5000 and (user[1][3] <= 10))):
			user_dop.append(user[0])

	for item in itemdic:
		if(((item[1][0] > 1000) and (item[1][3] == 0))):
			item_dop.append(item[0])

#bulid label dic
def build_label(path):
	validation_dic = {}

	for t, row in enumerate(DictReader(open(path))):
		date = row['time'].split()
		date[0] = date[0][5:]
		time = '-'.join(date)   #time = 11-26-20
		row['time'] = time

		Eid = [row['user_id'], row['item_id']]
		Eid = ','.join(Eid)

		if(if_validation):
			if (((time > validation_time) and (time <= splitime)) and (row['behavior_type'] == '4')):
				if Eid not in user_item_label:
					user_item_label[Eid] = 0

			if ((time > splitime) and (row['behavior_type'] == '4')):
				if row['user_id'] not in validation_dic:
					validation_dic[row['user_id']] = {}
				if row['item_id'] not in validation_dic[row['user_id']]:
					validation_dic[row['user_id']][row['item_id']] = 0

		else:
			if ((time > splitime) and (row['behavior_type'] == '4')):
				if Eid not in user_item_label:
					user_item_label[Eid] = 0	

	if(if_validation):
		with open('validation_buy.csv', 'w') as validation:
			validation.write('user_id,item_id\n')
			for user in validation_dic:
				for item in validation_dic[user]:
					validation.write('%s,%s\n' % (user, item))
	
		
#bulid train data
def construct_train(path):
	count1 = 0
	count = 0
	drop = 0

	with open('train_deal_validation.csv', 'w') as train:

		train.write('user_id,item_id,label,behavior_type,user_geohash,item_category,time\n')

		for t, row in enumerate(DictReader(open(path))):

			if((row['user_id'] in user_dop) or (row['item_id'] in item_dop)):
				drop += 1
				continue

			date = row['time'].split()
			date[0] = date[0][5:]
			time = '-'.join(date)   #time = 11-26-20

			Eid = [row['user_id'], row['item_id']]
			Eid = ','.join(Eid)

			label_time = splitime

			if(if_validation):
				label_time = validation_time

			if (time <= label_time):
				count += 1
				label = '0'
				if (Eid in user_item_label):
					count1 += 1
					label = '1'
					#print Eid
				train.write('%s,%s,%s,%s,%s,%s,%s\n' % (row['user_id'],row['item_id'],label,row['behavior_type'],row['user_geohash'],row['item_category'],row['time']))

	print count
	print count1
	print drop

cal_abnormal(train_user)
build_label(train_user)
construct_train(train_user)
#print len(item_dop)


