/*
 * Q2. Maximum Subarray – Kadane's Algorithm (Category: Arrays)
 *
 * Problem: Find the contiguous subarray with the largest sum.
 *
 * Approach: Track currentSum. If it drops below the element itself, restart from that element.
 *           Update maxSum at every step.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxSubArray(vector<int>& nums) {
    int maxSum = nums[0];
    int currentSum = nums[0];

    for (int i = 1; i < (int)nums.size(); i++) {
        currentSum = max(nums[i], currentSum + nums[i]);
        maxSum = max(maxSum, currentSum);
    }
    return maxSum;
}

int main() {
    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << "Max Subarray Sum: " << maxSubArray(nums) << endl; // 6
    return 0;
}
