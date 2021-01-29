print("my test program")

l1 = [3,4,6,7,1,2,9]

def func(list1):
	return list(map(lambda x: x**2,list1))

print(func(l1)) 

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

mycar = vehicle('good',120,False)
print('my car engine is '+ mycar.engine)
print('my car speed is ', mycar.speed)
print('high speed limit: ', mycar.high_speed_limit())
print('my car is new or old ',mycar.new)
if mycar.is_new_car() == True:
	print('new car')
else:
	print('old car')

		