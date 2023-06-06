#!/usr/bin/python3
for value in range(ord('a'), ord('z') + 1):
    if value == ord('e') or value == ord('q'):
        continue
    print("{:s}".format(chr(value)), end='')
