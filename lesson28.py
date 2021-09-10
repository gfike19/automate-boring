import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall("Agent Alice gave the secret documents to Agent Bob"))
# how to substitute text
print(namesRegex.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob"))