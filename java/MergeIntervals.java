import java.util.Arrays;

/**
 * Q20. Merge Intervals (Category: Sliding Window / Misc)
 *
 * Problem: Given a collection of intervals, merge all overlapping intervals.
 *
 * Approach: Sort by start time. Iterate and merge the current interval into
 *           the last interval in the result if they overlap.
 *
 * Time Complexity : O(n log n)  — dominated by sorting
 * Space Complexity: O(n)        — output list
 */
public class MergeIntervals {

    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;

        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        int[][] result = new int[intervals.length][2];
        int idx = 0;
        result[idx] = intervals[0];

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] <= result[idx][1]) {
                // Overlapping — extend the end if needed
                result[idx][1] = Math.max(result[idx][1], intervals[i][1]);
            } else {
                result[++idx] = intervals[i];
            }
        }
        return Arrays.copyOf(result, idx + 1);
    }

    public static void main(String[] args) {
        MergeIntervals solution = new MergeIntervals();
        int[][] intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
        int[][] merged = solution.merge(intervals);
        System.out.println(Arrays.deepToString(merged)); // [[1, 6], [8, 10], [15, 18]]
    }
}
