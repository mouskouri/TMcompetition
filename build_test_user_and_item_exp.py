from csv import DictReader

train_user = 'train_user.csv'  # path to training file
train_item = 'train_item.csv'  # path to testing file

test_user_feature = 'test_user_feature.csv'
test_item_feature = 'test_item_feature.csv'
test_user_and_item_feature = 'test_user_and_item_feature.csv'

item_userdic = {}
item_dop = []
user_dop = []
item_test_dic = {}

def cal_abnormal(path):
	item_dic = {}
	user_dic = {}

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


def cal_item_user_dic(path):

	for t, row in enumerate(DictReader(open(path))):
		if((row['item_id'] in item_dop) or(row['user_id'] in user_dop)):
			continue
		if(row['item_id'] not in item_userdic):
			item_userdic[row['item_id']] = []
		item_userdic[row['item_id']].append(row['user_id'])


def cal_inter_item(path):

	for t, row in enumerate(DictReader(open(path))):
		if(row['item_id'] in item_userdic):
			item_test_dic[row['item_id']] = row['item_category']

		
def build_user_item_exp():

	with open('test_user_item.csv', 'w') as test:
		test.write('user_id,iten_id,item_category\n')
		for item in item_test_dic:
			user_list = item_userdic[item]
			for user in user_list:
				test.write('%s,%s,%s\n' % (user,item,item_test_dic[item]))


cal_abnormal(train_user)
cal_item_user_dic(train_user)
cal_inter_item(train_item)
build_user_item_exp()
#print item_drop
