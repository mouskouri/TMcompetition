from csv import DictReader

train_user = 'train_deal.csv'  # path to training file
train_item = 'train_item.csv'  # path to testing file

user_geo_dic = {}

def cal_user_geo(path):
	count = 0

	for t, row in enumerate(DictReader(open(path))):
		count += 1
		if(row['user_id'] not in user_geo_dic):
			user_geo_dic[row['user_id']] = {}
		if(row['user_geohash'] not in user_geo_dic[row['user_id']]):
			user_geo_dic[row['user_id']][row['user_geohash']] = 0
		user_geo_dic[row['user_id']][row['user_geohash']] += 1

		if(count == 100):
			break
	userdic = sorted(user_geo_dic.items(), key = lambda d:d[1], reverse = True)
	return userdic


def build(user_geo_dic):

	with open('user_geo.csv', 'w') as usergeo:

		usergeo.write('user_id,user_geohash,count\n')
		for key in user_geo_dic:
			for geo in user_geo_dic[key]:
				usergeo.write('%s,%s,%s\n' % (key, geo, user_geo_dic[key][geo]))


userdic = cal_user_geo(train_user)

#build(user_geo_dic)
print userdic