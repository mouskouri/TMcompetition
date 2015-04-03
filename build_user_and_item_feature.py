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

		if(Eid not in cart_dic):
			cart_dic[Eid] = [0,0,0,0]
		if(date == cart_time):
			cart_dic[Eid][int(row['behavior_type'])-1] += 1	
			
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

		user.write('user_id,item_id,last_day_click_count,last_day_collect_count,last_day_cart_count,last_day_buy_count,buy_count,click_count,collect_count,cart_count,last_3_day_click_count,last_3_day_buy_count,last_3_day_collect_count,last_3_day_cart_count,last_7_day_buy_count,last_7_day_collect_count,last_7_day_cart_count\n')
		for key in user_and_item_dic:
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
															
			user.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (user_id,item_id,
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
