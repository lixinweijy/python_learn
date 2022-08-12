# -*- coding:utf-8 -*-
import sys
print("dsa" ,sep=" ",end="",file=sys.stdout,flush=False)


def print(self, *args, sep=' ', end='\n', file=None):  # known special case of print
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    pass