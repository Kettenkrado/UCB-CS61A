# su16-mt-7.Game of Throne
def tree(entry, children=[]):
    return [entry, children]

def entry(tree):
    return tree[0]

def children(tree):
    return tree[1]

def track_lineage(family_tree, name):
    """Return the entries of the parent and the grandparent of the node with entry name
    in the family tree.
    
    >>> t = tree('Tytos', [
    ...         tree('Tywin', [
    ...              tree('Cersei'), tree('Jaime'), tree ('Tyrion')
    ...         ]),
    ...         tree('Kevan', [
    ...             tree ('Lancel'), tree('Martyn'), tree('Willem')
    ...         ])])
    >>> track_lineage(t, 'Cersei')
    ['Tywin', 'Tytos']
    >>> track_lineage(t, 'Tywin')
    ['Tytos', None]
    >>> track_lineage(t, 'Tytos')
    [None, None]
    """
    def tracker(t, p, gp):
        if entry(t) == name:
            return [p, gp]
        for c in children(t):
            res = tracker(c, entry(t), p) # next time, p is entry(t) of last time parameter
            if res:
                return res
    return tracker(family_tree, None, None)

def are_cousins(family_tree, name1, name2):
    """Return True if a node with entry name1 is a cousin of a node with
    entry name2 in family_tree.

    >>> t = tree('Tytos', [
    ...         tree('Tywin', [
    ...              tree('Cersei'), tree('Jaime'), tree ('Tyrion')
    ...         ]),
    ...         tree('Kevan', [
    ...             tree ('Lancel'), tree('Martyn'), tree('Willem')
    ...         ])])
    >>> are_cousins(t, 'Kevan', 'Tytos') 
    False
    >>> are_cousins(t, 'Cersei', 'Lancel')
    True
    >>> are_cousins(t, 'Jaime', 'Lancel')
    True
    >>> are_cousins(t, 'Jaime', 'Tyrion')
    False
    """
    lineage1 = track_lineage(family_tree, name1)
    lineage2 = track_lineage(family_tree, name2)
    if lineage1[0] != lineage2[0] and lineage1[1] == lineage2[1] and lineage1[1]:
        return True
    else:
        return False