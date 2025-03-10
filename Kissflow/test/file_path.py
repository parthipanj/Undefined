from os import path, getcwd

print(getcwd())
realpath = path.realpath(__file__)
basepath = path.dirname(__file__)
filepath = path.abspath(__file__)

from pathlib import Path

print("File      Path:", Path(__file__).absolute())
print("Directory Path:", Path().absolute())

print("")
