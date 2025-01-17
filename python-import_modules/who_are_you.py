#!/usr/bin/python3
import sys
import importlib.util

def print_module_names(module_path):
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)
    names = sorted(name for name in dir(hidden_4) if not name.startswith("__"))
    for name in names:
        print(name)

if __name__ == "__main__":
    module_path = "/tmp/hidden_4.pyc"
    print_module_names(module_path)

