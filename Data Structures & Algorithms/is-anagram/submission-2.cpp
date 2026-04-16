class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;
 /*       if (s.length()==0)
            return true;
        bool found=false;
        for (int i=0; i<s.length(); i++) {
            found=false;
            for (int j=0; j<t.length(); j++) {
                if (s[i]==t[j]) {
                  t[j]=' ';
                  found=true;
                  break;
                }              
            }
            if (found==false)
                return false;
        }
        return true;*/
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        return s==t;
    }
};
