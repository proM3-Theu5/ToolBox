def sq_subplot_dims(vals):

    '''
    This function generates dimensions of a sub-plot provided the total number of sub-plots expected
    It generates the number of rows and columns of the sub-plot figure so that a rectangular figure is generated
    
    Input -
    vals (int) : Number of sub-plots expected
    
    Output -
    [plot_x,plot_y] (list) : A list consisting of number of rows and number of columns
    '''
    
    len_sqrt = vals**(1/2)

    if len_sqrt.is_integer():
        plot_x = int(len_sqrt)
        plot_y = plot_x
    else:
        plot_x = int(len_sqrt) + 1
        plot_y = round(len_sqrt)

    return [plot_x,plot_y]