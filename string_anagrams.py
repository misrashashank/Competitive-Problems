# Given two strings, a and b, that may or may not be of the same length,
# determine the minimum number of character deletions required to make a and b anagrams.
# Any characters can be deleted from either of the strings.

def make_anagram(a, b):
    dict_a = {}
    dict_b = {}
    count = 0
    for char in a:
        keys = dict_a.keys()
        if char in keys:
            dict_a[char] += 1
        else:
            dict_a[char] = 1
    for char in b:
        keys = dict_b.keys()
        if char in keys:
            dict_b[char] += 1
        else:
            dict_b[char] = 1

    for item in dict_a.keys():
        if item in dict_b.keys():
            count += abs(dict_a[item] - dict_b[item])
        else:
            count += dict_a[item]

    for item in dict_b.keys():
        if item not in dict_a.keys():
            count += dict_b[item]
    return count


print(make_anagram("human", "chef"))

