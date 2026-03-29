"""
Q20. Merge Intervals (Category: Sliding Window / Misc)

Problem: Given a collection of intervals, merge all overlapping intervals.

Approach: Sort by start time. For each interval, merge into the last result
          interval if they overlap; otherwise append a new interval.

Time Complexity : O(n log n)  — sorting dominates
Space Complexity: O(n)
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    result: list[list[int]] = []

    for start, end in intervals:
        if result and start <= result[-1][1]:
            # Merge: extend end of the last interval if needed
            result[-1] = [result[-1][0], max(result[-1][1], end)]
        else:
            result.append([start, end])

    return result


if __name__ == "__main__":
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
    print(merge([[1, 4], [4, 5]]))                      # [[1,5]]
