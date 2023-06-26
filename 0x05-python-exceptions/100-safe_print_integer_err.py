#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as va:
        print('Exception: {:s}'.format(str(va)), file=sys.stderr)
        return False
