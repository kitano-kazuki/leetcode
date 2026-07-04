class Solution {
public:
    void sortColors(vector<int>& nums) {
      int zero_place_index = 0;
      int two_place_index = nums.size() - 1;
      int i = 0;
      while (i <= two_place_index){
        if (nums[i] == 1){
          i++;
          continue;
        }
        if (nums[i] == 0){
          swap(nums[i], nums[zero_place_index]);
          zero_place_index++;
          i++;
          continue;
        }
        if (nums[i] == 2){
          swap(nums[i], nums[two_place_index]);
          two_place_index--;
          continue;
        }
      }
    }
};
