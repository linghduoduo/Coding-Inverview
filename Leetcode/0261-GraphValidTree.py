from typing import List
import collections


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        dist = collections.defaultdict(list)
        for n1, n2 in edges:
            dist[n1].append(n2)
            dist[n2].append(n1)

        visited = set()
        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for related in dist[node]:
                if related not in visited:
                    visited.add(related)
                    queue.append(related)
        return len(visited) == n


if __name__ == "__main__":
    res = Solution().validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]])
    print(res)
