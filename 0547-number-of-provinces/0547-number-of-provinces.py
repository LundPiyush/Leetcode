class Solution:
    def dfs(self,node,vis,adj):
        vis[node] = True
        for ele in adj[node]:
            if not vis[ele]:
                self.dfs(ele,vis,adj)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected) # no of nodes
        adj = [[] for _ in range(V)]

        # convert adj matrix to adj list
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
        vis = [False] * V # marking all nodes in visited array as False 
        count = 0
    
        for i in range(V):
            if not vis[i]:
                count = count + 1 #count will increase when there is new starting node 
                self.dfs(i,vis,adj)
        return count

        