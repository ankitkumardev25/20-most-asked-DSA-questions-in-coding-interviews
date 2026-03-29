/*
 * Q4. Best Time to Buy and Sell Stock (Category: Arrays)
 *
 * Problem: Given daily stock prices, find the maximum profit from one transaction.
 *
 * Approach: Track the minimum price seen so far.
 *           Compute profit for each day and update the global maximum.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

int maxProfit(vector<int>& prices) {
    int minPrice = INT_MAX;
    int maxProfit = 0;

    for (int price : prices) {
        minPrice = min(minPrice, price);
        maxProfit = max(maxProfit, price - minPrice);
    }
    return maxProfit;
}

int main() {
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    cout << "Max Profit: " << maxProfit(prices) << endl; // 5
    return 0;
}
