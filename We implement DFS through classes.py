
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
        self.root = root

    def dfs(self):
        visited = []
        stack = [self.root]

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                stack.extend(current.outbound)

        return visited


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)
result = g.dfs()
print(result)
