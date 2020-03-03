'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number
and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''


class Solution:
    def fizzBuzz(self, n):
        '''
        # Trivial approach. But, get complicated with multiple divisors.
        result = []
        for index in range(1, n+1):
            div_3 = index % 3
            div_5 = index % 5
            if div_3 == 0 and div_5 == 0:
                result.append('FizzBuzz')
            elif div_3 == 0:
                result.append('Fizz')
            elif div_5 == 0:
                result.append('Buzz')
            else:
                result.append(str(index))
        return result
        '''

        # Efficient approach (with same complexity)
        result = []
        for index in range(1, n+1):
            entry = ""
            divisors = {
                3: 'Fizz',
                5: 'Buzz'
            }
            for key in divisors:
                if index % key == 0:
                    entry += divisors[key]
            if not entry:
                entry = str(index)
            result.append(entry)
        return result
