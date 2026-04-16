class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int ndx1, ndx2;
        vector<int> solution(2);
        for (ndx1=0; ndx1<nums.size()-1; ndx1++) {
            for (ndx2=ndx1+1; ndx2<nums.size(); ndx2++)
                if (nums[ndx1]+nums[ndx2]==target) {
                    solution[0]=ndx1;
                    solution[1]=ndx2;
                    return solution;
                }
        }
    }
};
