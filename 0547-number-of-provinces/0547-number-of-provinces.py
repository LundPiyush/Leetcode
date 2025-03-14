class Solution:
    def dfs(self,node,vis,adj):
        vis[node] = True
        for ele in adj[node]:
            if not vis[ele]:
                self.dfs(ele,vis,adj)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        adj = [[] for _ in range(V)]

        # convert adj matrix to adj list
        for i in range(V):
            for j in range(V):
                if i!=j and isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        vis = [False] * V
        count = 0
    
        for i in range(V):
            if not vis[i]:
                count = count + 1
                self.dfs(i,vis,adj)
        return count

        