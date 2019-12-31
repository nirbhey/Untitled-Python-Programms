import re # re stands for regular expressions (regex).

'''
Identifiers: # These are the base rules or syntax for a specific expression(word, number, character, space, etc)

\d any number.
\D anything except a number.
\s space.
\S anything except a space.
\w any character.
\W anything except a space.
.  anything except a new line.
\b the whitespace around words
\. a .(period).

Modifiers: Description for identifiers.

{1, 3} we're expecting a length of 1 to 3, maybe of a word or a digit, only matter is that it's length will be b/w 1 to 3.
+ Match 1 or more.
? Match 0 or 1.
* Match 0 or more.
$ Match the end of a string.
^ Match the beginning of a string.
| OR
[] Range or variance, ex. [1-5a-qA-Z]
[x] expecting "x" amount

White space characters:

\n new line
\s space
\t tab
\e escape
\f form feed
\r return

Do'nt forget! :

. + * ? [ ] $ ^ ( ) { } | \

To use the above symbols, you always have to escape them from regex

'''

exampleString = '''
Nirbhey's greetings to the reader(s), my age is 21 years,
my mother Manveen is 56 years old and my sister Jessica is 24 years old,
my wife Vidhi is 20 years old, my wish is that each of the Pahwa family members lives more than 100 years of age.
'''

varAges = re.findall(r'\d{1,3}', exampleString)
varNames = re.findall(r'[A-Z][a-z]*', exampleString)

#print(varAges)
#print(varNames)

pahwaDict = {}
x = 0

for i in varNames:
    pahwaDict[varNames[x].lower()] = varAges[x]
    x += 1

#print(pahwaDict)

x = str(input('Which Pahwa family member \'s age do you want to know?' )).lower()

print(x. upper(),'\'s age is: ', pahwaDict[x])

try:
    re.compile(".*+")
    print("True")
except Exception as e:
    print("False")