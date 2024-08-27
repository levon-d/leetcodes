class Solution {
    public int maxProfit(int[] prices) {
        int current = prices[0];
        int maxProfitMade = 0;

        for (int i=1; i<prices.length; i++) { 
            if (prices[i] > current) { 
                maxProfitMade = maxProfitMade + prices[i] - current;
            }
            current = prices[i];
        }    
        return maxProfitMade;
    }
}
