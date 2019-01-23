# You are given a string containing characters A and B only. Your task is to
# change it into a string such that there are no matching adjacent characters. 
# To do this, you are allowed to delete zero or more characters in the string.
# Your task is to find the minimum number of required deletions.

def alternating_characters(s):
	count = 0
	for index in range(len(s) - 1):
		if s[index] == s[index+1]:
			count += 1
	print("Minimum number of deletions".format(count))

alternating_characters("aaabbb")