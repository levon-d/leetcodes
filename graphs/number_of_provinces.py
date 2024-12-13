class Solution:
    def dfs(self, node, isConnected, visited): 
        visited[node] = 1 

        neighbours = isConnected[node]

        for i in range(len(neighbours)):
            if neighbours[i] == 1 and not visited[i]:
                self.dfs(i, isConnected, visited)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0] * len(isConnected)
        count = 0 
        for i in range(len(isConnected)): 
            if not visited[i]:
                count += 1 
                self.dfs(i, isConnected, visited)
        
        return count
