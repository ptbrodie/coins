from distutils.core import setup

setup(name='pycoins',
      version='0.0.4',
      description='A little command line tool for tracking cryptocurrency prices.',
      url='http://github.com/ptbrodie/coins',
      author='Patrick Brodie',
      author_email='ptbrodie@gmail.com',
      long_description=open('./README.md').read(),
      install_requires=[
          'requests==2.18.4',
          'termcolor==1.1.0'
      ],
      scripts=['./coins'])
