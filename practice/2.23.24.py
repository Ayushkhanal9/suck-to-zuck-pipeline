'''Objective
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
assert swap_vowels("hello") == "holle", "Test case failed: 'hello' -> 'holle'"
assert swap_vowels("timemachine") == "temimichane", "Test case failed: 'timemachine' -> 'temimichane'"
assert swap_vowels("a") == "a", "Test case failed: 'a' -> 'a'"
assert swap_vowels("ae") == "ea", "Test case failed: 'ae' -> 'ea'"
assert swap_vowels("b") == "b", "Test case failed: No vowels should result in no change."
assert swap_vowels("AEIOU") == "EAOIU", "Test case failed: Uppercase vowel swap."
assert swap_vowels("") == "", "Test case failed: Empty string."
assert swap_vowels("bcdfg") == "bcdfg", "Test case failed: No vowels should result in no change."
assert swap_vowels("Racecar") == "Recacar", "Test case failed: 'Racecar' -> 'Recacar'"

print("All test cases passed.")
