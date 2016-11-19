#! /usr/bin/env python3

"""
grep.py unix grep-like utility

Usage: grep.py PATTERN FILE

"""
import os
import re
import subprocess
import sys
import fnmatch


def grep_file(filename, search_regex):
    with open(filename, 'r') as f:
        for line_nr, line in enumerate(f.readlines()):
            if search_regex.search(line):
                print('{}:{}:{}'.format(filename, line_nr+1, line.strip()))


def matching_files(file_pattern):
    # Convert a shell-style pattern to a regular expression
    regex_file_pattern = fnmatch.translate(file_pattern)
    file_regex = re.compile(regex_file_pattern)

    files = [file.name
             for file in os.scandir('.')
             if file.is_file()
             and file_regex.match(file.name)]
    return files


def main():
    search_pattern = sys.argv[1]
    search_regex = re.compile(search_pattern)
    file_pattern = sys.argv[2]

    files = matching_files(file_pattern)
    for filename in files:
        grep_file(filename, search_regex)


if __name__ == '__main__':
    main()
