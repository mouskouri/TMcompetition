from csv import DictReader

train = 'train_deal_validation.csv'  # path to training file

test = 'train_user.csv'

splitime = '12-18-00'
if_validation = True

user_dic = {}
user_list = []
user_buy_time_nearest = {}
user_nearest_date_of_week = {}
user_last_7_day = {}
cart_dic = {}

def data(path, flag):
	#count = 0

	for t, row in enumerate(DictReader(open(path))):
		#count += 1
		time = row['time'].split()
		time[0] = time[0][5:]
		time = '-'.join(time)   #time = 11-26-20

		if(if_validation):
			if(flag == 'train'):
				cart_time = '1216'
			else:
				cart_time = '1217'
		else:
			if(flag == 'train'):
				cart_time = '1217'
			else:
				cart_time = '1218'


		if((flag == 'test') and (if_validation)):
			if(time > splitime):
				continue

		if row['item_id'] not in user_dic:
			user_dic[row['item_id']] = [0,0,0,0]

		user_dic[row['item_id']][int(row['behavior_type'])-1] += 1

		#cal date of user buy
		date = row['time'].split()
		date = date[0][5:].split('-')
		date = ''.join(date)   #1120

		#if((date == cart_time) and (row['behavior_type'] == '3')):
			#if(row['item_id'] not in cart_dic):
				#cart_dic[row['item_id']] = 0
			#cart_dic[row['item_id']] += 1
		
		if(row['item_id'] not in cart_dic):
			cart_dic[row['item_id']] = [0,0,0,0]
		if(date == cart_time):
			cart_dic[row['item_id']][int(row['behavior_type'])-1] += 1


		if(row['behavior_type'] == '4'):
			
			if(row['item_id'] not in user_buy_time_nearest):
				user_buy_time_nearest[row['item_id']] = date

			if(date > user_buy_time_nearest[row['item_id']]):
				user_buy_time_nearest[row['item_id']] = date

		#cal nearest date of a week
		if(row['item_id'] not in user_nearest_date_of_week):
			user_nearest_date_of_week[row['item_id']] = []

		if(len(user_nearest_date_of_week[row['item_id']])<8):
			user_nearest_date_of_week[row['item_id']].append(date)
		else:
			user_nearest_date_of_week[row['item_id']].sort()
			if(date > user_nearest_date_of_week[row['item_id']][0]):
				user_nearest_date_of_week[row['item_id']][0] = date

		#if count == 100:
			#break

	for t, row in enumerate(DictReader(open(path))):

		time = row['time'].split()
		time[0] = time[0][5:]
		time = '-'.join(time)   #time = 11-26-20	

		if((if_validation) and (flag == 'test')):
			if(time > splitime):
				continue

		last_7_day = user_nearest_date_of_week[row['item_id']]

		date = row['time'].split()
		date = date[0][5:].split('-')
		date = ''.join(date)   #1120

		if(date in last_7_day):
			if(row['item_id'] not in user_last_7_day):
				user_last_7_day[row['item_id']] = [0,0,0,0]

			user_last_7_day[row['item_id']][int(row['behavior_type'])-1] += 1


	for key in user_dic:
		item_hot_level = float(user_dic[key][0])*0.1+float(user_dic[key][3])*5+float(user_dic[key][1])+float(user_dic[key][2])

		user_click_buy_rate = float(user_dic[key][3]) / (float(user_dic[key][0])+float(user_dic[key][1])+float(user_dic[key][2])+float(user_dic[key][3]))
		user_dic[key].append(user_click_buy_rate)
		user_dic[key].append(item_hot_level)

	if('320395600' not in cart_dic):
		print 'hello'



	#userdic = sorted(user_dic.items(), key = lambda d:d[1][3], reverse = True)
	#print user_buy_time


def construct(path):

	with open(path, 'w') as user:

		user.write('item_id,item_last_day_click_count,item_last_day_collect_count,item_last_day_cart_count,item_last_day_buy_count,item_buy_count,item_click_count,item_collect_count,item_cart_count,item_click_buy_rate,item_hot_level,item_least_buy_day_count,item_last_7_day_click_count,item_last_7_day_buy_count,item_last_7_day_collect_count,item_last_7_day_cart_count\n')
		for key in user_dic:
			#cart_count = 0
			#if(key in cart_dic):
				#cart_count = cart_dic[key]
			user_least_buy_day = '0000'
			if(key in user_buy_time_nearest):
				user_least_buy_day = user_buy_time_nearest[key]
			user.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (key,
				cart_dic[key][0],
				cart_dic[key][1],
				cart_dic[key][2],
				cart_dic[key][3],
				user_dic[key][3],
				user_dic[key][0],
				user_dic[key][1],
				user_dic[key][2],
				user_dic[key][4],
				user_dic[key][5],
				user_least_buy_day,
				user_last_7_day[key][0],
				user_last_7_day[key][3],
				user_last_7_day[key][1],
				user_last_7_day[key][2]))


#data(train)
#data(train,'train')
data(test,'test')
construct('test_item_feature.csv')
