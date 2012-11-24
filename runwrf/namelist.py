#!/usr/bin/env python
'''
Read and manipulate the Fortran namelist files. Regexp based parsing.

Fotran namelist files are in the following pattern.

     &section1
        par = val
        par2 = val,val2
        ...
     /

     &section2
        par = val
        par4 = val,val2
        ...
     /

'''

import codecs

AUTHOR = "Yagnesh Raghava Yakkala"
WEBSITE = "http://yagnesh.org"
LICENSE ="GPL v3 or later"


import re

class NameList(dict):
    """Read and Keep the Fortran namelist files.
    """

    def __init__(self,lines,filename="<undefined>"):
        """
        Arguments:
        - `namelistfile`: file
        """
        dict.__init__(self)
        self._filename = filename
        self._lines = lines
        self.update(self.parse())

    def parse(self):
        # re patterns
        varstring = r'\b[a-zA-Z][a-zA-Z0-9_]*\b'
        spaces = r'[\t\s]*'

        sectname = re.compile(r"^[\t\s]*&(" + varstring + r")[\t\s]*$")
        sectend = re.compile(r"^[\t\s]*/[\t\s]*$")

        nl = {}                 # this is going to returned
        sect= ''

        for line in self._lines.split("\n+"):
            if re.match(secname,line):
                sect = re.sub(secname,r"\1",line)
                nl[sect] = {
                    'raw' : [],
                    'par' : [{}]
                }
            elif re.match(re.sub):
                pass



def parse_lines(lines,filename):
    """

    """
    return NameList(lines,filename=filename)

def load(path):
    """
    Load namelist from a file.

    :type path: str
    :type arg: namelist file path

    """
    namelistfile = codecs.open(path,encoding='utf8')
    filename = path
    return loadi((l.rstrip('\n') for l in namelistfile.readlines()),
                 filename=filename)


def loads(string, filename='<string>'):
    """
    Load namelist document from a string.

    :rtype: :class: runwrf.NameList
    """
    return loadi(string.splitlines(),filename=filename)


def loadi(lines,filename='<lines>'):
    """
    Load configuration file.

    :type path: str or file-like.
    """
    return parse_lines(lines, filename=filename)


def main():
    return load("./namelist.input")


if __name__ == '__main__':
    main()
