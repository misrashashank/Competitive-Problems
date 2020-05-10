'''
Given an array nums of n integers where n > 1, return an array output
such that output[i] is equal to the product of all the elements of nums
except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or
suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of
space complexity analysis.)
'''


'''
class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return []
        len_nums = len(nums)

        # Maintain arrays to store left and right flank multiplications
        left, right = [1] * len_nums, [1] * len_nums
        output = []

        # Update left array
        for index in range(1, len_nums):
            left[index] = left[index-1] * nums[index-1]

        for index in reversed(range(len_nums-1)):
            right[index] = right[index+1] * nums[index+1]

        # Create output array
        for index in range(len_nums):
            output.append(left[index] * right[index])

        return output
'''


# Better solution
# Method 2 - Time: O(n), Space: O(1)
class Solution:
    def productExceptSelf(self, nums):
        '''
        Array > Array
        
        [1,2,3,4] > [24, 12, 8, 6]
        [1,1,2,6]
        [1,1,1,1]
        Naive O(n^2) > for every element traverse the whole array
        
        Better:
        [2, 5, -6-, 8, 9]
        maintain left and right arrays - containing cascading products
        till the element
        Product of left and right arrays

        Space O(1) - Generate left array > Iterate in reverse on nums
        Maintain a variable to track product of right elements
        Multiply variable with left array elements
        '''

        if not nums:
            return []
        
        len_nums = len(nums)
        result = [1] * len_nums
        
        # Manipulate left products and save in result
        for index in range(len_nums - 1):
            result[index+1] = nums[index] * result[index]
        
        # Manipulate a variable to track right product
        right_prod = 1
        
        # Manipulate final results using right_prod
        for index in range(len_nums-1, -1, -1):
            result[index] *= right_prod
            right_prod *= nums[index]

        return result
