# Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
# It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters 
# will occur the same number of times. Given a string s, determine if it is valid. 
# If so, return YES, otherwise return NO.

import collections

def sherlock_valid_string(s):
	dict_s = collections.Counter(s)
	print(dict_s)
	print(list(dict_s))
	print(list(dict_s.values()))

# 	max_s = max(dict_s.values())
# 	min_s = min(dict_s.values())
# 	diff = max_s - min_s
# 	if diff > 1:
# 		print("NO")
# 	elif diff == 0:
# 		print("YES")
# 	else:
# 		count = sum(value == max_s for value in dict_s.values())
# 		print("YES") if count == 1 else print("NO")

# sherlock_valid_string("aabbcd")
# sherlock_valid_string("aabbccddeefghi")
# sherlock_valid_string("abcdefghhgfedecba")

# s = "shashank"
# s = input().strip()
# print(s)
# freq = collections.Counter(s)
# values = list(freq.values())
# values.sort()
print('YES' if values.count(values[0]) == len(values) 
	or (values.count(values[0]) == len(values) - 1 and values[-1] - values[-2] == 1) 
	or (values.count(values[-1]) == len(values) - 1 and values[0] == 1) else 'NO')

