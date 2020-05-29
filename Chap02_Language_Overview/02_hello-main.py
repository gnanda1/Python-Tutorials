#!/usr/bin/env python3

import platform

def main():
    print('Start of main function.')
    message()
    print('End of main function.')

def message():
    print()
    print('Beginning of message function.')
    print('This is python version {}'.format(platform.python_version()))
    print('End of the message function.')
    print()

if __name__ == '__main__': main()
