#A string is good if there are no repeated characters.
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.

# think through
# Input: s = "aababcabc"
# Output: 4
# There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".

def countGoodSubstrings(s: str) -> int:
        left=right=0
        strs=""
        checker=""
        counter=0
        while right<=(len(s)-1):
            if len(strs)<=3:
                strs+=s[right]
                right+=1
                if len(strs)==3:
                    good=True
                    for i in range(len(strs)):
                        if strs[i] not in checker:
                            checker+=strs[i]
                        elif strs[i] in checker:
                            good=False
                    if good==True:counter+=1  
                    strs=""
                    checker="" 
                    left+=1
                    right=left
        return counter

#maximum subaray I
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# So given array [1,12,-5,-6,50,3] and k =4 we have 3 subarrays that we can make of length 4
# [1,12,-5,-6] will result in 2/4, [12,-5,-6,50] will result in 51/4, [-5,-6,50,3] = 42/4
# we return the highest number to solve this problem. Below is the implementation

def findMaxAverage(nums: List[int], k: int) -> float:
    left=right=0
    value=0
    summ=0
    if len(nums)==1:
        return nums[0]
    for right in range(len(nums)):
        if right - left +1 <= k:
            summ+=nums[right]
            if right-left+1==k:
                value=summ
        elif right-left +1 > k:
            summ-=nums[left]
            left+=1
            summ+=nums[right]
            value=max(value,summ)
    return value/k