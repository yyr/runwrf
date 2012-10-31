from distutils.core import setup

import runwrf

package = 'runwrf'
version = '0.1'

setup(
    name='runwrf', version=runwrf.VERSION,
    description="run WRF model with out any crud",
    packages=[
        'runwrf',
        'runwrf.namelist',
        'runwrf.tests',
    ],
    author=runwrf.AUTHOR,
    author_email='hi@yagnesh.org',
    license=runwrf.LICENSE,
    url='http://github.com/yyr/runwrf',
    keywords='WRF, weather Research, Model',
    long_description = runwrf.__doc__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
    ],
)
