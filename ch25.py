import re

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