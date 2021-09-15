import os

# how to create file path string for any os
print(os.path.join('folder1', 'folder2','folder3','image.png'))
# os.cwd = pwd
# os.chdir(new path) = change directory
# absolute paths contain root directory
# relative paths do not
print(os.path.abspath("lesson30.py"))
# above returns absolute path of parameter
# os.path.isabspath(path) returns boolean determining if path is absolute or not
# os.path.relpath(path, starting point) returns relative path from starting point
# os.path.dirname(path) will return all folders in path
# os.path.basename(path) will return item that is at the end of the path
# os.path.exists(path) boolean method that is self explanatory
# similarly there is os.path.isfile(path) os.path.isdir(path)
# 
