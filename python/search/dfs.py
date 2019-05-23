# -*- coding: utf-8 -*-

from copy import deepcopy

def parse_route(route):                                             # O(1)
    if not route or \
       not route[0] or \
       not route[1] or \
       not isinstance(route[0], basestring) or \
       not isinstance(route[1], int):                               # O(1)
        return None                                                 # O(1)

    path = route[0].split('-')                                      # O(1)
    if len(path) != 2 or \
       len(path[0]) != 1 or \
       len(path[1]) != 1:                                           # O(1)
        return None                                                 # O(1)

    return {
        'origin': path[0],
        'dest': path[1],
        'distance': route[1]
    }                                                               # O(1)

def add_route(routelist, origin, dest, distance):                   # O(1)
    if origin not in routelist:                                     # O(1)
        routelist[origin] = dict([(dest, distance)])                # O(1)
    elif dest not in routelist[origin]:                             # O(1)
        routelist[origin][dest] = distance                          # O(1)

def prepare_routelist(r):                                           # O(N)
    routelist = {}                                                  # O(1)
    for route in r:                                                 # O(N)
        parsed_route = parse_route(route)                           # O(1)
        if parsed_route:                                            # O(1)
            add_route(routelist,
                      parsed_route['origin'],
                      parsed_route['dest'],
                      parsed_route['distance'])                     # O(1)
            add_route(routelist,
                      parsed_route['dest'],
                      parsed_route['origin'],
                      parsed_route['distance'])                     # O(1)
    return routelist                                                # O(1)

def prepare_visited(routelist):                                     # O(N)
    visited = {}                                                    # O(1)
    for key in routelist.keys():                                    # O(N)
        visited[key] = False                                        # O(1)
    return visited                                                  # O(1)

def get_next_node(result, visited, position, distance):             # O(N)
    state = {
        'position': position,
        'result': deepcopy(result),
        'visited': deepcopy(visited)
    }                                                               # O(1)
    state['result']['route'].append(position)                       # O(1)
    state['result']['length'] += distance                           # O(1)
    return state                                                    # O(1)

def get_shortest_route(results):                                    # O(N)
    final_result = {}                                               # O(1)
    for result in results:                                          # O(N)
        if not final_result or \
           result['length'] < final_result['length']:               # O(1)
            final_result = result                                   # O(1)

    if final_result:                                                # O(1)
        return final_result                                         # O(1)
    return {
        'route': [],
        'length': -1
    }                                                               # O(1)

def dfs(routelist, node, finish, results):                          # O(N^2)
    current_position = node['position']                             # O(1)
    current_result = node['result']                                 # O(1)
    current_visited = node['visited']                               # O(1)
    if current_position == finish:                                  # O(1)
        results.append(current_result)                              # O(1)

    current_visited[current_position] = True                        # O(1)
    next_positions = routelist[current_position]                    # O(1)
    for position, distance in next_positions.iteritems():           # O(N)
        if not current_visited[position]:                           # O(1)
            return dfs(
                routelist,
                get_next_node(
                    current_result,
                    current_visited,
                    position, distance
                ),
                finish,
                results
            )                                                       # O(N)

    return results                                                  # O(1)

def solution(routes, start, finish):                                # O(N^2)
    """
    Given a list of routes and their lengths, find the shortest route between 2
    nodes using breadth first search.

    >>> solution([('a-b', 4), ('b-c', 2), ('a-f', 1), ('a-j', 2), ('b-d', 3),
    ... ('c-e', 1), ('d-g', 3), ('c-i', 1), ('f-h', 2)], 'a', 'c')
    {'route': ['a', 'b', 'c'], 'length': 6}
    >>> solution([('a-b', 4), ('b-c', 2), ('a-f', 1), ('a-j', 2), ('b-d', 3),
    ... ('c-e', 1), ('d-g', 3), ('c-i', 1), ('f-h', 2), ('e-a', 1)], 'a', 'c')
    {'route': ['a', 'e', 'c'], 'length': 2}
    >>> solution([], 'a', 'c')
    {'route': [], 'length': -1}
    >>> solution([('a-b', 4), ('b-cd', 1)], 'a', 'c')
    {'route': [], 'length': -1}
    >>> solution([('a-b', 4), ('b-c-d', 1)], 'a', 'c')
    {'route': [], 'length': -1}
    >>> solution([('a-b', 4), ('b-c', '1')], 'a', 'c')
    {'route': [], 'length': -1}
    >>> solution([('a-b', 4), (True, 1)], 'a', 'c')
    {'route': [], 'length': -1}
    """
    routelist = prepare_routelist(routes)                           # O(N)
    if not start in routelist or not finish in routelist:           # O(1)
        return {
            'route': [],
            'length': -1
        }                                                           # O(1)

    node = {
        'position': start,
        'result': {
            'route': [start],
            'length': 0
        },
        'visited': prepare_visited(routelist)
    }                                                               # O(1)

    results = dfs(routelist, node, finish, [])                      # O(N^2)
    return get_shortest_route(results)                              # O(N)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
