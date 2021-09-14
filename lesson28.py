import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall("Agent Alice gave the secret documents to Agent Bob"))
# how to substitute text
print(namesRegex.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob"))

# how get first letter so instead of redacted print agent a
namesRegex = re.compile(r'Agent (\w)\w*')
# \w* will just return the whole name
# namesRegex = re.compile(r'Agent (\w)')
print(namesRegex.findall("Agent Alice gave the secret documents to Agent Bob"))
# line 9 is needed to convert Agent Alice to Agent A, \1 points to first argument, \w* fill it in
print(namesRegex.sub(r'Agent \1****', "Agent Alice gave the secret documents to Agent Bob"))
# below will replace Agent and their name but space still remains
print(namesRegex.sub(r'\0REDACTED', "Agent Alice gave the secret documents to Agent Bob"))
# re.verbost removes whitespace as part of the string
# so below the new line character won't be present
re.compile('''
\d\d\d
-
\d\d\d
-
\d\d\d\d''', re.VERBOSE)