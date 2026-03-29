/*
 * Q5. Find the Duplicate Number (Category: Arrays)
 *
 * Problem: Given an array of n+1 integers in [1, n], find the duplicate.
 *          Do not modify the array; use O(1) extra space.
 *
 * Approach: Floyd's cycle detection — treat array values as linked-list "next" pointers.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
#include <iostream>
#include <vector>
using namespace std;

int findDuplicate(vector<int>& nums) {
    // Phase 1: find intersection inside the cycle
    int slow = nums[0];
    int fast = nums[0];
    do {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (slow != fast);

    // Phase 2: find cycle entrance (the duplicate)
    slow = nums[0];
    while (slow != fast) {
        slow = nums[slow];
        fast = nums[fast];
    }
    return slow;
}

int main() {
    vector<int> nums = {1, 3, 4, 2, 2};
    cout << "Duplicate: " << findDuplicate(nums) << endl; // 2
    return 0;
}
