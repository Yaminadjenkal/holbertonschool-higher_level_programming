#!/usr/bin/python
"""MyList Class
    A class that inherits 
    from list
"""


class Mylist(list):
    """fonction that definesa class Mylist
    """


    def print_sorted(self):
        """method that prints the list
        but sorted (ascending sort)
        """

        print(sorted(self))
