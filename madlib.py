import re

welcome = 'Hello and welcome to my madlib!'

print(welcome)


def read_file(path):
    try:
        with open(path, 'r') as f:
            content = f.read()
            print(content)
    except:
        return 'hello'


def extract(s):
    start = s.find('{')
    if start == -1:
        # No opening bracket found. Should this be an error?
        return ''
    start += 1  # skip the bracket, move to the next character
    end = s.find('}', start)
    if end == -1:
        # No closing bracket found after the opening bracket.
        # Should this be an error instead?
        return s[start:]
    else:
        return s[start:end]


names = []
for line in ('lib.txt'):
    names.append(extract(line))


filename = input("filename: ")


with open(filename, "a") as f:
    f.write(input())

read_file('lib.txt')
# write_file('lib.txt', 'yooooo')
