def maximum_toys(prices, k):
	prices.sort()
	count = 0
	for item in prices:
		if k != 0 and item <= k:
			k -= item
			count += 1
	print("Maximum number of toys: {}".format(count))


maximum_toys([1, 12, 5, 111, 200, 1000, 10], 50)