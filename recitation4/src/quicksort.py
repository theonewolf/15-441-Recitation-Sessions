#!/usr/bin/env python
###############################################################################
#                                                                             #
#   This script implements quicksort pseudo-code as listed on Wikipedia.      #
#   It is an example script for Recitation 4 of 15-441                        #
#                                                                             #
#   Author: Wolfgang Richter <wolf@cs.cmu.edu>                                #
#                                                                             #
###############################################################################


def quicksort(array):
    """Return a list in sorted order (not in place sorting).

    Example run:

    >>> quicksort([9,8,4,5,32,64,2,1,0,10,19,27])
    [0, 1, 2, 4, 5, 8, 9, 10, 19, 27, 32, 64]
    """
    
    less = []; greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot: less.append(x)
        else: greater.append(x)
    return quicksort(less)+[pivot]+quicksort(greater)


# only run if running as main() (executed directly), otherwise we are a library
if __name__ == '__main__':
    # demo doctest -- not normally done
    # try running this: python quicksort.py -v
    import doctest
    doctest.testmod()

    # try out quicksort on some random integers
    array = [323,5646,7876,23345,445,6,7,12,4345,678]
    print quicksort(array)
