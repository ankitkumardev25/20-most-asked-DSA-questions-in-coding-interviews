/*
 * Q3. Move Zeros (Category: Arrays)
 *
 * Problem: Move all zeros to the end of the array in-place, maintaining
 *          the relative order of non-zero elements.
 *
 * Approach: Two-pointer. insertPos tracks where the next non-zero should go.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
#include <iostream>
#include <vector>
using namespace std;

void moveZeroes(vector<int>& nums) {
    int insertPos = 0;
    for (int num : nums) {
        if (num != 0) nums[insertPos++] = num;
    }
    while (insertPos < (int)nums.size()) {
        nums[insertPos++] = 0;
    }
}

int main() {
    vector<int> nums = {0, 1, 0, 3, 12};
    moveZeroes(nums);
    cout << "[";
    for (int i = 0; i < (int)nums.size(); i++) {
        cout << nums[i];
        if (i + 1 < (int)nums.size()) cout << ", ";
    }
    cout << "]" << endl; // [1, 3, 12, 0, 0]
    return 0;
}
