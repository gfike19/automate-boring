# everything but txt is binary file
# pickle = convert python file to binary
# shelf = local data storage when db is excessive, can be pickled (see above)

import shelve

shelfFile = shelve.open("mydata")
shelfFile["Thundercats"] = ["Lion-o", "Panthro", "Cheetara", "Tygra", "Wily Kit", "Wily Kat", "Jaga"]
shelfFile.close()
# shelf files behave like dictionaries and have similar methods
# need to typecast to list when printing and stuff