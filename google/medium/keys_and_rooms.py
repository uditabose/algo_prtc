#!/usr/local/bin/python3

def keys_and_rooms(rooms_keys):
    '''
    There are N rooms and you start in room 0.  Each room 
    has a distinct number in 0, 1, 2, ..., N-1, and each 
    room may have some keys to access the next room. 

    Formally, each room i has a list of keys rooms[i], and 
    each key rooms[i][j] is an integer in [0, 1, ..., N-1] 
    where N = rooms.length.  A key rooms[i][j] = v opens the 
    room with number v.

    Initially, all the rooms start locked (except for room 0). 
    You can walk back and forth between rooms freely.
    Return true if and only if you can enter every room.

    Example 1:

    Input: [[1],[2],[3],[]]
    Output: true
    Explanation:  
    We start in room 0, and pick up key 1.
    We then go to room 1, and pick up key 2.
    We then go to room 2, and pick up key 3.
    We then go to room 3.  Since we were able to go 
    to every room, we return true.
    Example 2:

    Input: [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can't enter the room with number 2.
    Note:

    1 <= rooms.length <= 1000
    0 <= rooms[i].length <= 1000
    The number of keys in all rooms combined is at most 3000.
 
    https://leetcode.com/problems/keys-and-rooms/description/

    Time :
    Space:
    Note :
    1. a set for found keys, queue for traversal
    2. start at 0-th room, put keys in the set
    3. check the length of the set, 
        a. equals the number of rooms, break return true
        b. not equal, then move to next room
    4. at the end check again for the length of set and room list
    '''
    if rooms_keys == None or len(rooms_keys) < 2:
        return True

    keys_found = set([0])
    keys_queue = [rooms_keys[0]]

    while len(keys_queue) > 0:

        if len(keys_found) == len(rooms_keys):
            return True

        keys = keys_queue.pop()

        for key in keys:
            if key not in keys_found:
                keys_queue.append(rooms_keys[key])

        keys_found.update(keys)

    return False

def run():
    rooms_keys = [[1],[2],[3],[]]
    print("can go till end %s" % str(keys_and_rooms(rooms_keys)))
    
    rooms_keys = [[1,3],[3,0,1],[2],[0]]
    print("can go till end %s" % str(keys_and_rooms(rooms_keys)))

if __name__ == '__main__':
    run()

