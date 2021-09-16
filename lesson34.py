import os

test = os.walk("c\\:Users\\aerot\\coding")
# above returns a generator object
for folderName, subfolders, filenames in os.walk("c:\\Users\\aerot\\coding"):
    print("Folder name:")
    print(folderName)
    print("\nSubfolders: ")
    print(str(subfolders))
    print("\nFilenames:")
    print(str(filenames) + "\n***\n")

# subfolders and filenames are lists objects, folderName is a string
# folderName has only dirrname, need to combine with basename to do stuff, see lesson 34