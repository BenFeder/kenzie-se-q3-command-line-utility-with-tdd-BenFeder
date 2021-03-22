#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Benjamin Feder"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description="creating argparse for echo")
    parser.add_argument('-u', '--upper', help="converts text to uppercase")
    parser.add_argument('-l', '--lower', help="converts text to lowercase")
    parser.add_argument('-t', '--title', help="converts text to titlecase")
    parser.add_argument('-h', '--help', help="shows usage message")
    parser.add_argument('text', help="positional arg 'text' to convert")
    ns = parser.parse_args()
    return ns


def main(args):
    """Implementation of echo"""
    if args.text and (args.u or args.upper):
        return args.text.upper()
    elif args.text and (args.l or args.lower):
        return args.text.lower()
    elif args.text and (args.t or args.title):
        return args.text.title()
    elif args.text:
        return args.text
    else:
        print("""usage: echo.py [-h] [-u] [-l] [-t] text

Perform transformation on input text.

positional arguments:
    text         text to be manipulated

optional arguments:
    -h, --help   show this help message and exit
    -u, --upper  convert text to uppercase
    -l, --lower  convert text to lowercase
    -t, --title  convert text to titlecase""")


if __name__ == '__main__':
    main(sys.argv[1:])
