import os
import pathlib
import subprocess

os.chdir(pathlib.Path(os.path.dirname(__file__)) / '..')

def build():
    print(pathlib.Path('.').absolute())
    subprocess.run(['make', 'clean'])
    subprocess.run(['make', 'html'])
