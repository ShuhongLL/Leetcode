#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> temp;
    vector<int> sortArray(vector<int>& nums) {
        temp = nums;
        mergeSort(nums, 0, nums.size()-1);
        return nums;
    }
    
    void mergeSort(vector<int> &nums, int l, int r) {
        if (l >= r) return;
        int mid = (l + r) >> 1;
        mergeSort(nums, l, mid), mergeSort(nums, mid+1, r);
        int k = 0, i = l, j = mid+1;
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j]) temp[k++] = nums[i++];
            else    temp[k++] = nums[j++];
        }
        while (i <= mid)    temp[k++] = nums[i++];
        while (j <= r)  temp[k++] = nums[j++];
        // copy back
        for (k = 0, i = l; i <= r; i++, k++)    nums[i] = temp[k];
    }
};
