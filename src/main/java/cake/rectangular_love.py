def rectangular_love(love1, love2):
    '''
    https://www.interviewcake.com/question/python/rectangular-love
    '''

    xo, wo = get_x_overlap(love1, love2)
    yo, lo = get_y_overlap(love1, love2)
    return (xo, yo, wo, lo)

def get_x_overlap(love1, love2):
    xo, wo = None, None

    if love1['left_x'] <= love2['left_x']:
        if love2['left_x'] - love1['left_x'] < love1['width']:
            xo = love2['left_x']
            if love2['left_x'] + love2['width'] > love1['left_x'] + love1['width']:
                wo = love1['width'] - (love2['left_x'] - love1['left_x'])
            else:
                wo = love2['width']

    else :
        if love1['left_x'] - love2['left_x'] < love2['width']:
            xo = love1['left_x']
            if love1['left_x'] + love1['width'] > love2['left_x'] + love2['width']:
                wo = love2['width'] - (love1['left_x'] - love2['left_x'])
            else:
                wo = love1['width']

    return xo, wo

def get_y_overlap(love1, love2):
    yo, lo = None, None

    if love1['bottom_y'] <= love2['bottom_y']:
        if love2['bottom_y'] - love1['bottom_y'] < love1['height']:
            yo = love2['bottom_y']
            if love2['bottom_y'] + love2['height'] > love1['bottom_y'] + love1['height']:
                lo = love1['height'] - (love2['bottom_y'] - love1['bottom_y'])
            else:
                lo = love1['height']

    else :
        if love1['bottom_y'] - love2['bottom_y'] < love2['height']:
            yo = love1['bottom_y']
            if love1['bottom_y'] + love1['height'] > love2['bottom_y'] + love2['height']:
                lo = love2['height'] - (love1['bottom_y'] - love2['bottom_y'])
            else:
                lo = love2['height']

    return yo, lo


if __name__ == '__main__':
    love1 = {
        # coordinates of bottom-left corner
        'left_x': 1,
        'bottom_y': 5,

        # width and height
        'width': 10,
        'height': 4
    }

    love2 = {
        # coordinates of bottom-left corner
        'left_x': 6,
        'bottom_y': 2,

        # width and height
        'width': 5,
        'height': 14
    }
    print(rectangular_love(love1, love2))