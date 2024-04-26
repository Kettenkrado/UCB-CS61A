def generate_constant(x):
    """Q: Streams and Jennyrators
    a. Write generate_constant, a generator function that repeatedly yields the same value forever.

    A generator function that repeats the same value X forever.  
    >>> two = generate_constant(2)
    >>> next(two)
    2
    >>> next(two)
    2
    >>> sum([next(two) for _ in range(100)])
    200
    """
    while True:
        yield x


def black_hole(seq, trap):
    """b. Now implement black_hole, a generator that yields items in seq until one of them matches trap, in
    which case that value should be repeated yielded forever. You may assume that generate_constant works.
    You may not index into or slice seq.

    A generator that yields items in SEQ until one of them matches TRAP, in
    which case that value should be repeatedly yielded forever.
    >>> trapped = black_hole([1, 2, 3], 2)
    >>> [next(trapped) for _ in range(6)]
    [1, 2, 2, 2, 2, 2]
    >>> list(black_hole(range(5), 7))
    [0, 1, 2, 3, 4]
    """
    for i in seq:
        if i == trap:
            yield from generate_constant(i)
        else: 
            yield i


def love():
    yield 1000
    yield from [2000, 3000]

x = love()
L = list(x)

def alternate(real, ity):
    i1, i2 = iter(real), iter(ity)
    try:
        while True:
            yield next(i1)
            yield next(i2)
    except StopIteration:
        yield 'inevitable'

thanos = ['power', 'space', 'reality']
tony = ['mind', 'soul', 'time']
i = iter(tony)
next(i)
tony.extend(list(i))
thanos = tony[2::-2]

def check():
    """
    answer the following questions: WWPD
    pow(10, 2)
    print(print('end', print('game')), x)
    L
    next(x)
    tony
    list(alternate(thanos[1:], thanos))
    """

# tree Data Abstraction

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


def word_finder(letter_tree, words_list):
    """Q:  Implement word_finder, a generator function that yields each word that can be formed by following a path in
    a tree from the root to a leaf, where the words are specified in a list.
    When given the tree shown in the diagram below and a word list that includes ‘SO’ and ‘SAW’, the function
    should first yield ‘SO’ and then yield ‘SAW’.

    Generates each word that can be formed by following a path
    in TREE_OF_LETTERS from the root to a leaf,
    where WORDS_LIST is a list of allowed words (with no duplicates).

    # Case 1: 2 words found
    >>> words = ['SO', 'SAT', 'SAME', 'SAW', 'SOW']
    >>> t = tree("S", [tree("O"), tree("A", [tree("Q"), tree("W")]), tree("C", [tree("H")])])
    >>> gen = word_finder(t, words)
    >>> next(gen)
    'SO'
    >>> next(gen)
    'SAW'
    >>> list(word_finder(t, words))
    ['SO', 'SAW']

    # Case 2: No words found
    >>> t = tree("S", [tree("I"), tree("A", [tree("Q"), tree("E")]), tree("C", [tree("H")])])
    >>> list(word_finder(t, words))
    []

    # Case 3: Same word twice
    >>> t = tree("S", [tree("O"), tree("O")] )
    >>> list(word_finder(t, words))
    ['SO', 'SO']

    # Case 4: Words that start the same
    >>> words = ['TAB', 'TAR', 'BAT', 'BAR', 'RAT']
    >>> t = tree("T", [tree("A", [tree("R"), tree("B")])])
    >>> list(word_finder(t, words))
    ['TAR', 'TAB']

    # Case 5: Single letter words
    >>> words = ['A', 'AN', 'AH']
    >>> t = tree("A")
    >>> list(word_finder(t, words))
    ['A']

    # Case 6: Words end in leaf
    >>> words = ['A', 'AN', 'AH']
    >>> t = tree("A", [tree("H"), tree("N")])
    >>> list(word_finder(t, words))
    ['AH', 'AN']

    # Case 7: Words start at root
    >>> words = ['GO', 'BEARS', 'GOB', 'EARS']
    >>> t = tree("B", [tree("E", [tree("A", [tree("R", [tree("S")])])])])
    >>> list(word_finder(t, words))
    ['BEARS']

    # Case 8: This special test ensures that your solution does *not*
    # pre-compute all the words before yielding the first one.
    # If done correctly, your solution should error only when it
    # tries to find the second word in this tree.
    >>> words = ['SO', 'SAM', 'SAT', 'SAME', 'SAW', 'SOW']
    >>> t = tree("S", [tree("O"), tree("A", [tree("Q"), tree(1)]), tree("C", [tree(1)])])
    >>> gen = word_finder(t, words)
    >>> next(gen)
    'SO'
    >>> try:
    ...     next(gen)
    ... except TypeError:
    ...     print("Got a TypeError!")
    ... else:
    ...     print("Expected a TypeError!")
    Got a TypeError!
    """
    def find_word(letter_tree, word=''):
        word += label(letter_tree) # Optional
        if word in words_list and is_leaf(letter_tree):
            yield word
        for b in branches(letter_tree):
            yield from find_word(b, word)
        
    yield from find_word(letter_tree)


def integers(n):
    while True:
        yield n
        n += 1

def drop(n , s):
    for _ in range(n):
        next(s)
    for elem in s:
        yield elem

def powers_of_two(ints = integers(0)):
    """Q: Implement the generator function powers of two that iterates over the infinite sequence of non-negative integer
    powers of two, starting from 1. You must do this by selectively including elements from an infinite sequence of
    integers, created by calling the provided integers generator function.
    You may only use the lines provided. You may not need to fill all the lines.
    Hint: You may find the drop generator function useful.

    >>> p = powers_of_two ()
    >>> [next(p) for _ in range(10)]
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    """
    curr = next(ints)
    yield next(drop(pow(2, curr), integers(0)))
    yield from powers_of_two(ints)

    # curr = next ( ints )
    # yield curr
    # yield from powers_of_two ( drop ( curr -1 , ints ))