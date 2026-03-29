/*
 * Q20. Merge Intervals (Category: Sliding Window / Misc)
 *
 * Problem: Given a collection of intervals, merge all overlapping intervals.
 *
 * Approach: Sort by start time. Merge current interval into the last result
 *           interval if they overlap; otherwise append.
 *
 * Time Complexity : O(n log n)  — sorting dominates
 * Space Complexity: O(n)
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> result;

    for (auto& interval : intervals) {
        if (!result.empty() && interval[0] <= result.back()[1]) {
            result.back()[1] = max(result.back()[1], interval[1]);
        } else {
            result.push_back(interval);
        }
    }
    return result;
}

int main() {
    vector<vector<int>> intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    auto merged = merge(intervals);
    cout << "[";
    for (int i = 0; i < (int)merged.size(); i++) {
        cout << "[" << merged[i][0] << "," << merged[i][1] << "]";
        if (i + 1 < (int)merged.size()) cout << ", ";
    }
    cout << "]" << endl; // [[1,6], [8,10], [15,18]]
    return 0;
}
