class Trie:
    class _TrieNode:
        def __init__(self, val, endOfWord=False):
            self.val = val
            self.children = {} # str : _TrieNode
            self.endOfWord = endOfWord

    def __init__(self):
        self.root = self._TrieNode("", endOfWord=True)
    
    def addWord(self, string):
        currentNode = self.root
        for index in range(len(string)):
            if string[index] not in currentNode.children:
                currentNode.children[string[index]] = self._TrieNode(string[index])
            currentNode = currentNode.children[string[index]]

        currentNode.endOfWord = True

    def pruneWord(self, word: str):
        currentNode = self.root
        path = [self.root] # _TrieNode[]
        for char in word:
            if char not in currentNode.children:
                return
            currentNode = currentNode.children[char]
            path.append(currentNode)
        currentNode.endOfWord = False

        for index in range(len(path)-1, 0, -1):
            # print(f"index = {index}, path[index].val = {path[index].val}\n"
            # + f"len(path[index].children = {len(path[index].children)}\n)"
            # + f"path[index].children = {path[index].children}")
            if len(path[index].children) == 0:
                del path[index-1].children[path[index].val]
            else:
                break

    def searchWord(self, string):
        currentNode = self.root
        for index in range(len(string)):
            if string[index] not in currentNode.children:
                return False
            currentNode = currentNode.children[string[index]]
        if currentNode.endOfWord:
            return True
        return False

    def searchPrefix(self, string):
        currentNode = self.root
        for index in range(len(string)):
            if string[index] not in currentNode.children:
                return False
            currentNode = currentNode.children[string[index]]
        return True

    def __repr__(self):
        queue = [self.root]
        string_ = ""
        while queue:
            r = queue.pop(0)
            string_ += f"TrieNode({r.val}) "
            for child in r.children:
                queue.append(r.children[child])
        return string_

trie = Trie()
words = ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"]


for word in words:
    trie.addWord(word)

for word in words:
    print(f"{word}: {trie.searchWord(word)}")
print()
print(f"at: {trie.searchWord("at")}")

trie.pruneWord("oathfii")
print(f"oathfii: {trie.searchWord("oathfii")}")

trie.pruneWord("oath")
print(f"oath (findWord): {trie.searchWord("oath")}")
print(f"oath (findPrefix): {trie.searchPrefix("oath")}")
print()
print()

trie2 = Trie()
words2 = ["oa", "oaa"]
for word in words2:
    trie2.addWord(word)
trie2.pruneWord("oa")
print(f"oa (findWord): {trie2.searchWord("oa")}")
print(f"oaa (findWord): {trie2.searchWord("oaa")}")
print(trie2)
