#!/usr/bin/env python3

import argparse
import logging

import psu

if __name__ == '__main__':
    # setup of command line parsing
    parser = argparse.ArgumentParser(prog='python skeleton', description='Python skeleton for demonstration', epilog="Now it's on you!")
    parser.add_argument('text', help='text to output')
    args = parser.parse_args()

    logging.warning(args.text)
    psu.test()
