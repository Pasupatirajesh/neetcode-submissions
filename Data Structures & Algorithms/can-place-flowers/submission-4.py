class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        extendbed = [0] + flowerbed + [0]
        countzeros = 0
        maxflowers = 0

        for i in range(len(extendbed)):
            if extendbed[i] == 0:
                countzeros+=1
            else:
                maxflowers += (countzeros-1)// 2
                countzeros = 0
        maxflowers+= (countzeros -1)//2
        return maxflowers >=n 

        