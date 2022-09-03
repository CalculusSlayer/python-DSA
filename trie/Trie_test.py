import Trie as t

def main():
    NewTrie = t.Trie()
    NewTrie.insertString ("App")
    NewTrie.insertString ("Appl")

    print(NewTrie.searchString("App"))  # True
    print(NewTrie.searchString("Appl")) # True
    print(NewTrie.searchString(""))     # False
    print(NewTrie.searchString("A"))    # False
    print(NewTrie.searchString("Appz")) # False






if __name__ == "__main__":
    main()