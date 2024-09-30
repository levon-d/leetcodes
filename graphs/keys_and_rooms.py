class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        result = [False] * len(rooms)

        def dfs(current_room, rooms): 
            if result[current_room]:
                return
                
            result[current_room] = True
            current_keys = rooms[current_room]

            if not current_keys:
                return

            for key in current_keys: 
                if not result[key]:
                    dfs(key, rooms)
        
        
        dfs(0, rooms)
        return all(result)
