class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        countgap = 0
        maxflowers = 0
        # if len(flowerbed) < n:
        #     return False
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                countgap+=1
            if flowerbed[i] == 1:
                if i == countgap:
                    maxflowers += countgap // 2
                else:
                    maxflowers += (countgap - 1) // 2
                countgap = 0
        if countgap == len(flowerbed):
            maxflowers += (countgap + 1) // 2
        else:
            maxflowers += countgap // 2
        return maxflowers >= n