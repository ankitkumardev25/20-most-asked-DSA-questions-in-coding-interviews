/*
 * Q19. Subarray Sum Equals K (Category: Sliding Window / Misc)
 *
 * Problem: Return the total number of subarrays whose sum equals k.
 *
 * Approach: Prefix sum + frequency map.
 *           For each index, count how many previous prefix sums equal (prefixSum - k).
 *
 * Time Complexity : O(n)
 * Space Complexity: O(n)
 */
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int subarraySum(vector<int>& nums, int k) {
    unordered_map<int, int> prefixCount;
    prefixCount[0] = 1;
    int prefixSum = 0, count = 0;

    for (int num : nums) {
        prefixSum += num;
        count += prefixCount[prefixSum - k];
        prefixCount[prefixSum]++;
    }
    return count;
}

int main() {
    vector<int> nums1 = {1, 1, 1};
    cout << subarraySum(nums1, 2) << endl; // 2

    vector<int> nums2 = {1, 2, 3};
    cout << subarraySum(nums2, 3) << endl; // 2
    return 0;
}
