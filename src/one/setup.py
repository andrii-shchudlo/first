 
from setuptools import setup, find_packages

setup(
    name = "one",
    version = "1.0",
    license = 'BSD',
    description = "A short URL handler for Django apps.",
    author = 'Andrii',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
    entry_points = """\
      [console_scripts]
      one_exec = one.main:main
      """
)
