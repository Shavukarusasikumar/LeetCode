class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string s="";
        sort(strs.begin(),strs.end());
        int n=strs.size();
        string s1=strs[0];
        string s2=strs[n-1];
        int n1=s2.size();
        for(int i=0;i<s1.size();i++){
            if(i>n1 ||s1[i]!=s2[i]) return s;
            s+=s1[i];
        }
        return s;
    }
};