#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r") as f:
        print(f.read())

# Exemple d'utilisation
read_file("my_file_0.txt")
