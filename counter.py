""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
import pickle
from pickle import dump, load


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """

    if reset == True:
        fout = open(file_name,'wb')
        initial_value = 1
        stringed_new_value = pickle.dumps(initial_value)
        updated_value = pickle.loads(stringed_new_value)
        fout.write(stringed_new_value)
        fout.close()
        return updated_value
    elif reset == False:
        if exists(file_name):
            fout = open(file_name,'rb+')
            initial_value = pickle.load(fout)
            fout.close()
            fout = open(file_name, 'wb')
            updated_value = initial_value + 1
            stringed_new_value = pickle.dumps(updated_value)
            fout.write(stringed_new_value)
            fout.close()
            return updated_value
        elif:


if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
