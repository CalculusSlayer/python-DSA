"""
Nayeel Imtiaz
tries.py

Leetcode 208 - Implement trie

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""

class Trie:
    class TrieNode:
        def __init__(self, letter):
            self.letter = letter
            self.isCompleteWord = False
            self.childrenDictionary = {} #

    def __init__(self):
        self.root = self.TrieNode("")
        self.root.isCompleteWord = True
    
    def __repr__(self):
        queue = [self.root]
        string_ = ""
        while queue:
            r = queue.pop(0)
            string_ += f"TrieNode({r.letter}) "
            for child in r.childrenDictionary:
                queue.append(r.childrenDictionary[child])
        return string_

    def insert(self, word: str) -> None:
        current_index = 0
        n = self.root
        while current_index < len(word):
            if word[current_index] not in n.childrenDictionary:
                n.childrenDictionary[word[current_index]] = self.TrieNode(word[current_index])
            n = n.childrenDictionary[word[current_index]]
            current_index += 1

        n.isCompleteWord = True   

    def search(self, word: str) -> bool:
        current_index = 0
        n = self.root
        while current_index < len(word):
            if word[current_index] not in n.childrenDictionary:
                break
            n = n.childrenDictionary[word[current_index]]
            current_index += 1

        if current_index >= len(word) and n.isCompleteWord:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        current_index = 0
        n = self.root
        while current_index < len(prefix):
            if prefix[current_index] not in n.childrenDictionary:
                break
            n = n.childrenDictionary[prefix[current_index]]
            current_index += 1

        if current_index >= len(prefix):
            return True
        return False

# Your Trie object will be instantiated and called as such:
obj = Trie()
print(obj)

obj.insert("try")
print(obj)

print(f"try is in the trie: {obj.search("try")}")
print(f"try is in the trie: {obj.search("tr")}")


print(f"prefix tr is contained here: {obj.startsWith("tr")}")
# obj.insert("tr")
# print(f"try is in the trie: {obj.search("tr")}")
# obj.search("")
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)