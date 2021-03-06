# 314-867-5309
# 012345678901

# example of how much code is needed to verify number without regex (doesn't work)
# def isPhoneNumber(text):
#     if(len(text) != 12):
#         return False
#     for each in text:
#         if text.index(each) != 3 or text.index(each) != 7:
#             if each.isdecimal() == False:
#                 return False
#         else:
#             if each == '-':
#                 break

# print(isPhoneNumber('314-867-5309'))
# more code would be needed to apply this to a larger chunk of code we wanted to look through for phone numbers

import re

message = "call me at 314-967-5309, or at 314-555-5555"
phoneNumberRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
# mo stands for match object
mo = phoneNumberRegex.search(message)
mo.group() 
# holds text that was found first
print(mo.group())
print(phoneNumberRegex.findall(message))
# above will return list of all matches found

# The ? says the group matches zero or one times.
# The * says the group matches zero or more times.
# The + says the group matches one or more times.
# The curly braces can match a specific number of times.
# The curly braces with two numbers matches a minimum and maximum number of times.
# Leaving out the first or second number in the curly braces says there is no minimum or maximum.
# Putting a question mark after the curly braces makes it do a nongreedy/lazy match.
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me'+
'tomorrow')
# above regex will work
print(mo.group())
mo = phoneRegex.search('My phone number is 555-1234. Call me'+
'tomorrow')
# this one won't
print(mo == None)

# to resolve, group first chunk and place ? beside it
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
print(phoneRegex.search('My phone number is 555-1234. Call me'+
'tomorrow'))

# * star = matach 0 or more times
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group())

# curly braces used for specific amount
haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said "HaHaHa'))
# above returns true

# can add in a second number for a range
haRegex = re.compile(r'(Ha){3,5}')
print(haRegex.search('He said "HaHaHaHa') != None)
# works like slicing
# eg {3,} has no upper bound (limit) to how many instances of the
# regex can be found
# by default regex in python is "greedy" = tries to match as much
# as possible
# "non greedy" match = {range here}?

# r' = raw string
# below will return all matches found, assigned to a variable will be
# a list of strings
# regex.search() only returns match objects
# regex.search() with groups inside will return list with tuples
# broken down by group

# [] = same as char|char|char
# [a-fA-F] = ranges of chars that valid for expression
# create own character class (not druid, paladin, etc)
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food'))
# adding {2} to the end of regex will return only when two of the characters in the regex are found together
# ^ = not
