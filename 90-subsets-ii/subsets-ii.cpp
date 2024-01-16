class Solution {
public:
    void fun(vector<int>&arr,vector<vector<int>>&ans,int ind,int n,vector<int>&ds){
        ans.push_back(ds);
        for(int i=ind;i<n;i++){
            if(i!=ind && arr[i]==arr[i-1]){
                continue;
            }
            ds.push_back(arr[i]);
            fun(arr,ans,i+1,n,ds);
            ds.pop_back();
            }
        }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> ds;
        int ind=0;
        int n=nums.size();
        sort(nums.begin(),nums.end());
        fun(nums,ans,ind,n,ds);
        return ans;
    }
};