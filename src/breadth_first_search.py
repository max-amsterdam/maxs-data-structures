import collections

class Solution:
    def routeBtwNodesBFS(self, n1, n2):
        """
        Implement with a queue

        This runs in O(N) time where N = number of nodes in graph
        O(N) space (queue)
        """
        q = collections.deque()
        n1.visited = True
        q.appendleft(n1)
        while q:
            node = q.pop()
            if node is n2:
                return True
            for n in node.children:
                if not n.visited:
                    n.visited = True
                    q.appendleft(n)
        return False
