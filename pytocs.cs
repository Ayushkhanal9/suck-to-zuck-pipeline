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
public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        if(strs.Length==1 ){
            return strs[0];
        }
        string result= "";
        int min_str=strs[0].Length;
        for(int i=0; i<strs.Length;i++){
            if(strs[i].Length<min_str){
                min_str=strs[i].Length;
            }
        }
        for(int i=0; i<min_str;i++){
            char currentChar=strs[0][i];
            for(int j=0; j<strs.Length-1;j++){
                Console.WriteLine(strs[j][i]);
                if (strs[j][i]!=strs[j+1][i]){
                    return result; 
                }  
            // result+=strs[j][i];
            }result+=currentChar;
        }
        return result;
    }
}