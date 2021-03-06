'''
Write a function to check whether an input string is a valid
IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation,
which consists of four decimal numbers, each ranging from 0 to 255,
separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid.
For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits,
each group representing 16 bits.
The groups are separated by colons (":").
For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one.
Also, we could omit some leading zeros among four hexadecimal digits and
some low-case characters in the address to upper-case ones,
so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address
(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a
single empty group using two consecutive colons (::) to pursue simplicity.
For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid.
For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters
in the input string.

Example 1:
Input: "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
'''


class Solution:
    def validIPAddress(self, IP):
        '''
        String > String
        "2001:0db8:85a3:0:0:8A2E:0370:7334" > "IPv6"
        "254.254.254.254" > "IPv4"
        "256.256.256.256" > "Neither"
        "" > "Neither"
        
        Split string on . and : > Get number of parts > Return if not 4 or 8
        Check both symbols shouldn't be present
        IPv4 > Each part shouldn't start with 0 > Should be > -1 and < 256
        IPv4 > Only integers allowed
        IPv6 > Each part length > 0 and < 5
        IPv6 > Only alphanum allowed
        
        Time: O(n)
        Space: O(1)
        '''
        
        if len(IP) == 0:
            return "Neither"
        
        IPv4, IPv6 = False, False
        for item in IP:
            if item == ':':
                IPv6 = True
                break
            if item == '.':
                IPv4 = True
                break
            if not item.isalnum():
                return "Neither"
                
        if IPv4:
            IP_parts = IP.split(".")
            if len(IP_parts) != 4:
                return "Neither"
            
            for part in IP_parts:
                if len(part) == 0:
                    return "Neither"
                if part[0] == '0' and len(part) != 1:
                    return "Neither"
            
            for part in IP_parts:
                if not part.isnumeric() or int(part) > 255:
                    return "Neither"
            return "IPv4"
        
        if IPv6:
            IP_parts = IP.split(":")
            if len(IP_parts) != 8:
                return "Neither"
        
            for part in IP_parts:
                if len(part) == 0 or len(part) > 4:
                    return "Neither"
                
                for item in part:
                    if not item.isalnum():
                        return "Neither"
                    if item.isalpha():
                        if item not in 'abcdefABCDEF':
                            return "Neither"
            
            return "IPv6"
