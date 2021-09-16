import os
import shutil

# os.unlink(file) = rm fileName
# os.rmdir(folder) = rmdir, folder must be empty
# shutil.rmtree(folder) = rm -rf
# commands are like unix, permanent
# send2trash = self explanatory module, requires pip install

import send2trash
send2trash.send2trash("spam.txt")