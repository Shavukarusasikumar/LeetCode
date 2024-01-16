class Solution {
public:
    void helper(vector<int>&arr,vector<vector<int>>&ans,int freq[],vector<int>&ds){
        if(ds.size()==arr.size()){
            ans.push_back(ds);
            return;
        }
        for(int i=0;i<arr.size();i++){
            if(freq[i]==0){
                ds.push_back(arr[i]);
                freq[i]=1;
                helper(arr,ans,freq,ds);
                ds.pop_back();
                freq[i]=0;
            }

        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> ds;
        int n=nums.size();
        int freq[n];
        for(int i=0;i<n;i++){
            freq[i]=0;
        }
        helper(nums,ans,freq,ds);
        return ans;
    }
};