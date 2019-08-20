class Solution:
    def routeBtwNodesDFS(self, n1, n2):
            """
            Implement with recursion

            This runs in O(N) time where N = number of nodes in graph
            O(N) space (stack in recursion)
            """
            if not n1 or not n2:
                return False

            n1.visited = True
            for n in n1.children:
                if not n.visited:
                    if n is n2:
                        return True
                    else:
                        return self.routeBtwNodesDFS(n, n2)
            return False 