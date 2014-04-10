#!/usr/bin/env python
import getpass


def main():
    print("Hola mundo!!")
    print("Hola %s" % getpass.getuser())
    print("ok")


if __name__ == "__main__":
    main()
