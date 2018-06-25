
def flipping_an_image(img_matrix):
    '''

    https://leetcode.com/problems/flipping-an-image/description/

    Time :
    Space:
    Note :
    '''
    
    if img_matrix == None or len(img_matrix) == 0:
        return []

    for idx, elem in enumerate(img_matrix):
        elem.reverse()
        elem = [abs(x - 1) for x in elem]
        img_matrix[idx] = elem

    return img_matrix

def run():
    img_matrix = [[1,1,0],[1,0,1],[0,0,0]]
    print("reversed %s " % flipping_an_image(img_matrix))
    # Input: [[1,1,0],[1,0,1],[0,0,0]]
    # Output: [[1,0,0],[0,1,0],[1,1,1]]
    # reversed [[1, 0, 0], [0, 1, 0], [1, 1, 1]] 


    img_matrix = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print("reversed %s " % flipping_an_image(img_matrix))
    # Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    # Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    # reversed [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]] 


if __name__ == '__main__':
    run()

