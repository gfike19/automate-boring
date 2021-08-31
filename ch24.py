import re

message = "call me at 314-967-5309, or at 314-555-5555"
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search(message)

#  print mo.group() will return entire pattern found
# print mo.group(1) will return first pattern found 
# due to parentheses, putting in different number will grab
# different part of message

# print(mo.group(1))
# in order to find () specifally put backlash before it

# use of | (pipe character) shown below
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

# match object will have value of none if no matches are found
# using group will show which pattern in () was found
# mo.group() or mo.group(0) will return whole string
