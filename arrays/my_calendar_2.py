class MyCalendarTwo:

    def __init__(self):
        self.single_bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.double_bookings:
            if not (end <= s or start >= e):
                return False 
        
        for s, e in self.single_bookings:
            if not (end <= s or start >= e):
                self.double_bookings.append((max(s,start), min(e,end)))
        
        self.single_bookings.append((start, end))
        
        return True 
