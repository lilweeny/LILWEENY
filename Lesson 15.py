from collections import deque
class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __repr__(self):
        return f'Node({self.value})'

class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        visited = []
        stack = [self._root]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(reversed(node.outbound))

        return visited

    def bfs(self):
        visited = []
        queue = deque([self._root])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                queue.extend(node.outbound)

        return visited

#test 1
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

print(g.dfs())
print(g.bfs())

#test 2
a = Node('a')
b = Node('b')
c = Node('c')
a.point_to(b)
b.point_to(c)

g = Graph(a)
print(g.dfs())
print(g.bfs())

#test 3
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
b.point_to(f)
c.point_to(e)

g = Graph(a)
print(g.dfs())
print(g.bfs())

#test 4
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
k = Node('k')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
a.point_to(e)
e.point_to(f)
e.point_to(g)
f.point_to(i)
f.point_to(h)
g.point_to(k)

g = Graph(a)
print(g.dfs())
print(g.bfs())