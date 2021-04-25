import random

def random_color():
    '''
    This function generates an RGB value tuple
    RGB Tuple => (R,G,B) where
        R = Amount of red in the color
        G = Amount of green in the color
        B = Amoutn of blue in the color
        
    Output -
    rand_color (tuple) : A tuple of R,G,B values that can correspond to any random color each time the function is executed
    '''
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

def rgb_to_hex():
    '''
    This function converts an RGB tuple into a hexa representation of the color
    
    Output -
    A hexa color code that can be any random color for every execution
    '''
    return '%02x%02x%02x' % random_color()