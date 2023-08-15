#!/usr/bin/python3

def sum_of_args(argv):
    count = len(argv) - 1
    if count == 0:
        print("{:d}".format(count))
        return
    else:
        i = 1
        total = 0
        while i <= count:
            total += int(argv[i])
            i += 1
        print("{:d}".format(total))


if __name__ == "__main__":
    import sys
    sum_of_args(sys.argv)
