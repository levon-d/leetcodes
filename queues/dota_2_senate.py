from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        if len(senate) == 1:
            return "Radiant" if senate[0] == "R" else "Dire"

        opposites = {"R": "D", "D": "R"}

        names = {
            "R": "Radiant",
            "D": "Dire",
        }

        queue = deque([])
        while senate:
            newSenate = []

            if len(set(senate)) == 1:
                return names[senate[0]]

            for i in range(len(senate)):
                if not queue or senate[i] != queue[0]:
                    queue.append(opposites[senate[i]])
                    newSenate.append(senate[i])
                else:
                    queue.popleft()

            senate = newSenate
