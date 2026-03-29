/*
 * Q18. Longest Subarray with Sum K (Category: Sliding Window / Misc)
 *
 * Problem: Find the length of the longest contiguous subarray with sum = k.
 *          (Array may contain negatives or zeros.)
 *
 * Approach: Prefix sum + unordered_map.
 *           If (prefixSum - k) has been seen before, we found a valid subarray.
 *           Store only the earliest index for each prefix sum.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(n)
 */
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int longestSubarrayWithSumK(vector<int>& nums, int k) {
    unordered_map<long, int> prefixSumIndex;
    prefixSumIndex[0] = -1;
    long prefixSum = 0;
    int maxLen = 0;

    for (int i = 0; i < (int)nums.size(); i++) {
        prefixSum += nums[i];
        if (prefixSumIndex.count(prefixSum - k)) {
            maxLen = max(maxLen, i - prefixSumIndex[prefixSum - k]);
        }
        if (!prefixSumIndex.count(prefixSum)) {
            prefixSumIndex[prefixSum] = i;
        }
    }
    return maxLen;
}

int main() {
    vector<int> nums1 = {1, -1, 5, -2, 3};
    cout << longestSubarrayWithSumK(nums1, 3) << endl; // 4

    vector<int> nums2 = {-2, -1, 2, 1};
    cout << longestSubarrayWithSumK(nums2, 1) << endl; // 2
    return 0;
}
