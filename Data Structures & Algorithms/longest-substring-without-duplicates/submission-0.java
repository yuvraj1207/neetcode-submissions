class Solution {
    public int lengthOfLongestSubstring(String s) {
      Map<Character , Integer> lSeen = new HashMap<>();
      int left = 0;
      int maxLength =0;

      for(int i = 0; i < s.length(); i ++){
        char ch = s.charAt(i);

        if(lSeen.containsKey(ch)){
            left = Math.max(left, lSeen.get(ch) +1);
        }
        lSeen.put(ch,i);
        maxLength = Math.max(maxLength, i - left +1);
      }  

        return maxLength;
    }
 }
