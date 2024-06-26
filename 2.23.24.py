from typing import List
'''Objective:
The goal of this task is to write a Python function that modifies a given string by swapping every other vowel found within it.
This operation should follow a specific pattern where the first vowel encountered is swapped with the second, the third with the fourth, and so on, throughout the entire string.
'''
def swap_vowels(s):
    left=0
    right=1
    vowels=['a','e','i','o','u','A','E','I','O','U']
    if len(s)==1:
        return s
    while left<right:
        print(s) 
        if left>=len(s):
            return s
        if right>=len(s):
            return s
        if s[left] not in vowels:
            left+=1
        if s[right] not in vowels:
            right+=1
        if left==right:
            right+=1
        
        if left>=len(s):
            return s
        if right>=len(s):
            return s
        
        if s[left] in vowels and s[right] in vowels:
            s= s[:left]+s[right]+s[left+1:right]+s[left]+s[right+1:]
            left=right+1
            right+=2
            print(s)
    print("Returning", s)   
    return s

 

# Test cases
# assert swap_vowels("hello") == "holle", "Test case failed: 'hello' -> 'holle'"
# assert swap_vowels("timemachine") == "temimichane", "Test case failed: 'timemachine' -> 'temimichane'"
# assert swap_vowels("a") == "a", "Test case failed: 'a' -> 'a'"
# assert swap_vowels("ae") == "ea", "Test case failed: 'ae' -> 'ea'"
# assert swap_vowels("b") == "b", "Test case failed: No vowels should result in no change."
# assert swap_vowels("AEIOU") == "AIEOU", "Test case failed: Uppercase vowel swap."
# assert swap_vowels("") == "", "Test case failed: Empty string."
# assert swap_vowels("bcdfg") == "bcdfg", "Test case failed: No vowels should result in no change."
# assert swap_vowels("Racecar") == "Recacar", "Test case failed: 'Racecar' -> 'Recacar'"

# print("All test cases passed.")
   
def binary_search(nums, target):
        low=0
        high=len(nums)-1
        mid= int(low+((high-low)/2))
        if len(nums)==0:
            return -1
        
        while low <= high:            
            if nums[mid] ==target:
                return mid
            if target >=nums[low] and target < nums[mid]:
                high=mid-1
                mid= int(low+((high-low)/2))
            elif target >nums[mid] and target<=nums[high]:
                low= mid+1
                mid= int(low+((high-low)/2))
            else:
                return -1
            
        return mid
        


# def test_b_search():
#     assert binary_search([-1,0,5], -1) == 0, "Test 8 Failed"

#     assert binary_search([1, 3, 5, 7], 4) == -1, "Test 8 Failed"

#     assert binary_search([2,5,8,12,16,23,38,56,72,91], 23) == 5, "Test 7 Failed"

#     # Test 7: Target Value Not Present in the List
#     assert binary_search([1, 2, 3, 4, 5], 6) == -1, "Test 7 Failed"

#     # Test 1: Search in a Small List
#     assert binary_search([1, 2, 3, 4, 5], 4) == 3, "Test 1 Failed"
    
#     # Test 2: Search in a Large List
#     assert binary_search(list(range(1, 10001)), 5000) == 4999, "Test 2 Failed"
    
#     # Test 3: Target Value at the Start of the List
#     assert binary_search([10, 20, 30, 40, 50], 10) == 0, "Test 3 Failed"
    
#     # Test 4: Target Value at the End of the List
#     assert binary_search([10, 20, 30, 40, 50], 50) == 4, "Test 4 Failed"
    
#     # Test 5: Single Element List
#     assert binary_search([100], 100) == 0, "Test 5 Failed"
    
#     # Test 6: Empty List
#     assert binary_search([], 10) == -1, "Test 6 Failed"
    
    
#     # Test 8: Target Value Between Elements
#     assert binary_search([1, 3, 5, 7], 4) == -1, "Test 8 Failed"
    
#     # Test 9: List with Duplicates
#     assert binary_search([1, 2, 2, 2, 3], 2) in [1, 2, 3], "Test 9 Failed"
    
#     # Test 10: Non-integer Elements
#     #assert binary_search(["apple", "banana", "cherry", "date"], "cherry") == 2, "Test 10 Failed"
    
#     # Optionally, Test 11: Very Large List - This test might be too intensive to run regularly
#     # assert binary_search(list(range(1, 10000001)), 5000000) == 4999999, "Test 11 Failed"
    
#     print("All tests passed!")

# # Uncomment the following line to run the tests
# test_b_search()

def binary_search_first_occurrence(nums, target):
        low=0
        high=len(nums)-1
        count = 0
        mid= int(low+((high-low)/2))
        for i in range (len(nums)):
            if nums[mid] == target:
                if mid ==len(nums)-1:
                    return mid+1 -count
                elif nums[mid]==nums[mid+1]:
                    mid+=1
                else:
                    return mid +1 - count
            elif target >= nums[low] and target<nums[mid]:
                high= mid-1
                mid= int(low+((high-low)/2))
            elif target > nums[mid] and target <= nums[high]:
                low= mid+1
                mid= int(low+((high-low)/2))
            else: 
                return -1
        return mid

def test_binary_search_first_occurrence():
    assert binary_search_first_occurrence([1, 2, 3, 4, 5], 6) == 4, "Test 3 Failed"
    # Test 3: First occurrence at the end
    assert binary_search_first_occurrence([1, 2, 3, 4, 5, 5], 5) == 4, "Test 3 Failed"

    # Test 1: First occurrence in the middle
    assert binary_search_first_occurrence([1, 2, 2, 4, 5], 2) == 1, "Test 1 Failed"

    # Test 2: First occurrence at the start
    assert binary_search_first_occurrence([2, 2, 3, 4, 5], 2) == 0, "Test 2 Failed"

    

    # Test 4: Target not present
    assert binary_search_first_occurrence([1, 2, 3, 4, 5], 6) == -1, "Test 4 Failed"

    # Test 5: Single occurrence
    assert binary_search_first_occurrence([1, 2, 3, 4, 5], 3) == 2, "Test 5 Failed"

    # Test 6: All elements are the target
    assert binary_search_first_occurrence([2, 2, 2, 2, 2], 2) == 0, "Test 6 Failed"

    # Test 7: Large list with duplicates
    assert binary_search_first_occurrence([1] * 50 + [2] * 50 + [3] * 50, 2) == 50, "Test 7 Failed"

    print("All tests passed!")

# Uncomment the following line to run the tests
test_binary_search_first_occurrence()
