import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# basic logging code
# add filename=name to above to log to a file
# logging.debug(msg) can be used to display time stamp, , and what is happening at whatever line of code the debug
# is at, fancier version of just using print statements
logging.disable(logging.CRITICAL)
# above disables all logging messages, faster than hunting for print messages, kinda
# CRITICAL is used as it is the highest logging level and so will disale everything that has a lower level
# see onenote notes for more
