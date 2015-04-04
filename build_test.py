from csv import DictReader

test_path = 'test_user_item.csv'  # path to training file

user_feature = 'test_user_feature.csv'
item_feature = 'test_item_feature.csv'
user_and_item_feature = 'test_user_and_item_feature.csv'

user_feature_dic = {}
item_feature_dic = {}
user_and_item_feature_dic = {}
user_dic = {}
item_dic = {}
user_itemdic = {}

def build_user_and_item_dic(test_path):

	for t, row in enumerate(DictReader(open(test_path))):
		if(row['user_id'] not in user_dic):
			user_dic[row['user_id']] = 0

		if(row['item_id'] not in item_dic):
			item_dic[row['item_id']] = 0

		if(row['user_id'] not in user_itemdic):
			user_itemdic[row['user_id']] = {}

		if(row['item_id'] not in user_itemdic[row['user_id']]):
			user_itemdic[row['user_id']][row['item_id']] = 0



def build_user(user_feature):
	count = 0

	for t, row in enumerate(DictReader(open(user_feature))):
		#count += 1
		#if(row['user_id'] not in user_feature_dic):
			#user_feature_dic[row['user_id']] = {}
		if(row['user_id'] in user_dic):
			user_id = row['user_id']
			del row['user_id']
			user_feature_dic[user_id] = row

		#if(count == 10):
			#break

def build_item(item_feature):
	count = 0

	for t, row in enumerate(DictReader(open(item_feature))):
		#count += 1
		#if(row['item_id'] not in item_feature_dic):
			#item_feature_dic[row['item_id']] = {}
		if(row['item_id'] in item_dic):
			item_id = row['item_id']
			del row['item_id']
			item_feature_dic[item_id] = row
		#if(count == 10):
			#break
def build_user_and_item(user_and_item_feature):

	for t, row in enumerate(DictReader(open(user_and_item_feature))):
		if(row['user_id'] in user_itemdic):
			if(row['item_id'] in user_itemdic[row['user_id']]):
				Eid = []
				Eid.append(row['user_id'])
				Eid.append(row['item_id'])
				Eid = tuple(Eid)
				del row['user_id']
				del row['item_id']
				user_and_item_feature_dic[Eid] = row


def cal_least_buy_day_count(now, least):
	if(least == '0000'):
		return -30

	now = int(now[0:2])*30+int(now[2:])
	least = int(least[0:2])*30+int(least[2:])
	count = least-now
	return count
	

