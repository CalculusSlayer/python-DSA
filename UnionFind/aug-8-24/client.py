"""
Nayeel Imtiaz
8-4-24

client.py
Client file that uses UnionFind ADT functionality
"""

from UnionFind import UnionFind

def main():
    map = {
        "adam": 0,
        "bob": 1,
        "kat": 2,
        "emily": 3,
        "john": 4,
    }

    u = UnionFind(len(map))
    print(u)

    u.union(map["adam"], map["bob"])
    print(u)
    # 0    1    2     3    4




if __name__ == '__main__':
    main()