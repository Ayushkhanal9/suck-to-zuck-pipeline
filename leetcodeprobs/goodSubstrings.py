def countGoodSubstrings(self, s: str) -> int:
    left=0
    right =0
    seq=""
    goodSubStrings=[]
    while left<=right:
        if len(seq)==3:
            goodSubStrings.append(seq)
            seq=""
            left+=1
            right=left
        elif right>=len(s):
            return len(goodSubStrings)
        elif s[right] not in seq:
            seq+=s[right]
            right+=1
        else:
            seq=""
            left+=1
            right=left
    return len(goodSubStrings)