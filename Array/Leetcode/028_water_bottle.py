class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles 
        while empty >= numExchange :
            count = empty//numExchange
            extra = empty%numExchange
            empty = count + extra 
            total += count
        return total 