#  indicates where pattern should be found at
import re
import random

# example of ^ (not)
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello world!'))
print(beginsWithHelloRegex.search('He said "Hello!"') == None)

endsWithWorldRegex = re.compile(r'world!$')
print(beginsWithHelloRegex.search('Hello world!') != None)
print(beginsWithHelloRegex.search('Hello world!lorem ipsum'))
# ^ and $ present = pattern must match entire string

allDigitsRegex = re.compile(r'^\d+$')
# below will return a match
print(allDigitsRegex.search(str(random.randint(1,1000000000000000000000))))
# the following won't
num1 = str(random.randint(1,1000000))
num2 = str(random.randint(1,1000000))
print(allDigitsRegex.search(num1 + 'x' + num2))

# . = any character except for the newline
atRegex = re.compile(r'.at')
print(atRegex.findall('the cat in the hat sat on the flat mat'))

# doesn't print flat as it was looking for only one preceeding character
# following resolves this but also returns white spaces
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('the cat in the hat sat on the flat mat'))

atRegex = re.compile(r'.*at')
print(atRegex.findall('the cat in the hat sat on the flat mat'))

# following kind of solves it though this wouldn't for input where we don't know what hard coded text is being sent
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall("First Name: Ada Last Name: Lovelace"))

# .* by default is greedy, to make it not greedy .*?
serve = "<To serve humans> for dinner.>"
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

# how to incorporate new line character into regex
prime = "Serve the public trust.\nProtect the innocent.\nUphold the law.\n"
# below won't print new line
dotStar = re.compile(r'.*')
print(dotStar.findall(prime))
# this one will though
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar(prime))

# re.IGNORECASE = self explanatory