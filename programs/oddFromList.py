# Python program to print odd numbers in a List
def odd_num(list):
	for num in list:
		if num%2 != 0:
			print(num)


list1 = [10, 21, 4, 45, 66, 93]
odd_num(list1)