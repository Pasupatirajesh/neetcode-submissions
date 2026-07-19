class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keymap = {}
        total_time, prev = 0,0
        for i, key in enumerate(keyboard):
            keymap[key] = i
        for char in word:
            total_time += abs(prev - keymap[char])
            prev = keymap[char]
            # total_time+=distance


        return total_time
