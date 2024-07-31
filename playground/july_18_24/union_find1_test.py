"""
Nayeel Imtiaz
7-18-24

union_find1_test.py
This is a test file for the module `union_find.py`
"""

"""
def main():
    u = UnionFind(4)
    print(u)

    for val in range(4):
        print(f"representative for {val}: {u.find(val)}")
    print()
    
    u.union(0, 1)
    for val in range(4):
        print(f"representative for {val}: {u.find(val)}") 




if __name__ == '__main__':
    main()

"""
from union_find import UnionFind

def test_Union_Find_instantiation():
    union_find_size = 4
    u = UnionFind(union_find_size)
    assert len(u.groups) == union_find_size
    assert u.components == union_find_size
    
    for group in range(union_find_size):
        assert u.groups[group].val == group
        assert u.groups[group].parent == None


def test_Union_Find_find_representative():
    '''
    Test helper function for UnionFind.find() and
    UnionFind.union()
    '''
    
