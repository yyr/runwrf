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

class Namelist(dict):
    """Read and Keep the Fortran namelist files.
    """

    def __init__(self,lines,filename="<undefined>"):
        """
        Create a :class:`Namelist` object.

        """
        dict.__init__(self)
        self._filename = filename
        self._lines = lines
        self.update(self.parse())


    @property
    def lines(self):
        """
        Raw lines of Namelist file(s).

        >>> from runwrf import namelist
        >>> namelist.loads("").lines
        []

        """
        return self._lines


    def pprint(self):
        """
        Pretty print namelist
        """
        pass


    def _split_namelist_line(self,string):
        """ split a namelist line into parameter and values.

        """
        par = []
        val = []
        return [par,val]

    def parse(self):
        # re patterns
        varstring = r'\b[a-zA-Z][a-zA-Z0-9_]*\b'
        spaces = r'[\t\s]*'

        sectname = re.compile(r"^[\t\s]*&(" + varstring + r")[\t\s]*$")
        sectend = re.compile(r"^[\t\s]*/[\t\s]*$")

        nl = {}                 # this is going to returned
        sect= ''

        # split sections
        for line in [l.strip() for l in self._lines if not l.strip() == '']: # remove empty lines
            # print line
            if re.match(sectname,line):
                sect = re.sub(sectname,r"\1",line)
                nl[sect] = {
                    'raw' : [],
                    'par' : [{}]
                }
            elif re.match(sectend,line):
                sect = ''
            else:
                if sectname:
                    nl[sect]['raw'].append(line)


        # sections to parameters
        for sect in nl.keys():
            for line in self._split_namelist_line(nl[sect]['raw']):
                pass
        return nl

def parse_lines(lines,filename):
    """

    """
    return Namelist(lines,filename=filename)

def load(path):
    """
    Load namelist from a file.

    :type path: str
    :type path: namelist file path

    """
    namelistfile = codecs.open(path,encoding='utf8')
    filename = path
    return loadi((l.rstrip('\n') for l in namelistfile.readlines()),
                 filename=filename)


def loads(string, filename='<string>'):
    """
    Load namelist document from a string.

    :rtype: :class: runwrf.Namelist
    """
    return loadi(string.splitlines(),filename=filename)


def loadi(lines,filename='<lines>'):
    """
    Load configuration file.

    :type path: str or file-like.
    """
    return parse_lines(lines, filename=filename)

def main():
    """ path to namelist file
    """
    path = "namelist.input"
    return load(path)

if __name__ == '__main__':
    main()
