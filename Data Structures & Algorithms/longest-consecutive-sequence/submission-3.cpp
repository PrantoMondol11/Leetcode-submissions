class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }
        set<int>st;
        for(auto &it:nums){
            st.insert(it);
        }
        vector<int>v;
        for(auto it:st){
            v.push_back(it);
        }
         
        int cnt = 0,i;
        int maxi = 0;
        for( i = 0;i < v.size();i++){
            if(v[i + 1] - v[i] != 1){
               cnt++;
               maxi = max(maxi,cnt);
               cnt = 0; 
            }
            else{
                cnt++;
            }
        }
        return maxi;
    }
};
