class StringIterator:

    def __init__(self, compressedString: str):
        self.text = compressedString
        self.index = 0
        self.length = len(compressedString)
        self.current_char = ""
        self.remaining_count = 0

    def next(self) -> str:
        if not self.hasNext():
            return ''
        if self.remaining_count == 0:
            self.current_char = self.text[self.index]
            self.index+=1
     
            num_str = ""    
            while self.index < self.length and self.text[self.index].isdigit():
                num_str+=self.text[self.index]
                self.index+=1
            self.remaining_count = int(num_str)
        
        self.remaining_count-=1
        return self.current_char
    
        

    def hasNext(self) -> bool:
       return self.remaining_count > 0 or self.index < self.length
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
