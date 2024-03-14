
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith 
# digit of the integer. The digits are ordered from most significant to least significant in left-to-right 
# order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]

# Input: digits = [9]
# Output: [1,0]

def plusOne(digits: List[int]) -> List[int]:
        right = len(digits)-1
        remainder=1
        for i in range(right,-1,-1):
            if digits[i]==9 and remainder==1:
                digits[i]=0
            else:
                digits[i]+=1
                remainder=0
                break
        if remainder==1:
            digits.insert(0,1)
        return digits