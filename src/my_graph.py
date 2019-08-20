class NoChildrenException(Exception):
    pass

class NodeDoesNotExistException(Exception):
    pass

class MyNode(object):
    def __init__(self, name):
        self.name = name 
        self.children = list()
        self.visited = False

    def addChild(self, node):
        self.children.append(node)

    def removeChild(self, name):
        if self.hasNoChildren():
            raise NoChildrenException()
        for c in self.children:
            if c.name == name:
                return self.children.remove(c)

    def hasNoChildren(self):
        return len(self.children) == 0


class MyGraph(object):
    def __init__(self):
        self.nodes = dict()
        self.size = 0
   
    def addNode(self, name):
        node = MyNode(name)
        self.nodes[node.name] = node
        self.size += 1

    def getNode(self, name):
        if name in self.nodes:
            return self.nodes[name] 
        else:
            return None

    def removeNode(self, name):
        if name in self.nodes:
            self.size -= 1
            return self.nodes.pop(name)
        else:
            raise NodeDoesNotExistException()

    def zeroVisited(self):
        for _, node in self.nodes.items():
            node.visited = False

    def isEmpty(self):
        return self.size == 0

def buildGraph():
    g = MyGraph()
    for i in range(12):
        g.addNode(i)
    g.getNode(0).children = [g.getNode(1), g.getNode(2)]
    g.getNode(1).children = [g.getNode(4), g.getNode(5)]
    g.getNode(2).children = [g.getNode(3), g.getNode(6)]
    g.getNode(4).children = [g.getNode(8)]
    g.getNode(5).children = [g.getNode(9)]
    g.getNode(6).children = [g.getNode(7)]
    g.getNode(7).children = [g.getNode(9)]
    g.getNode(8).children = [g.getNode(10)]
    g.getNode(9).children = [g.getNode(8)]
    return g