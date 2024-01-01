from pathlib import Path
from datetime import datetime

with open("dummy.txt",'w') as f:
    f.write("File is created for testing")
path=Path('dummy.txt')
print(path)
print(path.absolute())
file_stat=path.stat()
print(file_stat)
print(file_stat.st_size)
print(file_stat.st_mtime)
time=datetime.fromtimestamp(file_stat.st_mtime)
print(time)
print(path.exists())
exist=Path("/home/pganalytics/Documents/pathlib_module/dummy.txt").exists()
print(exist)
print(Path('dummy.txt').is_dir())
print(Path("dummy.txt").is_file())
print(Path("/home/pganalytics/Documents/pathlib_module/dummy.txt").is_dir())
print(Path("/home/pganalytics/Documents/pathlib_module/dummy.txt").is_file())
print(Path("/home/pganalytics/Documents/pathlib_module").is_dir())
print(Path("/home/pganalytics/Documents/pathlib_module").is_file())


# dummy.txt
# /home/pganalytics/Documents/pathlib_module/dummy.txt
# os.stat_result(st_mode=33204, st_ino=10392945, st_dev=2056, st_nlink=1, st_uid=1000, st_gid=1000, st_size=27, st_atime=1704089655, st_mtime=1704105671, st_ctime=1704105671)
# 27
# 1704105671.4150076
# 2024-01-01 16:11:11.415008
# True
# True
# False
# True
# False
# True
# True
# False