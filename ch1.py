# [] is a sequence not a list
for i in [0,1,2,3]:
    print(i)

# assign values from range to list/array
lst = list(range(0, 4))
print(lst)

# above useful for mapping large amount of numbers
print(list(range(0,101, 2)))

# multiple assignment operator
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition)

size, color, disposition = 'skinny', 'black', 'quiet'
print(size)
print(color)
print(disposition)

a = 'AAA'
b = 'BBB'
a, b = b, a
# values will be reversed