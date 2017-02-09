# some functions using comprehensions

def dot_prod(u: [float, ...], v: [float, ...]) -> float:
    """Return the dot product of u and v

    u, v --- non-empty lists of the same length

    >>> dot_prod([1.0, 2.0], [3.0, 4.0])
    11.0
    """
    # sum of products of pairs of corresponding coordinates of u and v
    # my answer: sum(u[i] * v[i] for i in range(len(u)))
    return sum([u_coord * v_coord for u_coord, v_coord in zip(u, v)])

def matrix_vector_prod(m: [[float, ...], ...], v: [float, ...]) -> [float, ...]:
    """Return the matrix-vector product of m x v

    m --- a non-empty list of lists of floats, all sublists the same length
    v --- a non-empty list of floats, all the same length as those in m

    >>> matrix_vector_prod([[1.0, 2.0], [3.0, 4.0]], [5.0, 6.0])
    [17.0, 39.0]
    """
    # list of dot products of vectors in m with v
    return [dot_prod(u, v) for u in m]

def pythagorean_triples(n: int) -> [(int, int, int), ...]:
    """Return list of pythagorean triples as non-descending tuples of ints from 1 to n

    n --- a positive integer
    
    >>> pythagorean_triples(5)
    [(3, 4, 5)]
    """
    # helper to check whether a triple is pythagorean and non_descending
    def ascending_pythagorean(t: (int, int, int)) -> bool:
        """Return True iff t is pythagorean and non-descending

        t --- triple of positive integers
        """
        return (t[0] <= t[1] <= t[2]) and (t[0]**2 + t[1]**2) == t[2]**2

    # filter just the ones that satisfy ascending_pythagorean
    # produce a list from the filter for ascending_pythagoreans from...
    return list(filter(ascending_pythagorean,
                       # ...the list of triples in the range 1..n
                       [(i, j, k) 
                        for i in range(1, n + 1)  
                        for j in range(1, n + 1) 
                        for k in range(1, n + 1)]))

def any_pythagorean_triples(start: int, finish: int) -> bool:
    """Return True iff there is at least one pythagorean triple formed
    of integers from start to finish

    start, finish --- positive integers

    >>> any_pythagorean_triples(1, 4)
    False
    >>> any_pythagorean_triples(1, 5)
    True
    """
    # are there any...
    return any(
        # pythagorean triples in the *generator* --- notice the (...) not [...]
        # look up generator comprehensions, and experiment with changing
        # it back to [...] and calling any_pythagorean_triples(500, 1000)
        ((i**2 + j**2) == k**2 
                for i in range(start, finish + 1)
                for j in range(start, finish + 1)
                for k in range(start, finish + 1)))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
