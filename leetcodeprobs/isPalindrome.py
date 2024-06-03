class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        #instead of taking out the space and , i will choose to ignore it
        low=0 
        high=len(s)-1
        while low<high:
            # if s[low]==" " or s[low]== "," or s[low]==":":
            if s[low].isalnum()==False:
                low+=1
            # elif s[high]==" " or s[high]== "," or s[high]==":":
            elif s[high].isalnum() == False:
                high-=1
            elif s[low]!=s[high]:
                return False
            else:
                low+=1
                high-=1
        return True