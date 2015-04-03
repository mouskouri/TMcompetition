from csv import DictReader
import random

train = 'train_deal_validation.csv'  # path to training file

user_item_result = {}
number_list = []
row_train = {}

def build_rand_number(path):

	count = 0
	for t, row in enumerate(DictReader(open(path))):
		count += 1

	for i in range(count):

		number = random.randint(0, count-1)
		number_list.append(number)
		#if(number not in number_dic):
			#number_dic[number] = 0
		#number_dic[number] += 1

	#print number_dic

def build_train_data(path):
	count = 0

	for t, row in enumerate(DictReader(open(path))):
		#count += 1
		row_train[t] = row

	with open('train_deal_validation_boostrap_1.csv', 'w') as train:
		train.write('user_id,item_id,label,behavior_type,user_geohash,item_category,time\n')

		for number in number_list:
			exp = row_train[number]
			train.write('%s,%s,%s,%s,%s,%s,%s\n' % (exp['user_id'],exp['item_id'],exp['label'],exp['behavior_type'],exp['user_geohash'],exp['item_category'],exp['time']))

build_rand_number(train)
build_train_data(train)
#data(submission)
