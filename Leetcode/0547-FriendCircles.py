from typing import List
import collections


class Solution(object):
    def findCircleNum(self, M):
        cnt, n = 0, len(M)
        self.vset = set()
        for x in range(n):
            if x not in self.vset:
                cnt += 1
                self.dfs(M, x)
        return cnt

    def dfs(self, M, n):
        for x in range(len(M)):
            if M[n][x] and x not in self.vset:
                self.vset.add(x)
                self.dfs(M, x)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected: return 0

        graph = collections.defaultdict(set)
        n = len(isConnected)
        for i in range(n):
            for j in range(i + 1):
                if isConnected[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)

        seen = set()

        def dfs(u):
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    dfs(v)

        res = 0
        for i in range(n):
            if i not in seen:
                res += 1
                seen.add(i)
                dfs(i)
        return res


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

    def find(self, x):
        if x == self.par[x]:
            return self.par[x]
        parent = self.find(self.par[x])
        self.par[x] = parent
        return parent

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.par[x] = y


class UnionFind:
    def __init__(self, n):
        self.parents = [x for x in range(n)]
        self.rank = [1 for _ in range(n)]
        self.groups = n

    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)

        if x_root == y_root:
            return True

        if self.rank[x_root] > self.rank[y_root]:
            self.parents[y_root] = x_root
            self.rank[x_root] += self.rank[y_root]
        else:
            self.parents[x_root] = y_root
            self.rank[y_root] += self.rank[x_root]
        self.groups -= 1

        return False


class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n < 1 or len(grid[0]) != n:
            return 0

        union = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    union.union(i, j)

        return union.groups


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        if n < 1 or len(isConnected[0]) != n:
            return 0

        union = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union.union(i, j)

        return union.groups


class UnionFind:
    def __init__(self, n):
        self.parents = [x for x in range(n)]
        self.rank = [1 for _ in range(n)]
        self.groups = n

    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)

        if x_root == y_root:
            return True

        if self.rank[x_root] > self.rank[y_root]:
            self.parents[y_root] = x_root
            self.rank[x_root] += self.rank[y_root]
        else:
            self.parents[x_root] = y_root
            self.rank[y_root] += self.rank[x_root]
        self.groups -= 1

        return False
