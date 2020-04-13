'''
Suppose Andy and Doris want to choose a restaurant for dinner,
and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with
the least list index sum. If there is a choice tie between answers,
output all of them with no order requirement.
You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is
"Shogun" with index sum 1 (0+1).

Note:
1. The length of both lists will be in the range of [1, 1000].
2. The length of strings in both lists will be in the range of [1, 30].
3. The index is starting from 0 to the list length minus 1.
4. No duplicates in both lists.
'''


class Solution:
    def findRestaurant(self, list1, list2):
        # Method: Create a hash map of an array
        # Iterate over other array to find common indexes
        # Time: O(n)
        # Space: O(n)

        list1_map = {}
        for index in range(len(list1)):
            list1_map[list1[index]] = index

        min_index_sum = float('inf')
        result = []
        for index in range(len(list2)):
            if list2[index] in list1_map:
                index_sum = index + list1_map[list2[index]]
                if index_sum < min_index_sum:
                    result = [list2[index]]
                    min_index_sum = index_sum
                elif index_sum == min_index_sum:
                    result.append(list2[index])
        return result
