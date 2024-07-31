'''
Nayeel Imtiaz
backtrack.py

7-30-24
'''
from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    memo = {}

    l = [0 for index in range(len(nums))]
    def backtrack(i):
        print(l)
        
        for index in range(i+1, len(nums)):
            l[index] = 1
            backtrack(index)
            l[index] = 0
            backtrack(index)
    backtrack(-1)

def main():
    lengthOfLIS([1,2,3])
    # print('hi')


if __name__ == '__main__':
    main()