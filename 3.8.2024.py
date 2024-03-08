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