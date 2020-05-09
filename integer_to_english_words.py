'''
Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 231 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
Thousand Eight Hundred Ninety 
'''


class Solution:
    def numberToWords(self, num: int) -> str:
        '''
        Integer > String
        1234567 > "One Million Two Hundred Thirty Four Thousand
        Five Hundred Sixty Seven"
        0 > "Zero"
        No negatives
        
        Break in sets of 3 starting from units place
        Every set of 3 will have its formation
        Add thousands, millions, billions
        
        Time: O(n)
        Space: O(n)
        '''
        
        # Get all digits
        digits = list(str(num))
        batches = []
        while(True):
            if len(digits) > 2:
                batches.append(digits[-3:])
                digits = digits[:-3]
            elif len(digits) > 0:
                batches.append(digits)
                break
            else:
                break
        batches = batches[::-1]
        print(batches)

        # Create digits mapping
        digits_map = {
            '0': ["", ""],
            '1': ["One ", ""],
            '2': ["Two ", "Twenty "],
            '3': ["Three ", "Thirty "],
            '4': ["Four ", "Forty "],
            '5': ["Five ", "Fifty "],
            '6': ["Six ", "Sixty "],
            '7': ["Seven ", "Seventy "],
            '8': ["Eight ", "Eighty "],
            '9': ["Nine ", "Ninety "]
        }
        # Mapping for 1 at Tens place
        ones_map = {
            '0': "Ten ",
            '1': "Eleven ",
            '2': "Twelve ",
            '3': "Thirteen ",
            '4': "Fourteen ",
            '5': "Fifteen ",
            '6': "Sixteen ",
            '7': "Seventeen ",
            '8': "Eighteen ",
            '9': "Nineteen "
        }
        
        # Mapping to specify Hundreds, Thousands, etc.
        batch_mapping = {
            1: "",
            2: "Thousand ",
            3: "Million ",
            4: "Billion "
        }
        
        result = ""
        if len(batches) == 1 and batches[0][0] == "0":
            return "Zero"

        for index in range(len(batches)):
            # Check if all the digits are zero in the batch
            all_zero = False
            if sum(map(int, batches[index])) == 0:
                all_zero = True

            if len(batches[index]) == 3:
                # 0th index
                result += digits_map[batches[index][0]][0]
                if batches[index][0] != '0':
                    result += "Hundred "

                # 1th and 2nd index
                # Check if 1 is at Tens place
                if batches[index][1] != '1':
                    result += digits_map[batches[index][1]][1]
                    result += digits_map[batches[index][2]][0]
                else:
                    result += ones_map[batches[index][2]]

            elif len(batches[index]) == 2:
                # 0th and 1st index
                # Check if 1 is at Tens place
                if batches[index][0] != '1':
                    result += digits_map[batches[index][0]][1]
                    result += digits_map[batches[index][1]][0]
                else:
                    result += ones_map[batches[index][1]]
                    
            else:
                result += digits_map[batches[index][0]][0]

            # Check batch for Hundreds, Millions, etc.
            if not all_zero:
                result += batch_mapping[len(batches) - index]
            
        result = result[:-1]
        return result
