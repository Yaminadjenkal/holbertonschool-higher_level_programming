#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:  # Vérifie si la liste n'est pas vide
        for i in reversed(my_list):
            print("{:d}".format(i))
