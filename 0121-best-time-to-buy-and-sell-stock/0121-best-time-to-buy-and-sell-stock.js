/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxProfit = 0
    let minPrice = Number.MAX_VALUE
    n = prices.length
    for(let i =0;i<n;i++){
        minPrice = Math.min(minPrice,prices[i])
        maxProfit = Math.max(maxProfit,prices[i]-minPrice)
  }
    return maxProfit
};