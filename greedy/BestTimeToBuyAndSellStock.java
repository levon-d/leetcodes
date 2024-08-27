class Solution {
    public int maxProfit(int[] prices) {
        int current = prices[0];
        int maxProfitMade = 0;

        for (int j=1; j<prices.length; j++) { 
            if (prices[j] > current) { 
                maxProfitMade = maxProfitMade + prices[j] - current;
            }
            current = prices[j];
        }    
        return maxProfitMade;
    }
}
