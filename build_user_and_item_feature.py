from csv import DictReader
import matplotlib.pyplot as plt

train = 'train_deal_validation.csv'  # path to training file
test = 'train_user.csv'

splitime = '12-18-00'
if_validation = True

user_and_item_dic = {}
user_list = []
user_and_item_time_nearest = {}
user_and_item_nearest_date_of_week = {}
user_and_item_last_7_day = {}
user_and_item_last_3_day = {}
cart_dic = {}
user_and_item_nearest_date_of_3 = {}
user_and_item_first_buy_day = {}
user_and_item_first_buy_day_behave_count = {}
user_all_behave_count = {}
item_all_behave_count = {}
user_to_item_behave_day_count = {}

def data(path, flag):
	#count = 0

	for t, row in enumerate(DictReader(open(path))):

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

		if((if_validation) and (flag == 'test')):
			if(time > splitime):
				continue

		Eid = []
		Eid.append(row['user_id'])
		Eid.append(row['item_id'])
		Eid = tuple(Eid)
		#count += 1

		if Eid not in user_and_item_dic:
			user_and_item_dic[Eid] = [0,0,0,0]

		user_and_item_dic[Eid][int(row['behavior_type'])-1] += 1

		#cal date of user buy
		date = row['time'].split()
		date = date[0][5:].split('-')
		date = ''.join(date)   #1120

		if(Eid not in user_to_item_behave_day_count):
			user_to_item_behave_day_count[Eid] = {}
		if(row['behavior_type'] not in user_to_item_behave_day_count[Eid]):
			user_to_item_behave_day_count[Eid][row['behavior_type']] = []
		if(date not in user_to_item_behave_day_count[Eid][row['behavior_type']]):
			user_to_item_behave_day_count[Eid][row['behavior_type']].append[date]

		if(Eid not in cart_dic):
			cart_dic[Eid] = [0,0,0,0]
		if(date == cart_time):
			cart_dic[Eid][int(row['behavior_type'])-1] += 1	

		if(row['user_id'] not in user_all_behave_count):
			user_all_behave_count[row['user_id']] = [0,0,0,0]
		user_all_behave_count[row['user_id']][int(row['behavior_type'])-1] += 1

		if(row['item_id'] not in item_all_behave_count):
			item_all_behave_count[row['item_id']] = [0,0,0,0]
		item_all_behave_count[row['item_id']][int(row['behavior_type'])-1] += 1


		if(row['behavior_type'] == '4'):
			if(Eid not in user_and_item_first_buy_day):
				user_and_item_first_buy_day[Eid] = date
			if(date < user_and_item_first_buy_day[Eid]):
				user_and_item_first_buy_day[Eid] = date


			
		#if(Eid not in user_and_item_time_nearest):
			#user_and_item_time_nearest[Eid] = {}
		#if(row['behavior_type'] not in user_and_item_time_nearest[Eid]):
			#user_and_item_time_nearest[Eid][row['behavior_type']] = date

		#if(date > user_and_item_time_nearest[Eid][row['behavior_type']]):
			#user_and_item_time_nearest[Eid][row['behavior_type']] = date

		#cal nearest date of a week
		if(Eid not in user_and_item_nearest_date_of_week):
			user_and_item_nearest_date_of_week[Eid] = []

		if(Eid not in user_and_item_nearest_date_of_3):
			user_and_item_nearest_date_of_3[Eid] = []

		if(len(user_and_item_nearest_date_of_week[Eid])<8):
			user_and_item_nearest_date_of_week[Eid].append(date)
		else:
			user_and_item_nearest_date_of_week[Eid].sort()
			if(date > user_and_item_nearest_date_of_week[Eid][0]):
				user_and_item_nearest_date_of_week[Eid][0] = date

		if(len(user_and_item_nearest_date_of_3[Eid])<3):
			user_and_item_nearest_date_of_3[Eid].append(date)
		else:
			user_and_item_nearest_date_of_3[Eid].sort()
			if(date > user_and_item_nearest_date_of_3[Eid][0]):
				user_and_item_nearest_date_of_3[Eid][0] = date

		#if count == 100:
			#break

	for t, row in enumerate(DictReader(open(path))):

		time = row['time'].split()
		time[0] = time[0][5:]
		time = '-'.join(time)   #time = 11-26-20

		if((flag == 'test') and (if_validation)):
			if(time > splitime):
				continue
		
		Eid = []
		Eid.append(row['user_id'])
		Eid.append(row['item_id'])
		Eid = tuple(Eid)

		last_7_day = user_and_item_nearest_date_of_week[Eid]
		last_3_day = user_and_item_nearest_date_of_3[Eid]

		date = row['time'].split()
		date = date[0][5:].split('-')
		date = ''.join(date)   #1120

		#if(Eid not in user_item_inter_date_of_week_seperate):
			#user_item_inter_date_of_week_seperate[Eid] = {}
			#for i in range(lenth(last_7_day)):
				#user_item_inter_date_of_week_seperate[Eid][i] = [0,0,0,0] 

		if(Eid in user_and_item_first_buy_day): 
			first_day_buy = user_and_item_first_buy_day[Eid]
			if(date < first_day_buy):
				if(Eid not in user_and_item_first_buy_day_behave_count):
					user_and_item_first_buy_day_behave_count[Eid] = [0,0,0]
				user_and_item_first_buy_day_behave_count[Eid][int(row['behavior_type'])-1] += 1


		

		if(date in last_7_day):
			if(Eid not in user_and_item_last_7_day):
				user_and_item_last_7_day[Eid] = [0,0,0,0]

			user_and_item_last_7_day[Eid][int(row['behavior_type'])-1] += 1

		if(date in last_3_day):
			if(Eid not in user_and_item_last_3_day):
				user_and_item_last_3_day[Eid] = [0,0,0,0]

			user_and_item_last_3_day[Eid][int(row['behavior_type'])-1] += 1

	#userdic = sorted(user_dic.items(), key = lambda d:d[1][3], reverse = True)
	#print user_buy_time


