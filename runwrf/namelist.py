#!/usr/bin/env python
'''
  Read and manipulate the Fortran namelist files. Regexp based parsing.

  Fotran namelist files are in the following pattern.

________________________________________________________________
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
________________________________________________________________

'''

AUTHOR = "Yagnesh Raghava Yakkala"
WEBSITE = "http://yagnesh.org"
LICENSE ="GPL v3 or later"


import re

class NameList(dict):
    """Read and Keep the Fortran namelist files.
    """

    def __init__(self, namelistfile):
        """
        Arguments:
        - `namelistfile`: file
        """
        dict.__init__(self)
        self._namelistfile = namelistfile
        self._fileContent = open(namelistfile).read()
        self.update(self.parse())

    def parse(self):
        # re patterns
        varstring = r'\b[a-zA-Z][a-zA-Z0-9_]*\b'
        spaces = r'[\t\s]*'

        sectname = re.compile(r"^[\t\s]*&(" + varstring + r")[\t\s]*$")
        sectend = re.compile(r"^[\t\s]*/[\t\s]*$")

        nl = {}                 # this is going to returned
        sect= ''

        for line in self._fileContent.split("\n+"):
            if re.match(secname,line):
                sect = re.sub(secname,r"\1",line)
                nl[sect] = {
                    'raw' : [],
                    'par' : [{}]
                }
            elif re.match(re.sub)


def main():
    nl = NameList("./namelist.input")
    print "\n".join(nl)

if __name__ == '__main__':
    main()
