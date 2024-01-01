from pathlib import Path

directory=Path('Home').joinpath("dir1/dir2/dir2/dummy.txt")
print(directory)
directory=Path.home().joinpath("dir1/dir2/dir2/dummy.txt")
print(directory)
directory=Path.home().joinpath("dir1","dir2","dir3","dummy.txt")
print(directory)
dirs=["dir1","dir2","dir3","dummy.txt"]
directory=Path.home().joinpath(*dirs)
print(directory.exists())
print(directory)
print(directory.parts)
print(str(directory))
print(directory.parent)
par=directory.parent
print(par.parent)
print(par.name)
print(directory.name)
print(directory.suffix)
part=Path.home()/'pathlib_module'
print(part)
print(part.name)
print(part.suffix)

# Home/dir1/dir2/dir2/dummy.txt
# /home/pganalytics/dir1/dir2/dir2/dummy.txt
# /home/pganalytics/dir1/dir2/dir3/dummy.txt
# False
# /home/pganalytics/dir1/dir2/dir3/dummy.txt
# ('/', 'home', 'pganalytics', 'dir1', 'dir2', 'dir3', 'dummy.txt')
# /home/pganalytics/dir1/dir2/dir3/dummy.txt
# /home/pganalytics/dir1/dir2/dir3
# /home/pganalytics/dir1/dir2
# dir3
# dummy.txt
# .txt
# /home/pganalytics/pathlib_module
# pathlib_module
