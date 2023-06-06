#!/usr/bin/python3
i = 1
for char in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        print('{:s}'.format(chr(char).upper()), end='')
    else:
        print('{:s}'.format(chr(char)), end='')
    i += 1
