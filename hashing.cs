public class Solution {
    public bool CheckIfPangram(string sentence) {
        HashSet<char> letters= new HashSet<char>("abcdefghijklmnopqrstuvwxyz");
        for(int i=0;i<sentence.Length;i++){
            if(letters.Contains(sentence[i])){
                letters.Remove(sentence[i]);
            } 

        }
            if(letters.Count==0){
                return true;
            }else{return false;}
    }
}
public class Solution {
    public int MissingNumber(int[] nums) {
        Array.Sort(nums); // Sort the array of integers
        int maxNum=nums.Length;
        for(int i=0;i<maxNum;i++){
            if(i!=nums[i]){
                return i;
            }
        }return maxNum;
    }
}