class StringIterator:

    def __init__(self, compressedString: str):
        self.text = compressedString
        self.length = len(compressedString)
        self.index = 0
        self.count_remaining = 0
        self.char_remaining = ''

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.count_remaining == 0:
            self.char_remaining = self.text[self.index]
            self.index+=1

            num_str = ''
            while self.index < self.length and self.text[self.index].isdigit():
                num_str += self.text[self.index]
                self.index+=1
            self.count_remaining = int(num_str)
        self.count_remaining -=1
        return self.char_remaining

        

    def hasNext(self) -> bool:
        return self.index < self.length or self.count_remaining !=0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
