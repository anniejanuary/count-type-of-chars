# Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string.
# Note: There are no white spaces in the string.
# 
# Example 1:
# 
# Input:
# S = "#GeeKs01fOr@gEEks07"
# Output:
# 5
# 8
# 4
# 2
# Explanation: There are 5 uppercase characters,
# 8 lowercase characters, 4 numeric characters
# and 2 special characters.

class Solution:
    def count (self,s): # why 'self'?
        result = [0 for i in range(4)] # how does it get printed/returned each in a new line?
        
        for i in s:
            if i >= 'A' and i <= 'Z':
                result[0] += 1
            elif i >= 'a' and i <= 'z':
                result[1] += 1
            elif i >= '0' and i <= '9':
                result[2] += 1
            else:
                result[3] += 1
        
        return result
        
