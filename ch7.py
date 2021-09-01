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
# mo.group() holds text that was found first
# print(mo.group())
print(phoneNumberRegex.findall(message))
# above will return list of all matches found

# match 1 or one times = ?
# batRegex = re.compile(r'Bat(wo)?man')
# mo = batRegex.search('The Adventures of Batman')
# print(mo.group())
# mo = batRegex.search('The Adventures of Batwoman')
# print(mo.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me'+
'tomorrow')
# above regex will work
# print(mo.group())
mo = phoneRegex.search('My phone number is 555-1234. Call me'+
'tomorrow')
# this one won't
# print(mo == None)

# to resolve, group first chunk and place ? beside it
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# print(phoneRegex.search('My phone number is 555-1234. Call me'+
# 'tomorrow'))

# * star aka wildcard matach 0 or more times
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group())