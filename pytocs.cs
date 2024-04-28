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

public class Solution {
    public int LengthOfLastWord(string s) {
        int value = 0;
        int counter = 0;
        Console.WriteLine(s.Length);
        for (int i = 0; i < s.Length; i++) {
            if (s[i] == ' ') {
                if (counter >= 1) {
                    value = counter;
                }
                counter = 0;
            } else {
                counter += 1;
            }
        }
        return counter > 0 ? counter : value;
    }
}

public class Solution {
    public int ClimbStairs(int n) {
        if (n == 1) {
            return 1; 
        }
        if (n == 2) {
            return 2; 
        }
        int first = 1;
        int second = 2;
        int result = 0;
        for (int i = 3; i <= n; i++) {
            result = first + second;
            first = second; 
            second = result; 
        }
        return result;
    }
}
public class Solution {
    public int Search(int[] nums, int target) {
        int low=0;
        int high= nums.Length-1;
        int mid = (low+(high-low)/2);

        while(low<=high){
            if(nums[mid]==target){
                return mid;}
            if(target>= nums[low] && target<nums[mid]){
                high= mid-1;
                mid = (low+(high-low)/2);
            }else if (target<=nums[high] && target>nums[mid]){
                low = mid+1;
                mid = (low+(high-low)/2);
            } else{
                return -1;
            }
        } return mid;
    }
}