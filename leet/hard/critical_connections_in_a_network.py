#!/usr/local/bin/python3

from typing import List

def critical_connections_in_a_network(n: int, connections: List[List[int]]) -> List[List[int]]:
    """
    https://leetcode.com/problems/critical-connections-in-a-network/

    Time :
    Space:
    Note :
    """
    connections_map = {i:[] for i in range(0, n)}
    for conn in connections:
        connections_map.get(conn[0]).append(conn[1])
        connections_map.get(conn[1]).append(conn[0])

    ret_conns = []
    print(connections_map)
    # for key, value in connections_map.items():
    #

    return ret_conns


def run():
    # print(critical_connections_in_a_network(4, [[0,1],[1,2],[2,0],[1,3]]))
    print(critical_connections_in_a_network(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]))


if __name__ == '__main__':
    run()
