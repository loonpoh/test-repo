print("my test program")

l1 = [3,4,6,7,1,2,9]

def func(list1):
	return list(map(lambda x: x**2,list1))

print(func(l1)) 