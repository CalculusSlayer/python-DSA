"""
Nayeel Imtiaz
8-4-24

client.py
Client file that uses UnionFind ADT functionality
"""

from UnionFind import UnionFind
from collections import defaultdict
from typing import Dict


def print_groups(u: UnionFind, m: Dict) -> None:
    groups = defaultdict(set)
    for name, index in m.items():
        groups[u.find(index)].add(name)
    print(f"groups = {list(groups.values())}")


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

    print_groups(u, map)

    print()
    print(f"are kat and adam connected? : {u.connected(map['kat'], map['adam'])}")
    print(f"are bob and adam connected? : {u.connected(map['bob'], map['adam'])}")
    # 0    1    2     3    4

    u.union(map['kat'], map['emily'])
    u.union(map['kat'], map['john'])
    # does nothing because they
    # are already in the same group
    # u.union(map['emily'], map['john'])
    print_groups(u, map)
    print(u)

    # throws error since components
    # attribute is set to read-only
    try:
        u.components = 99
        print(u)
    except AttributeError as e:
        print(f"ERROR: {e}")




if __name__ == '__main__':
    main()