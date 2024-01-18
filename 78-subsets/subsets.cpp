class Solution {
public:
    void fun(vector<int>&arr,vector<int>&ds, vector<vector<int>>&ans,int ind){
        if(ind==arr.size()){
            ans.push_back(ds);
            return;
        }
        ds.push_back(arr[ind]);
        fun(arr,ds,ans,ind+1);
        ds.pop_back();
        fun(arr,ds,ans,ind+1);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> ds;
        int ind=0;
        fun(nums,ds,ans,ind);
        return ans;   
    }
};