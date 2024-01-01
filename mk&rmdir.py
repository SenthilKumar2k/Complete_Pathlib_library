from pathlib import Path

p=Path.cwd()
print(p)
p=Path.cwd()/"dir1/dir2"
p.mkdir(parents=True)
print(p)
print(p.exists())


# /home/pganalytics/Documents/pathlib_module
# /home/pganalytics/Documents/pathlib_module/dir1/dir2
# True