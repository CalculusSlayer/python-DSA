from typing import List, Tuple, Dict

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo: Dict[Tuple[int, bool], int] = {}
        
        def backtrack(i: int, prev: bool) -> int:
            if i >= len(nums):
                return 0
            
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            if prev:
                # If the previous house was robbed, we cannot rob the current house
                result = backtrack(i + 1, False)
            else:
                # We have two choices: rob the current house or skip it
                rob_current = nums[i] + backtrack(i + 1, True)
                skip_current = backtrack(i + 1, False)
                result = max(rob_current, skip_current)
            
            memo[(i, prev)] = result
            return result
        
        return backtrack(0, False)

def main():
    s = Solution()
    print(s.rob([1,2,3,1]))

if __name__ == '__main__':
    main()