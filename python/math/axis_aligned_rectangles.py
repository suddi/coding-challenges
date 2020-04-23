def detect_overlap(r1, r2):
    if r1[0][0] <= r2[1][0] and r1[1][0] >= r2[0][0] and \
        r1[0][1] >= r2[1][1] and r1[1][1] <= r2[0][1]:
        return True
    return False

def solution(A):                                                    # O(N)
    """
    Describe  an  algorithm  that  takes  an  unsorted  array  of  axis‐aligned  rectangles  and
    returns  any  pair  of  rectangles  that  overlaps,  if  there  is  such  a  pair.

      Axis‐aligned  means  that  all  the  rectangle  sides  are  either  parallel  or
     perpendicular  to  the  x‐  and  y‐axis.

      You  can  assume  that  each  rectangle  object  has  two  variables  in  it:
    the  x‐y  coordinates  of  the  upper‐left  corner  and  the  bottom‐right corner.

    >>> solution([ \
        [(3, 5), (7, 1)], \
        [(2, 8), (12, -4)], \
        [(10, 2), (12, -3)], \
        [(-1, 14), (2, 9)] \
    ])
    [([(3, 5), (7, 1)], [(2, 8), (12, -4)]), ([(2, 8), (12, -4)], [(10, 2), (12, -3)])]
    """
    length = len(A)
    overlaps = []
    for i in range(1, length):
        r1 = A[i - 1]
        r2 = A[i]
        overlap = detect_overlap(r1, r2)
        if overlap:
            overlaps.append((r1, r2))

    return overlaps

if __name__ == '__main__':
    import doctest
    doctest.testmod()
