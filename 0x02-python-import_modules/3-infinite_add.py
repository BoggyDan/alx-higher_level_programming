#!/usr/bin/python3
if "__name__" == "__main__":
    import sys
    num = 0
    for arg in sys.argv[1:]:
        num += int(arg)
    print(num)
