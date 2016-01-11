#!/usr/bin/env python

import pprint
import sys
import yaml


def get_yaml(file_name=None):
    """Basic function that returns a Python data structure from a YAML file.

    Parameters: File name of YAML file
    """

    if file_name is None:
        raise ValueError("No YAML file passed to function!")

    try:
        return yaml.load_all(open(file_name))
    except IOError:
        print('Oops! Check the name of the YAML file passed as an argument.')
        print('The file passed during execution does not appear to exist.')
        sys.exit()



def main():
    """Main method to iterate over data structures imported from YAML files.

    Parameters: None
    """
    if len(sys.argv) != 2:
        print('Oops! Might want to check your syntax!')
        print('You should run this example like this:')
        print('python {f} <NAME OF YAML FILE>'.format(f=__file__))
        sys.exit()
    else:
        _YAML_FILE = sys.argv[1]

    docs = get_yaml(_YAML_FILE)
    for doc in docs:
        print('Here is the Python data type:')
        print(type(doc))
        print('Here is the data:')
        pprint.pprint(doc)

if __name__ == '__main__':
    main()
