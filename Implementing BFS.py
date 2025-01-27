from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'


class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):

        pass

    def bfs(self):
        visited = set()
        queue = deque([self._root])

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                print(current)
                for neighbor in current.outbound:
                    if neighbor not in visited:
                        queue.append(neighbor)

