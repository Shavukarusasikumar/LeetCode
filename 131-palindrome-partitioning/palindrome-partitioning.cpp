class Solution {
public:
    bool pal(string s,int st,int en){
    while(st<=en){
        if(s[st++]!=s[en--]){
            return false;
        }
    }
    return true;
}
void helper(string s,int ind,vector<string>&ds,vector<vector<string>>&ans){
    if(ind==s.size()){
        ans.push_back(ds);
        return;
    }
    for(int i=ind;i<s.size();i++){
        if(pal(s,ind,i)){
            ds.push_back(s.substr(ind,i-ind+1));
            helper(s,i+1,ds,ans);
            ds.pop_back();
        }
    }
}
    vector<vector<string>> partition(string s) {
        int ind=0;
        vector<string> ds;
        vector<vector<string>> ans;
        helper(s,ind,ds,ans);
        return ans;

    }
};