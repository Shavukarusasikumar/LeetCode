class Solution {
public:
    int helper(string s,string t,int m,int n,vector<vector<int>>&dp){
        if(n==0){
            return 1;
        }
        if(m==0){
            return 0;
        }
        if(dp[m][n]!=-1){
            return dp[m][n];
        }
        if(s[m-1]==t[n-1]){
            return dp[m][n]=helper(s,t,m-1,n,dp)+helper(s,t,m-1,n-1,dp);
        }
        else{
            return dp[m][n]=helper(s,t,m-1,n,dp);
        }
    }
    int numDistinct(string s, string t) {
        int m=s.size();
        int n=t.size();
        vector<vector<int>>dp(m+1,vector<int>(n+1,-1));
        return helper(s,t,m,n,dp);
    }
};