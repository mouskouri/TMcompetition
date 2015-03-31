from csv import DictReader
import matplotlib.pyplot as plt

train = 'train_deal.csv'  # path to training file
test = 'train_user.csv'

user_dic = {}
user_list = []
user_buy_time_nearest = {}
user_nearest_date_of_week = {}
user_last_7_day = {}

def data(path):
	#count = 0

	for t, row in enumerate(DictReader(open(path))):
		#count += 1

		if row['user_id'] not in user_dic:
			behave = [0,0,0,0]
			user_dic[row['user_id']] = behave

		user_dic[row['user_id']][int(row['behavior_type'])-1] += 1

		#cal date of user buy
		date = row['time'].split()
		date = date[0][5:].split('-')
		date = ''.join(date)   #1120

		if(row['behavior_type'] == '4'):
			
			if(row['user_id'] not in user_buy_time_nearest):
				user_buy_time_nearest[row['user_id']] = date

			if(date > user_buy_time_nearest[row['user_id']]):
				user_buy_time_nearest[row['user_id']] = date

		#cal nearest date of a week
		if(row['user_id'] not in user_nearest_date_of_week):
			user_nearest_date_of_week[row['user_id']] = []

		if(len(user_nearest_date_of_week[row['user_id']])<8):
			user_nearest_date_of_week[row['user_id']].append(date)
		else:
			user_nearest_date_of_week[row['user_id']].sort()
			if(date > user_nearest_date_of_week[row['user_id']][0]):
				user_nearest_date_of_week[row['user_id']][0] = date

		#if count == 100:
			#break

	for t, row in enumerate(DictReader(open(path))): 
		last_7_day = user_nearest_date_of_week[row['user_id']]

		date = row['time'].split()
		date = date[0][5:].split('-')
		date = ''.join(date)   #1120

		if(date in last_7_day):
			if(row['user_id'] not in user_last_7_day):
				user_last_7_day[row['user_id']] = [0,0,0,0]

			user_last_7_day[row['user_id']][int(row['behavior_type'])-1] += 1


	for key in user_dic:
		user_click_buy_rate = float(user_dic[key][3]) / float(user_dic[key][0])
		user_dic[key].append(user_click_buy_rate)


	#userdic = sorted(user_dic.items(), key = lambda d:d[1][3], reverse = True)
	#print user_buy_time


def construct():

	with open('test_user_feature.csv', 'w') as user:

		user.write('user_id,user_buy_count,user_click_count,user_collect_count,user_cart_count,user_click_buy_rate,user_least_buy_day_count,user_last_7_day_click_count,user_last_7_day_buy_count,user_last_7_day_collect_count,user_last_7_day_cart_count\n')
		for key in user_dic:
			user_least_buy_day = '0000'
			if(key in user_buy_time_nearest):
				user_least_buy_day = user_buy_time_nearest[key]
			user.write('%s,%s,%s,%s,%s,%f,%s,%s,%s,%s,%s\n' % (key,user_dic[key][3],user_dic[key][0],user_dic[key][1],
				user_dic[key][2],
				user_dic[key][4],
				user_least_buy_day,
				user_last_7_day[key][0],
				user_last_7_day[key][3],
				user_last_7_day[key][1],
				user_last_7_day[key][2]))


data(test)
construct()
