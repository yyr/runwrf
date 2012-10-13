#!/usr/bin/env python
'''
  Read and manipulate the Fortran namelist files

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

class NameList(dict):
    """Read and Keep the Fortran namelist files.
    """

    def __init__(self, namelistfile):
        """

        Arguments:
        - `namelistfile`:
        """
        dict.__init__(self)
        self._namelistfile = namelistfile
        self._fileContent = open(namelistfile).read()
        self.

    def print_raw_content(self):
        return self._fileContent


def main():
    pass


if __name__ == '__main__':
    main()
