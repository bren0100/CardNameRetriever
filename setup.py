import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"]}
                     
includes = ['re', 'os', 'json', 'fnmatch']

setup(name='ConvertDeckToTextFile',
     version='0.1',
      author='Nicholas Brennan',
     description='Convert a .json file from tabletop simulator to a text file with each individual card name',
     executables=[Executable("CardNameRetriever.py")]
     )