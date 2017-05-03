#!/usr/bin/env python

""" Sort all text files in the directory """
import subprocess


def main():
    print("Sorting all files in the dir.")

    import os
    textfiles = [f for f in os.listdir(".") if f.endswith(".txt")]

    for f in textfiles:
        print('Sorting {}'.format(f))
    # sort -u -o adjectives_negative.txt adjectives_negative.txt

    cmd = ['sort', '-u', '-o', f, f]

    try:
        p = subprocess.Popen(cmd)
        p.wait()
        return True
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False

if __name__ == "__main__":
    main()
