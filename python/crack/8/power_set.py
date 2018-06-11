
def find_subsets(a_set, part_idx, subsets):
    if len(a_set) == 0:
        return subsets
    
    
def power_set(a_set):
    '''
    8.4 return all sub-sets of a set
    
    Time :
    Space:
    Note :
    '''
    if a_set == None or len(a_set):
        return a_set

    subsets = []
    find_subsets(a_set, set(), subsets)

def run():
    pass

if __name__ == '__main__':
    run()

