# File READER Function
def mad_read(path):
  with open(path, 'r') as madreader:
    return madreader.read()

# Function that CREATES a file
def mad_write(path, value):
  with open(path, 'w') as madwriter:
    return madwriter.write(value)

# Function that REPLACES all the fillers for {}
def replacement():
   template_content = mad_read('template.txt')
   finished_product = template_content.replace("{Adjective}", "{}").replace("{A First Name}", "{}").replace("{Plural Noun}", "{}").replace("{Past Tense Verb}", "{}").replace("{Large Animal}", "{}").replace("{Small Animal}", "{}").replace("{A Girl's Name}", "{}").replace("{Number}", "{}").replace("{First Name's}", "{}")
   return finished_product

# Function that SETS all the PARAMS for the questions
def value_setter(adj1, adj2, fn1, ptv1, fn2, adj3, adj4, pn1, la, sa, gn, adj5, pn2, adj6, pn3, n1, fn3, n2, pn4, n3, pn5):
  cleanscript = replacement()
  formattedscript = cleanscript.format(adj1, adj2, fn1, ptv1, fn2, adj3, adj4, pn1, la, sa, gn, adj5, pn2, adj6, pn3, n1, fn3, n2, pn4, n3, pn5)
  print(formattedscript)
  mad_write('funny.txt', formattedscript)
  return formattedscript

#Welcome message
star = ('*'*19)
half = ('*'*8)
print(f'{star}{star}{star}{star}')
print('')
print(f'{star}{(half)}Welcome to MADLIBS!{star}{half}')
print('')
print('To play the game you will be promped to enter a number of nouns, adjectives, verbs, (21 total)... ')
print('')
print('Follow those prompts to the end and a story will appear with all your answers!')
print('')
print('to EXIT the game at any time type "quit"')
print('')
print(f'{star}{star}{star}{star}')
print('')

#User INPUT
def user_input():
  while True:
    adj1 = input(str('Enter an Adjective: '))
    adj2 = input(str('Enter an Adjective: '))
    fn1 = input(str('First name: '))
    ptv1 = input(str('Past Tense Verb: '))
    fn2 = input(str('First name: '))
    adj3 = input(str('Enter an Adjective: '))
    adj4 = input(str('Enter an Adjective: '))
    pn1 = input(str('Plurl noun: '))
    la = input(str('Large Animal: '))
    sa = input(str('Small Animal: '))
    gn = input(str('Girls name: '))
    adj5 = input(str('Enter an Adjective: '))
    pn2 = input(str('Plurl noun: '))
    adj6 = input(str('Enter an Adjective: '))
    pn3 = input(str('Plurl noun: '))
    n1 = input(str('Number 1-50: '))
    fn3 = input(str('First name: '))
    n2 = input(str('Number: '))
    pn4 = input(str('Plurl noun: '))
    n3 = input(str('Number: '))
    pn5 = input(str('Plurl noun: '))

    print(f'{star}{star}{star}{star}')

    value_setter(adj1, adj2, fn1, ptv1, fn2, adj3, adj4, pn1, la, sa, gn, adj5, pn2, adj6, pn3, n1, fn3, n2, pn4, n3, pn5)

    break

user_input()

print(f'{star}{star}{star}{star}')
print(f'{star}{star}{star}{star}')
print(f'{star}{star}{star}{star}')
print(f'{star}THANKS FOR PLAYING! HAVE A JOYFUL DAY!{star}')
print(f'{star}{star}{star}{star}')
print(f'{star}{star}{star}{star}')
print(f'{star}{star}{star}{star}')