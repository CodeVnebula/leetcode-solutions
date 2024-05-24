""" 
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        prev_step = 1
        curr_step = 1

        for i in range(2, n+1):
            num_ways = prev_step + curr_step
            prev_step, curr_step = curr_step, num_ways
    
    
        return curr_step
    