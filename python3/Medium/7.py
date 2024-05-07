"""
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes 
    the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:
    def reverse(self, x: int) -> int:
        reversed_int = 0
        if x >= 0:
            reversed_int = int(str(x)[::-1])
        else:
            reversed_int = int(str(x)[1:][::-1]) * -1
            
        if reversed_int > 2 ** 31 - 1 or reversed_int < -2 ** 31:
            return 0
        
        return reversed_int
