# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.
# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.
from typing import List

def numUniqueEmails(emails: List[str]) -> int:
    array=[]
    for i in range(len(emails)):
        parts=emails[i].split("@")
        before = parts[0]
        after= parts[1]
        if "." in before:
            before=before.replace(".","")
        if "+" in before:
            before = before.split("+")[0]
        temp= before+"@"+after
        if temp not in array:
            array.append(temp)
    return len(array)


#Given an array of positive integers nums and an integer k, find the length of the longest subarray
# whose sum is less than or equal to k.

def subarraySum(nums: List[int], k: int) -> int:
        left=0
        right=0
        curr=0
        for right in range(len(nums)):
            curr+=nums[right]
            if curr > k:
                curr-=nums[left]
                left+=1
            curr= max(curr,right-left+1)
        return curr

#1st implementation didnt work with [1,0,1,1,0,1] output was 1 when expected was 2:
#lets run through it. 
#l,r,c=0. - for 0 to 6(means not including 6 so 5)
#so we had set ip count =0 if nums[right]=0 so after the longest consecutive 1's it reset again
#after it saw a 0 again. we have to change it so it doesn't reset. We can save the value variable

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    left=right=count=0
    value=0
    for right in range(len(nums)):
        if nums[right]==0:
            value=max(value,count)
            left=right+1
            count=0
        else:
            count+=1
            
        value=max(value,count)
    return value 
            
#2nd implementation using sliding window as the last one we were just counting and there was no window

def findMaxConsecutiveOnes1(nums: List[int]) -> int:
    left=right=count=0
    value=0
    for right in range(len(nums)):
        if nums[right]==0:
            value=max(value,right-left)
            left=right+1  
        value=max(value,right-left+1)
    return value 
        

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array 
#if you can flip at most k 0's.
# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

def longestOnes(nums: List[int], k: int) -> int:
    left=right=zero_count=ans=0
    for right in range(len(nums)):
        if nums[right]==0:
            zero_count+=1
        while zero_count>k:
            if nums[left]==0:
                zero_count-=1
            left += 1
        ans=max(ans,right-left+1)
    return ans


# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some
# (can be none) of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
#s="abc" t="ajdjdbakac" = true
#s="abc".t= "axxcxxb"
def isSubsequence(s: str, t: str) -> bool:
    left=right=0
    strs=''
    if s is None:
        return True
    for right in range(len(t)):
            if left>=len(s):
                return True if strs==s else False
            if s[left]==t[right]:
                left+=1
                strs+=t[right]
    return True if strs==s else False


# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
# in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
def maxProfit(prices: List[int]) -> int:
    left=0
    profit=0
    value=0
    if len(prices)==0:
        return 0
    for right in range(1,len(prices)):
        profit= prices[right]-prices[left]
        if profit<=0:
            left=right
        value=max(value,profit)
    return value

