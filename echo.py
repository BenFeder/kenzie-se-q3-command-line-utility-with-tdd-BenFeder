#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Benjamin Feder"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument('-u', '--upper', action="store_true",
                        help="convert text to uppercase")
    parser.add_argument('-l', '--lower', action="store_true",
                        help="convert text to lowercase")
    parser.add_argument('-t', '--title', action="store_true",
                        help="convert text to titlecase")
    parser.add_argument('text', help="text to be manipulated")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    if ns.upper:
        text_to_print = ns.text.upper()
    if ns.lower:
        text_to_print = ns.text.lower()
    if ns.title:
        text_to_print = ns.text.title()
    if not ns.upper and not ns.lower and not ns.title:
        text_to_print = ns.text
    print(text_to_print)


if __name__ == '__main__':
    main(sys.argv[1:])
