/*
 * Q1. Two Sum (Category: Arrays)
 *
 * Problem: Given an array of integers nums and an integer target,
 *          return indices of the two numbers such that they add up to target.
 *
 * Approach: Use an unordered_map to store element -> index.
 *           For each element, check if (target - element) exists in the map.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(n)
 */
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> map; // value -> index
    for (int i = 0; i < (int)nums.size(); i++) {
        int complement = target - nums[i];
        if (map.count(complement)) {
            return {map[complement], i};
        }
        map[nums[i]] = i;
    }
    return {};
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = twoSum(nums, target);
    cout << "Indices: [" << result[0] << ", " << result[1] << "]" << endl; // [0, 1]
    return 0;
}
