import os
import shutil

import sys, stat

path = "1.txt"
path2 = "DeleteThisFolder"
path3 = "FolderContainingFiles"
os.chmod(path2,stat.S_IXUSR)

try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")
else:
    print(path+" was deleted!")
finally:
    print('Done first...')
try:
    os.rmdir(path2)
except PermissionError:
    print("You do not have the permission to delete that!")
except FileNotFoundError:
    print("That folder was not found")
else:
    print(path2+" was deleted!")
finally:
    print('Done second..')

try:
    shutil.rmtree(path3)    # Be careful with this function. It will delete everything within a directory!

except FileNotFoundError:
    print("That folder(s) were not found")
except OSError:
    print("This folder contains files! Cannot delete!")
else:
    print(path3+" was deleted!")
finally:
    print('Done third.')