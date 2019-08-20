class MyTrieNode(object):

    def __init__(self, val=None):
        self.val = val
        self.children = dict()
        self.isTerminating = False

    def __repr__(self):
        return str(self.val)

    def addWord(self, word):
        if not word or len(word) == 0:
            return

        firstChar = word[0]
        child = self.getChild(firstChar)
        if not child:
            child = MyTrieNode(firstChar)
            self.children[firstChar] = child
        
        if len(word) > 1:
            child.addWord(word[1:])
        else:
            child.isTerminating = True

    def getChild(self, c):
        return self.children.get(c, None)

class MyTrie(object):
    def __init__(self, list_of_words):
        self.root = MyTrieNode()
        for word in list_of_words:
            self.root.addWord(word)

    def contains(self, prefix, exact):
        lastNode = self.root
        for c in prefix:
            lastNode = lastNode.getChild(c)
            if not lastNode:
                return False
        
        return not exact or lastNode.isTerminating
