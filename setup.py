from distutils.core import setup

setup(name='coins',
      version='0.0.1',
      description='A little command line tool for tracking cryptocurrency prices.',
      url='http://github.com/ptbrodie/coins',
      author='Patrick Brodie',
      long_description=open('README.md').read(),
      install_requires=[
          'requests==2.18.4',
          'termcolor==1.1.0'
      ],
      scripts=['bin/coins'])