def construct(path):

	with open(path, 'w') as user:

		user.write('user_id,item_id,click_day_count,collect_day_count,cart_day_count,buy_day_count,item_is_clicked_rate,item_is_collected_rate,item_is_carted_rate,item_is_bought_rate,buy_2_count,user_click_item_rate,user_collect_item_rate,user_cart_item_rate,user_buy_item_rate,click_count_before_firstbuy,collect_count_before_firstbuy,cart_count_before_firstbuy,last_day_click_count,last_day_collect_count,last_day_cart_count,last_day_buy_count,buy_count,click_count,collect_count,cart_count,last_3_day_click_count,last_3_day_buy_count,last_3_day_collect_count,last_3_day_cart_count,last_7_day_buy_count,last_7_day_collect_count,last_7_day_cart_count\n')
		for key in user_and_item_dic:

			click_count_before_firstbuy = 0
			collect_count_before_firstbuy = 0
			cart_count_before_firstbuy = 0
			if(key in user_and_item_first_buy_day_behave_count):
				click_count_before_firstbuy = user_and_item_first_buy_day_behave_count[key][0]
				collect_count_before_firstbuy = user_and_item_first_buy_day_behave_count[key][1]
				cart_count_before_firstbuy = user_and_item_first_buy_day_behave_count[key][2]

			#least_buy_day = '0000'
			#least_click_day = '0000'
			#least_collect_day = '0000'
			#least_cart_day = '0000'
			#if(key in user_and_item_time_nearest):
				#if('1' in user_and_item_time_nearest[key]):
					#least_click_day = user_and_item_time_nearest[key]['1']
				#if('2' in user_and_item_time_nearest[key]):
					#least_collect_day = user_and_item_time_nearest[key]['2']
				#if('3' in user_and_item_time_nearest[key]):
					#least_cart_day = user_and_item_time_nearest[key]['3']
				#if('4' in user_and_item_time_nearest[key]):
					#least_buy_day = user_and_item_time_nearest[key]['4']

			user_id = key[0]
			item_id = key[1]

			click_day_count = len(user_to_item_behave_day_count[Eid]['1'])			
			collect_day_count = len(user_to_item_behave_day_count[Eid]['2'])
			cart_day_count = len(user_to_item_behave_day_count[Eid]['3'])
			buy_day_count = len(user_to_item_behave_day_count[Eid]['4'])

			if(user_all_behave_count[user_id][0] == 0):
				user_click_item_rate = 0.
			else:
				user_click_item_rate = float(user_and_item_dic[key][0]) / float(user_all_behave_count[user_id][0])

			if(user_all_behave_count[user_id][1] == 0):
				user_collect_item_rate = 0.
			else:
				user_collect_item_rate = float(user_and_item_dic[key][1]) / float(user_all_behave_count[user_id][1]) 

			if(user_all_behave_count[user_id][2] == 0):
				user_cart_item_rate = 0.
			else:
				user_cart_item_rate = float(user_and_item_dic[key][2]) / float(user_all_behave_count[user_id][2])

			if(user_all_behave_count[user_id][3] == 0):
				user_buy_item_rate = 0.	
			else:
				user_buy_item_rate = float(user_and_item_dic[key][3]) / float(user_all_behave_count[user_id][3])



			if(item_all_behave_count[item_id][0] == 0):
				item_is_click_rate = 0.
			else:
				item_is_click_rate = float(user_and_item_dic[key][0]) / float(item_all_behave_count[user_id][0])

			if(item_all_behave_count[item_id][1] == 0):
				item_is_collect_rate = 0.
			else:
				item_is_collect_rate = float(user_and_item_dic[key][1]) / float(item_all_behave_count[user_id][1]) 

			if(item_all_behave_count[item_id][2] == 0):
				item_is_cart_rate = 0.
			else:
				item_is_cart_rate = float(user_and_item_dic[key][2]) / float(item_all_behave_count[user_id][2])

			if(item_all_behave_count[item_id][3] == 0):
				item_is_buy_rate = 0.	
			else:
				item_is_buy_rate = float(user_and_item_dic[key][3]) / float(item_all_behave_count[user_id][3])

			buy_2_count = user_and_item_dic[key][3] * user_and_item_dic[key][3]
															
			user.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (user_id,item_id,
				click_day_count,
				collect_day_count,
				cart_day_count,
				buy_day_count,
				item_is_click_rate,
				item_is_collect_rate,
				item_is_cart_rate,
				item_is_buy_rate,
				buy_2_count,
				user_click_item_rate,
				user_collect_item_rate,
				user_cart_item_rate,
				user_buy_item_rate,
				click_count_before_firstbuy,
				collect_count_before_firstbuy,
				cart_count_before_firstbuy,
				cart_dic[key][0],
				cart_dic[key][1],
				cart_dic[key][2],
				cart_dic[key][3],
				user_and_item_dic[key][3],
				user_and_item_dic[key][0],
				user_and_item_dic[key][1],
				user_and_item_dic[key][2],				
				#least_click_day,
				#least_collect_day,
				#least_cart_day,
				#least_buy_day,
				user_and_item_last_3_day[key][0],
				user_and_item_last_3_day[key][3],
				user_and_item_last_3_day[key][1],
				user_and_item_last_3_day[key][2],
				user_and_item_last_7_day[key][0],
				user_and_item_last_7_day[key][3],
				user_and_item_last_7_day[key][1],
				user_and_item_last_7_day[key][2]))


#data(test,'test')
data(train,'train')
construct('train_user_and_item_feature.csv')
