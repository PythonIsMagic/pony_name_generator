#!/usr/bin/env python

""" Sort all text files in the directory
    # sort -u -o adjectives_negative.txt adjectives_negative.txt
    -u: --unique
    -o FILE: Redirects to specified file
    -f: --ignore-case

    # tr '[:upper:]' '[:lower:]' < input.txt > output.txt
"""
import os
import subprocess


def sort_bash(textfiles):
    for f in textfiles:
        tr_cmd = ['tr', '[:upper:]', '[:lower:]', '<', f, '>', f]
        sort_cmd = ['sort', '-u', '-o', f, f]

        try:
            print('Converting all words to lowercase')
            p = subprocess.Popen(tr_cmd)
            p.wait()

            print('Sorting {}'.format(f))
            p = subprocess.Popen(sort_cmd)
            p.wait()
            print('')
        except OSError as e:
            print(e)


def sort_py(textfiles):
    for tf in textfiles:
        # Open our file and read it
        with open(tf, 'r') as f:

            # Read all the lines,
            lines = [line.lower().strip() for line in f]

            # Reduce them to unique items
            lines = list(set(lines))

            # Sort them!
            lines = sorted(lines)

        # Write to the same file.
        with open(tf, 'w') as out:
            out.writelines(lines)

if __name__ == "__main__":
    textfiles = [f for f in os.listdir(".") if f.endswith(".txt")]
    print("Sorting all .txt files in the dir.")

    # sort_bash(textfiles)
    sort_py(textfiles)
