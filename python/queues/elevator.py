def validate_floors(floors, max_floors):                            # O(N)
    for floor in floors:                                            # O(N)
        if floor > max_floors:                                      # O(N)
            raise Exception('Requested floor higher than the ' + \
                'maximum number of floors in the building: %s' \
                % max_floors)                                       # O(1)

def solution(A, B, M, X, Y):                                        # O(N)
    """
    You are provided arrays A and B, and values M, X and Y:
    A contains the list of the weight of N people waiting to use the elevator.
    B contains the floors each of the N people need to visit.

    You are also given:
        M (number of floors in the building),
        X (maximum capacity of lift),
        Y (maximum weight limit on lift)

    Given that people must be served in the order they arrive,
    Write a function to calculate the number of floors the lift must stop at and come back
    to the ground floor in order to service all of the people.

    eg. A = [40, 40, 100, 60], B = [3, 3, 2, 2], M = 3, X = 3, Y = 200
    1) Lift will take person 1, 2, 3 to floor 3 and floor 2 => 2 floors
    2) Lift will return to ground floor => 1 floor
    3) Lift will take person 4 to floor 2 => 1 floor
    4) Lift will return to ground floor => 1 floor
    Total floors = 5

    Worst time complexity = O(N)
    Expected auxillary space complexity = O(N)

    >>> solution([40, 40, 100, 60], [3, 3, 2, 2], 3, 5, 200)
    5
    >>> solution([40, 40, 100, 80, 20], [3, 3, 2, 2, 3], 3, 5, 200)
    6
    >>> solution([40, 40], [3, 2], 3, 2, 100)
    3
    """
    i = 0                                                           # O(1)
    count = 0                                                       # O(1)
    weight = 0                                                      # O(1)
    num_people = 0                                                  # O(1)
    floors = set()                                                  # O(1)
    length = len(A)                                                 # O(1)

    def validate_weight(w):
        return w <= Y                                               # O(1)

    def validate_capacity(c):
        return c <= X                                               # O(1)

    def run_elevator(c, f):
        return c + len(f) + 1                                       # O(1)

    validate_floors(B, M)                                           # O(N)
    while i < length:                                               # O(N)
        if validate_weight(weight + A[i]) and \
           validate_capacity(num_people + 1):                       # O(1)
            weight += A[i]                                          # O(1)
            num_people += 1                                         # O(1)
            floors.add(B[i])                                        # O(1)
            i += 1                                                  # O(1)
        else:                                                       # O(1)
            count = run_elevator(count, floors)                     # O(1)
            weight = 0                                              # O(1)
            num_people = 0                                          # O(1)
            floors.clear()                                          # O(1)


    return run_elevator(count, floors)                              # O(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
