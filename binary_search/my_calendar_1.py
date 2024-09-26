class MyCalendar:

    def __init__(self):
        self.bookings = []

    def search(self, start):
        l = 0
        r = len(self.bookings) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.bookings[mid][0] == start:
                return mid + 1

            elif self.bookings[mid][0] < start:
                l = mid + 1
            else:
                r = mid - 1

        return l

    def book(self, start: int, end: int) -> bool:
        if not self.bookings:
            self.bookings.append((start, end))
            return True

        insertion_index = self.search(start)

        previous_start, previous_end = None, None
        next_start, next_end = None, None
        if insertion_index > 0:
            previous_start, previous_end = self.bookings[insertion_index - 1]

        if insertion_index < len(self.bookings):
            next_start, next_end = self.bookings[insertion_index]

        if (previous_end and previous_end > start) or (next_start and next_start < end):
            return False

        self.bookings = (
            self.bookings[:insertion_index]
            + [(start, end)]
            + self.bookings[insertion_index:]
        )
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
