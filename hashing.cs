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