import random
r = random.randint(1, 100)
count = 0
while True:
	num = input('enter a number(from 1 to 100):')
	num = int(num)
	if num == r:
		print('you are correct!')
		break
	elif num > r:
		print('the answer is smaller')
	elif num < r:
		print('the answer is biger')