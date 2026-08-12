class Logger:

    def __init__(self):
        self.mhash = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message not in self.mhash:
            self.mhash[message] = timestamp
            return True
        
        if timestamp - self.mhash.get(message) >= 10:
            self.mhash[message] = timestamp
            return True
        else:
            return False
        
        
        
       

       
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
