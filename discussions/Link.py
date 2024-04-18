class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
        
s = Link(1, Link(3, Link(5)))  

def add1(s, v): # valid, but not mutative
    """Add v to an ordered list s with no repeats, returning modified s."""
    if s == Link.empty:
        return Link(v)
    elif v == s.first:
        return s
    elif v < s.first: 
        return Link(v, s)
    else:
        return Link(s.first, add1(s.rest, v))

def add2(s, v):
    """Add v to an ordered list s with no repeats, returning modified s."""
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, s # error, but why?
    elif s.first < v and s.rest == Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        s = add2(s.rest, v)
    return s