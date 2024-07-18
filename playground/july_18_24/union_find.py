"""
Nayeel Imtiaz
7-18-24

union_find.py
This file implements the Union Find
data structure in python
"""

class UnionFind:
    """
    This is a UnionFind data structure class
    """
    class _ListNode:
        def __init__(self, val=0, parent=None):
            self._val = val
            self.parent = parent
        
        def __repr__(self):
            return f"ListNode(val={self.val}, parent={self.parent.val if self.parent else None})"

        @property
        def val(self):
            return self._val
    
    def __init__(self, n):
        self.groups = [self._ListNode(val) for val in range(n)]
        self._components = n
    
    def __repr__(self):
        return f"self.groups = {self.groups}"
    
    def _find_represenative(self, val):
        current = self.groups[val]
        while current and current.parent:
            current = current.parent
        return current
    
    def find(self, val):
        return self._find_represenative(val).val
    
    def union(self, val1, val2):
        val1_representative = self._find_represenative(val1)
        val2_representative = self._find_represenative(val2)
        if val1_representative != val2_representative:
            val2_representative.parent = val1_representative
            self._components -= 1
    
    @property
    def components(self):
        return self._components
