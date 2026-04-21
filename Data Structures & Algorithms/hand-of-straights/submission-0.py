class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 
        hand.sort()
        hash_map = Counter(hand)

        group = [0] * len(hand)

        for i in range(len(hand)):
            card = hand[i]
            if hash_map[card] > 0:
            # next_card = card + groupSize -1
                for next_card in range(card, card+ groupSize):
                    if hash_map[next_card] > 0:
                        hash_map[next_card]-=1
                    else:
                        return False
        return True 