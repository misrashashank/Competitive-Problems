#Bubble sort

def swap_custom(num1, num2, arr):
	ind1 = arr.index(num1)
	ind2 = arr.index(num2)
	temp = arr[ind1]
	arr[ind1] = arr[ind2]
	arr[ind2] = temp

def count_swaps(a):
	count = 0
	for _ in range(len(a)):
		for item in range(len(a)-1):
			if a[item] > a[item+1]:
				swap_custom(a[item], a[item+1], a)
				count += 1
	print("Array is sorted in {} swaps.".format(count))
	print("First Element: {}".format(a[0]))
	print("Last Element: {}".format(a[-1]))


count_swaps([6,4,1])