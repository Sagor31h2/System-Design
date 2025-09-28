#Source https://blog.algomaster.io/p/rate-limiting-algorithms-explained-with-code
import time

class TokenBucket:
    def __init__(self, capacity, fill_rate):
        self.capacity=capacity
        self.fill_rate= fill_rate
        self.tokens=capacity
        self.last_time =time.time()
    
    def allow_request(self, tokens=1):
        now=time.time()
        time_passed=now -self.last_time
        self.tokens=min(self.capacity, self.tokens+self.fill_rate*time_passed)
        self.last_time=now

        if self.tokens>=tokens:
            self.tokens-=tokens
            return True
        return False

limiter=TokenBucket(10,1)

for i in range(100):
   print( limiter.allow_request())
   time.sleep(0.1)

