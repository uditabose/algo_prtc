
def find_path_in_grid(rows, columns, off_limits, path):
    
    #print("r[%d]c[%d] :: %s" %(rows, columns, path))
    
    if rows < 1 and columns < 1:
        return path
    
    if rows == 1:
        subpath = [(0, x) for x in range(0, columns)]
        #print("subpath :: %s" % subpath)
        for off in off_limits:
            if off in subpath:
                return path

        if subpath != None or len(subpath) > 0:
            path.extend(subpath)
        return path
    
    if columns == 1:
        subpath = [(x, 0) for x in range(0, rows)]
        #print("subpath :: %s" % subpath)
        for off in off_limits:
            if off in subpath:
                return path

        if subpath != None or len(subpath) > 0:
            path.extend(subpath)
        return path

    #print(path)
    if (rows - 2, columns - 1) not in off_limits:
        subpath = find_path_in_grid(rows - 1, columns, off_limits, path)
        if subpath != None or len(subpath) > 0:
            path.extend(subpath)

    if (rows - 1, columns - 2) not in off_limits:
        subpath = find_path_in_grid(rows, columns - 1, off_limits, path)
        if subpath != None or len(subpath) > 0:
            path.extend(subpath)

    return path

def robot_in_grid(rows, columns, off_limits):
    '''
    8.2 Grid has `r` row and `c` columns. Robot can move right
    and down. There are some cells that are off limit. 
    find path from top left to bottom right.

    Time : O(N*M)
    Space: O(N*M)
    Note :
    '''

    no_off_limits = (off_limits == None or len(off_limits) == 0)

    if rows == 1:
        if no_off_limits:
            return set([(0, x) for x in range(0, columns)])
        else:
            return set([])
        
    if columns == 1:
        if no_off_limits:
            return set([(x, 0) for x in range(0, rows)])
        else:
            return set([])

    return find_path_in_grid(rows, columns, off_limits, set([]))

def run():
    rows = 5
    columns = 4
    off_limits = [(3, 2), (2, 1)]
    print(robot_in_grid(rows, columns, off_limits))

if __name__ == '__main__':
    run()

