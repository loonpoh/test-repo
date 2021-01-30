print("my test program")

l1 = [3,4,6,7,1,2,9,1,4]

def func(list1):
	return list(map(lambda x: x**2,list1))

print(func(l1)) 

l2 = list(filter(lambda x: x%2 == 1, l1))
print('filter list : ', l2)

print('set of l1 +: ', set(l1))

class vehicle():
	def __init__(self,engine,speed,new):
		self.engine = engine
		self.speed = speed
		self.new   = new
	def high_speed_limit(self):
		return 200
	def low_speed_limit():
		return 40
	def is_new_car(self):
		print('new car: ', self.new)
		return self.new == True

class motorcar(vehicle):
	def __init__(self,engine,speed,new):
		self.engine = 'Average'
		self.speed = 60
		self.new = new
	def high_speed_limit(self):
		return 70
	def low_speed_limit(self):
		return 30
	def is_new_car(self):
		print('new motorcar: ',self.new)
		return self.new == True

mycar = vehicle('good',120,False)
print('my car engine is '+ mycar.engine)
print('my car speed is ', mycar.speed)
print('high speed limit: ', mycar.high_speed_limit())
print('my car is new or old ',mycar.new)
if mycar.is_new_car() == True:
	print('new car')
else:
	print('old car')

mymotorcar = motorcar('excellent',90,True)

print('my motorcar engine is '+ mymotorcar.engine)
print('my motocar speed is ', mymotorcar.speed)
print('high speed limit: ', mymotorcar.high_speed_limit())
print('my motocarcar is new or old ',mymotorcar.new)
if mymotorcar.is_new_car() == True:
	print('new motorcar')
else:
	print('old motorcar')

		