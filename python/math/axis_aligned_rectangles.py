def solution(A):                                                    # O(N)
    """
    Describe  an  algorithm  that  takes  an  unsorted  array  of  axis‐aligned  rectangles  and
    returns  any  pair  of  rectangles  that  overlaps,  if  there  is  such  a  pair.

      Axis‐aligned  means  that  all  the  rectangle  sides  are  either  parallel  or
     perpendicular  to  the  x‐  and  y‐axis.

      You  can  assume  that  each  rectangle  object  has  two  variables  in  it:
    the  x‐y  coordinates  of  the  upper‐left  corner  and  the  bottom‐right corner.

    # >>> solution([ \
    #     [(3, 5), (7, 1)], \
    #     [(2, 8), (12, -4)], \
    #     [(10, 2), (12, -3)], \
    #     [(-1, 14), (2, 9)] \
    # ])
    # [ \
    #     [(3, 5), (7, 1)], \
    #     [(2, 8), (12, -4)] \
    # ]
    """
    print(A)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
