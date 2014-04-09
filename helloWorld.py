#!/usr/bin/env python
from sys import exit
from getpass import getuser


def main():
    print("Hello world")
    print("Hello %s" % getuser())


if __name__ == "__main__":
    main()
    exit(0)
