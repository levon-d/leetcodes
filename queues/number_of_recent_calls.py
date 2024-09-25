from collections import deque 
class RecentCounter:

    def __init__(self):
        self.count = 0 
        self.requests = deque([])
        

    def ping(self, t: int) -> int:
        while self.requests and self.requests[0] < t-3000:
            self.requests.popleft()
        self.requests.append(t)
        return len(self.requests)
