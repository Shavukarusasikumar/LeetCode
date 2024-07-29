class Solution {
public:
    int numTeams(vector<int>& rating) {
         int n = rating.size();
        int count = 0;

        // Generate all combinations of 3 elements
        for (int i = 0; i < n - 2; ++i) {
            for (int j = i + 1; j < n - 1; ++j) {
                for (int k = j + 1; k < n; ++k) {
                    // Check if the combination is strictly increasing or decreasing
                    if ((rating[i] < rating[j] && rating[j] < rating[k]) ||
                        (rating[i] > rating[j] && rating[j] > rating[k])) {
                        ++count;
                    }
                }
            }
        }

        return count;
        
    }
};