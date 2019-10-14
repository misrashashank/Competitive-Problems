'''
Given array ip = [1,2,3,2,1]
Property 1 - Degree of an array - It is the highest occurrence of any element in the array.
Property 2 - Optimal sub-array - It is the minimum length sub-array of the original array which has the same degree.
Output the length of the optimal sub-array.

Example:

Input: [1, 2, 3, 1, 4, 2]
Output: 4

Explanation: Degree of the input array is 2 as the maximum occurrence of any element is 2.
Sub-array with same degree could be formed as [1, 2, 3, 1] and [2, 3, 1, 4, 2]
Minimum length sub-array is [1, 2, 3, 1] with length as 4.
'''


def min_sub_array(ip):
	d_items = {}
	for item in ip:
		if item in d_items.keys():
			d_items[item] += 1
		else:
			d_items[item] = 1

	max_value = 0
	for value in d_items.values():
		if value > max_value:
			max_value = value

	print(max_value)

	target_items = []
	for item in d_items.keys():
		if d_items[item] == max_value:
			target_items.append(item)
	print(target_items)

	min_range = len(ip)
	for item in target_items:
		l = ip.index(item)
		rev_ip = ip[::-1]
		r_mid = ip.index(item)
		r = len(ip) - r_mid - 1
		new_range = r - l+ 1
		if new_range < min_range:
			min_range = new_range
	print(min_range)
	return min_range

ip = [1,2,3,4,2,1,1,2]
min_sub_array(ip)