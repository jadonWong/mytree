#！/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Usage:
  mytree <dirname>
  mytree (-h | --help)

Options:
  -h  --help    Show this screen
"""

import os
from docopt import docopt


def mytree(dirpath, level=1):
    listandfile = os.listdir(dirpath)
    for one in listandfile:
        print("|   " * level)
        print("|   " * (level-1) + "|---" + one)
        one_path = dirpath + '/' + one
        if os.path.isdir(one_path):
            mytree(one_path, level + 1)

            
def main():
    args = docopt(__doc__, version='mytree')
    dirpath = "./" + args['<dirname>']
    print(args['<dirname>'])
    mytree(dirpath)

if __name__=='__main__':
    main()


    
