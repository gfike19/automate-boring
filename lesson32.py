import shutil

# shutil contians copy, paste function
# below will return new path with file at end
print(shutil.copy("spam.txt", "c:\\Users\\aerot\\Desktop"))
# can also rename file with same function (similar to cp command)
# shutil.coptree(file-path-to-folder, destination) to move 
# entire folder, can also rename folder with same command
# mv = shutil.move(current-path, destination-path)
# no built in rename command, just rename like when using mv
