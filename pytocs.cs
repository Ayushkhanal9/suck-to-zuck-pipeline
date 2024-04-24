public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var mappy = new Dictionary<int,int>();
        for(int i=0;i<nums.Length;i++){
            int remainder = target - nums[i];
            if ((mappy.ContainsKey(remainder))){
                return new int[]{mappy[remainder],i};
            }
            mappy[nums[i]]=i;
        }
        return[-1,-1];
    }
}

public class Solution {
    public bool IsPalindrome(int x) {
        string s= x.ToString();
        int length= s.Length-1;
        for(int i=0; i<s.Length; i++){
            if (s[i]==s[length]){
                length-=1;
            }
            else{return false;}
        }
        return true;
    }
}