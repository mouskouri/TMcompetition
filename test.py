from csv import DictReader

train = 'train_user.csv'  # path to training file
user_behave = {}

def data(path):

	for t, row in enumerate(DictReader(open(path))):
		if(row['user_id'] == '9424202' and (row['behavior_type'] == '4')):
			if(row['user_id'] not in user_behave):
				user_behave[row['user_id']] = []
			user_behave[row['user_id']].append(row['time'])
			

data(train)
print user_behave