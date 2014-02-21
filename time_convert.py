#!/bin/env python
#-*-coding:utf-8-*-
#converting between time string and timestamp
import argparse
import time
import sys
from datetime import datetime


def str2stamp(timestr, fmt):
    if not fmt:
        fmt = '%Y%m%d'
    return str(int(time.mktime(
        datetime.strptime(timestr, fmt).timetuple())))


def stamp2str(timestamp, fmt):
    if not fmt:
        fmt = '%Y-%m-%d %H:%M:%S'
    return datetime.fromtimestamp(timestamp).strftime(fmt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='convert between formated time string between timestamp')
    parser.add_argument('-f', '--format', type=str, help='time format')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--timestamp', nargs=1, type=int,
                       help='timestamp')
    group.add_argument('-s', '--timestr', nargs=1, type=str,
                       help='formated time string')
    args = parser.parse_args()
    fmt = args.format
    if args.timestr:
        result = str2stamp(args.timestr[0], fmt)
    elif args.timestamp:
        result = stamp2str(args.timestamp[0], fmt)
    else:
        result = str(int(time.time()))
    sys.stdout.write(result + '\n')
