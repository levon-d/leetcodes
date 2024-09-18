class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            if not stack or (stack[-1] < 0) or (stack[-1] > 0 and asteroid > 0):
                stack.append(asteroid)
            else:
                current = asteroid
                while current:
                    if not stack or stack[-1] < 0 and current < 0:
                        stack.append(current)
                        current = None
                        break

                    if abs(current) > abs(stack[-1]) and stack[-1] > 0 and current < 0:
                        stack.pop()
                    elif (
                        abs(current) < abs(stack[-1]) and stack[-1] > 0 and current < 0
                    ):
                        current = None
                    else:
                        current = None
                        stack.pop()

        return stack
