#1st - note & is a bit wise operator in py, and is the logical one
def isSubsequence(self, s: str, t: str) -> bool:
    replica=""
    left=0
    right=0
    if len(s)==0:
        return True
    while right< len(t) and left< len(s):
        if s[left]==t[right]:
            replica+=s[left]
            left+=1
            right+=1
        else:
            right+=1
    return True if replica==s else False