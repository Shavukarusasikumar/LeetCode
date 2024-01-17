class Solution {
public:
    void helper(vector<int>&arr,vector<int>&ds,int ind,int n,int t,vector<vector<int>>&ans){
        if(ind==n){
        if(t==0){
            ans.push_back(ds);
        }
        return;
        }
        if(arr[ind]<=t){
            ds.push_back(arr[ind]);
            helper(arr,ds,ind,n,t-arr[ind],ans);
            ds.pop_back();
        }
        helper(arr,ds,ind+1,n,t,ans);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> ds;
        int ind=0;
        int n=candidates.size();
        helper(candidates,ds,ind,n,target,ans);
        return ans;
    }
};