class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        # count the cards
        hash_map = {}
        for i in range(len(hand)):
            hash_map[hand[i]] = 1 + hash_map.get(hand[i], 0)
        

        for i in range(len(hand)):
            card = hand[i]
            if hash_map[card] > 0:
                for next_card in range(card, card+groupSize):
                    if hash_map.get(next_card, 0) == 0:
                        return False
                    hash_map[next_card] -= 1
                    
                        
        return True
