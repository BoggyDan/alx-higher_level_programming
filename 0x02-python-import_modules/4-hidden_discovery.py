#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    for name in dir(hidden_4):
        if name[0] != 0 and name[1] != 0:
            print(name)
