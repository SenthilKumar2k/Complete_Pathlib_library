from pathlib import Path

with open('dummy.txt') as f:
    print(f.readlines())
p=Path.cwd()/'dummy.txt'
with open(p) as f:
    print(f.readlines())
print(p.exists())
p=Path.cwd()/'text.txt'
print(p.exists())
"""p.mkdir()         # create the unexisted file
print(p.exists())
try:                  # try to recreate the file to know the error
    p.mkdir()
except FileExistsError as ex:
    print(ex)"""

"""p.rmdir()           # delete the existed file
print(p.exists())
try:                   # try to delete the unexisted file
    p.rmdir()
except FileNotFoundError as ex:
    print(ex)"""


# ['File is created for testing']
# ['File is created for testing']
# True
# False