from csv import DictReader
import matplotlib.pyplot as plt

train = 'train_user.csv'  # path to training file
test = 'train_item.csv'  # path to testing file

user_dic = {}
user_list = []

def data(path):
	

	for t, row in enumerate(DictReader(open(path))):
		

		if row['item_id'] not in user_dic:
			behave = [0,0,0,0]
			user_dic[row['item_id']] = behave

		user_dic[row['item_id']][int(row['behavior_type'])-1] += 1

		#if count == 100:
			#break

	userdic = sorted(user_dic.items(), key = lambda d:d[1][3], reverse = True)
	print len(user_dic)
	return userdic


def construct(user_dic):

	with open('item_behave_count_by_buy.csv', 'w') as user:

		user.write('item_id,click,conserve,add,buy\n')
		for key in user_dic:
			user.write('%s,%d,%d,%d,%d\n' % (key[0],key[1][0],key[1][1],key[1][2],key[1][3]))


userdic = data(train)
construct(userdic)
