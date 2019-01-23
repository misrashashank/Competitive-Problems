# A string is said to be a child of a another string if it can be formed by deleting 
# 0 or more characters from the other string. Given two strings of equal length, 
# what's the longest string that can be constructed such that it is a child of both?


#Solution - Dynamic Programming
# If the last character of both the string match (s1[len(s1)-1] == s1[len(s1)-1]) then,
# OPT(s1[:len(s1)-1], s2[:len(s2)-1])
# Else if last characters don't match (s1[len(s1)-1] != s1[len(s1)-1]) then,
# Maximum of {OPT(s1[:len(s1)], s2[:len(s2)-1]), OPT(s1[:len(s1)-1], s2)}

def common_child(s1, s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1 == 0 or len2 == 0:
		return 0
	elif s1[len1-1] == s2[len2-1]:
		return 1 + common_child(s1[:len1-1], s2[:len2-1])
	else:
		return max(common_child(s1, s2[:len2-1]), common_child(s1[:len1-1], s2))

print(common_child("shinchan", "norahaaa"))
