import re

# match the before group 0 or one times = ?
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex.search('My phone number is 415-555-1234. Call me'+
'tomorrow')