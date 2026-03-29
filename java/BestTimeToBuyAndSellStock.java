/**
 * Q4. Best Time to Buy and Sell Stock (Category: Arrays)
 *
 * Problem: Given an array of stock prices where prices[i] is the price on day i,
 *          find the maximum profit from one buy-sell transaction.
 *
 * Approach: Track the minimum price seen so far. For each day compute
 *           the potential profit and update the global maximum.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
public class BestTimeToBuyAndSellStock {

    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }
        return maxProfit;
    }

    public static void main(String[] args) {
        BestTimeToBuyAndSellStock solution = new BestTimeToBuyAndSellStock();
        int[] prices = {7, 1, 5, 3, 6, 4};
        System.out.println("Max Profit: " + solution.maxProfit(prices)); // 5
    }
}
