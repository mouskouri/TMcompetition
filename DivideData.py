from csv import DictReader
import matplotlib.pyplot as plt

train = 'train_user.csv'  # path to training file
test = 'train_item.csv'  # path to testing file

user_dic = {}
user_list = []

def data(path):
	count = 0

	for t, row in enumerate(DictReader(open(path))):
		#date = row['time'].split()
		#date[0] = date[0][5:]
		#time = '-'.join(date)   #time = 11-26-20
		#row['time'] = time



		#x=[]
		#Eid = [row['user_id'], row['item_id']]
		#x.append(Eid)
		#key = ['user_id','item_id','behavior_type','user_geohash','item_category','time']
		#for index in key:
			#value = row[index]
			#x.append(value)
		#print x
		#yield t, time, x
		#break

		if row['user_id'] not in user_dic:
			count += 1
			behave = [0,0,0,0]
			user_dic[row['user_id']] = behave

		behave[int(row['behavior_type'])-1] += 1
		
		#user_list.append(user_dic[row['user_id']])

		#if (count == 100):
			#break

	print count





#splitime = '12-18-00'

#train_label = {}

#for t, time, x in data(train):
	#count = 0

	#if x[0] not in user_dic:
		#behave = [0,0,0,0]
		#user_dic[x[0]] = behave

	#behave[int(x[2])-1] += 1 




	#if (time < splitime):
		#if x[0] not in train_data:
			#train_data


data(train)

for key in user_dic:
	user_list.append(user_dic[key])
#print user_dic
#print user_list
#print len(user_list)
print len(user_dic)

#plot
user = [i for i in range(len(user_list))]
clicks = [x[0] for x in user_list]
buy = [x[3] for x in user_list]
conserve = [x[1] for x in user_list]
add = [x[2] for x in user_list]

plt.figure(1)
plt.figure(2)
plt.figure(3)

plt.figure(1)
plt.plot(user, clicks, 'b*')
plt.plot(user,clicks, 'r')

plt.plot(user, buy, 'r*')
plt.plot(user,buy, 'b')
plt.ylim(0,500)
plt.title('clicks and buy')


plt.figure(2)
plt.plot(user, conserve, 'b*')
plt.plot(user,conserve, 'r')

plt.plot(user, buy, 'r*')
plt.plot(user,buy, 'b')
plt.ylim(0,50)
plt.title('conserve and buy')

plt.figure(3)
plt.plot(user, add, 'b*')
plt.plot(user,add, 'r')

plt.plot(user, buy, 'r*')
plt.plot(user,buy, 'b')
plt.ylim(0,50)
plt.title('add and buy')
plt.show()



