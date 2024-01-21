class Solution {
public:
    int helper(int n,vector<int>&dp){
        if(n<2){
            return n;
        }
        if(dp[n]!=-1){
            return dp[n];
        }
        return dp[n]=helper(n-1,dp)+helper(n-2,dp);
    }
    int climbStairs(int n) {
        vector<int> dp(n+2,-1);
        return helper(n+1,dp);
    }
};