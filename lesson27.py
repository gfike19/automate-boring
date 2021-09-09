#  indicates where pattern should be found at
import re 

# example of ^ (not)
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello world!'))
print(beginsWithHelloRegex.search('He said "Hello!"') == None)

endsWithWorldRegex = re.compile(r'world!$')
print(beginsWithHelloRegex.search('Hello world!') != None)
print(beginsWithHelloRegex.search('Hello world!lorem ipsum'))
# ^ and $ present = pattern must match entire string

allDigitsRegex = re.compile(r'^\d+$')