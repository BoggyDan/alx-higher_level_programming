import sys
num = 0
if len(sys.argv) == 1:
    print("{} arguments.".format(len(sys.argv) - 1))
elif len(sys.argv) == 2:
    print("{} argument:".format(len(sys.argv)-1))
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
    for arg in sys.argv:
        if num > 0:
            print("{}: {}".format(num, arg))
        num += 1
