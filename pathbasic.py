from pathlib import Path

current=Path.cwd()
print(current)
current1=Path('.')
print(current1)
print(current1.absolute())
print(current==current1)              #False
print(current==current1.absolute())   #True
print(current.samefile(current1.absolute()))  #True
print(Path.home())


# /home/pganalytics/Documents/pathlib_module
# .
# /home/pganalytics/Documents/pathlib_module
# False
# True
# True
# /home/pganalytics