def build_test(test_path):

	with open('test_with_all_feature.csv', 'w') as test:
		test.write('user_id,item_id,item_category,user_click_day_count,user_collect_day_count,user_cart_day_count,user_buy_day_count,user_last_day_click_count,user_last_day_collect_count,user_last_day_cart_count,user_last_day_buy_count,user_buy_count,user_click_count,user_collect_count,user_cart_count,user_click_buy_rate,user_least_buy_day_count,user_last_7_day_click_count,user_last_7_day_buy_count,user_last_7_day_collect_count,user_last_7_day_cart_count,item_last_day_click_count,item_last_day_collect_count,item_last_day_cart_count,item_last_day_buy_count,item_buy_count,item_click_count,item_collect_count,item_cart_count,item_click_buy_rate,item_hot_level,item_least_buy_day_count,item_last_7_day_click_count,item_last_7_day_buy_count,item_last_7_day_collect_count,item_last_7_day_cart_count,click_day_count,collect_day_count,cart_day_count,buy_day_count,item_is_clicked_rate,item_is_collected_rate,item_is_carted_rate,item_is_bought_rate,buy_2_count,user_click_item_rate,user_collect_item_rate,user_cart_item_rate,user_buy_item_rate,click_count_before_firstbuy,collect_count_before_firstbuy,cart_count_before_firstbuy,last_day_click_count,last_day_collect_count,last_day_cart_count,last_day_buy_count,buy_count,click_count,collect_count,cart_count,last_3_day_click_count,last_3_day_buy_count,last_3_day_collect_count,last_3_day_cart_count,last_7_day_buy_count,last_7_day_collect_count,last_7_day_cart_count\n')
		
		for t, row in enumerate(DictReader(open(test_path))):

			Eid = []
			Eid.append(row['user_id'])
			Eid.append(row['item_id'])
			Eid = tuple(Eid)

			now_time = '1218'

			user_id = row['user_id']
			item_id = row['item_id']

			user_least_buy_time =user_feature_dic[user_id]['user_least_buy_day_count']
			user_least_buy_day_count = cal_least_buy_day_count(now_time, user_least_buy_time)

			item_least_buy_time = item_feature_dic[item_id]['item_least_buy_day_count']
			item_least_buy_day_count = cal_least_buy_day_count(now_time, item_least_buy_time)

			#least_click_day_time = user_and_item_feature_dic[Eid]['least_click_day_count']
			#least_click_day_count = cal_least_buy_day_count(now_time, least_click_day_time)

			#least_collect_day_time = user_and_item_feature_dic[Eid]['least_collect_day_count']
			#least_collect_day_count = cal_least_buy_day_count(now_time, least_collect_day_time)

			#least_cart_day_time = user_and_item_feature_dic[Eid]['least_cart_day_count']
			#least_cart_day_count = cal_least_buy_day_count(now_time, least_cart_day_time)

			#least_buy_day_time = user_and_item_feature_dic[Eid]['least_buy_day_count']
			#least_buy_day_count = cal_least_buy_day_count(now_time, least_buy_day_time)

			test.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (row['user_id'],row['item_id'],row['item_category'],
				user_feature_dic[user_id]['user_click_day_count'],
				user_feature_dic[user_id]['user_collect_day_count'],
				user_feature_dic[user_id]['user_cart_day_count'],
				user_feature_dic[user_id]['user_buy_day_count'],
				user_feature_dic[user_id]['user_last_day_click_count'],
				user_feature_dic[user_id]['user_last_day_collect_count'],
				user_feature_dic[user_id]['user_last_day_cart_count'],
				user_feature_dic[user_id]['user_last_day_buy_count'],
				user_feature_dic[user_id]['user_buy_count'],
				user_feature_dic[user_id]['user_click_count'],
				user_feature_dic[user_id]['user_collect_count'],
				user_feature_dic[user_id]['user_cart_count'],
				user_feature_dic[user_id]['user_click_buy_rate'],
				user_least_buy_day_count,
				user_feature_dic[user_id]['user_last_7_day_click_count'],
				user_feature_dic[user_id]['user_last_7_day_buy_count'],
				user_feature_dic[user_id]['user_last_7_day_collect_count'],
				user_feature_dic[user_id]['user_last_7_day_cart_count'],
				item_feature_dic[item_id]['item_last_day_click_count'],
				item_feature_dic[item_id]['item_last_day_collect_count'],
				item_feature_dic[item_id]['item_last_day_cart_count'],
				item_feature_dic[item_id]['item_last_day_buy_count'],
				item_feature_dic[item_id]['item_buy_count'],
				item_feature_dic[item_id]['item_click_count'],
				item_feature_dic[item_id]['item_collect_count'],
				item_feature_dic[item_id]['item_cart_count'],
				item_feature_dic[item_id]['item_click_buy_rate'],
				item_feature_dic[item_id]['item_hot_level'],
				item_least_buy_day_count,
				item_feature_dic[item_id]['item_last_7_day_click_count'],
				item_feature_dic[item_id]['item_last_7_day_buy_count'],
				item_feature_dic[item_id]['item_last_7_day_collect_count'],
				item_feature_dic[item_id]['item_last_7_day_cart_count'],
				user_and_item_feature_dic[Eid]['click_day_count'],
				user_and_item_feature_dic[Eid]['collect_day_count'],
				user_and_item_feature_dic[Eid]['cart_day_count'],
				user_and_item_feature_dic[Eid]['buy_day_count'],
				user_and_item_feature_dic[Eid]['item_is_clicked_rate'],
				user_and_item_feature_dic[Eid]['item_is_collected_rate'],
				user_and_item_feature_dic[Eid]['item_is_carted_rate'],
				user_and_item_feature_dic[Eid]['item_is_bought_rate'],
				user_and_item_feature_dic[Eid]['buy_2_count'],
				user_and_item_feature_dic[Eid]['user_click_item_rate'],
				user_and_item_feature_dic[Eid]['user_collect_item_rate'],
				user_and_item_feature_dic[Eid]['user_cart_item_rate'],
				user_and_item_feature_dic[Eid]['user_buy_item_rate'],
				user_and_item_feature_dic[Eid]['click_count_before_firstbuy'],
				user_and_item_feature_dic[Eid]['collect_count_before_firstbuy'],
				user_and_item_feature_dic[Eid]['cart_count_before_firstbuy'],
				user_and_item_feature_dic[Eid]['last_day_click_count'],
				user_and_item_feature_dic[Eid]['last_day_collect_count'],
				user_and_item_feature_dic[Eid]['last_day_cart_count'],
				user_and_item_feature_dic[Eid]['last_day_buy_count'],
				user_and_item_feature_dic[Eid]['buy_count'],
				user_and_item_feature_dic[Eid]['click_count'],
				user_and_item_feature_dic[Eid]['collect_count'],
				user_and_item_feature_dic[Eid]['cart_count'],				
				user_and_item_feature_dic[Eid]['last_3_day_click_count'],
				user_and_item_feature_dic[Eid]['last_3_day_buy_count'],
				user_and_item_feature_dic[Eid]['last_3_day_collect_count'],
				user_and_item_feature_dic[Eid]['last_3_day_cart_count'],
				user_and_item_feature_dic[Eid]['last_7_day_click_count'],
				user_and_item_feature_dic[Eid]['last_7_day_buy_count'],
				user_and_item_feature_dic[Eid]['last_7_day_collect_count'],
				user_and_item_feature_dic[Eid]['last_7_day_cart_count']))
				#user_and_item_feature_dic[Eid]['buy_count'],
				#user_and_item_feature_dic[Eid]['click_count'],
				#user_and_item_feature_dic[Eid]['collect_count'],
				#user_and_item_feature_dic[Eid]['cart_count'],
				#least_click_day_count,
				#least_collect_day_count,
				#least_cart_day_count,
				#least_buy_day_count,
				#user_and_item_feature_dic[Eid]['last_7_day_click_count'],
				#user_and_item_feature_dic[Eid]['last_7_day_buy_count'],
				#user_and_item_feature_dic[Eid]['last_7_day_collect_count'],
				#user_and_item_feature_dic[Eid]['last_7_day_cart_count']))

build_user_and_item_dic(test_path)

build_user(user_feature)

build_item(item_feature)

build_user_and_item(user_and_item_feature)

build_test(test_path)
