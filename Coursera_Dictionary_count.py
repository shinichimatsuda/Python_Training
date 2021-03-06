##### Count new words in dictionary¶

counts = dict()
names = ['Ichiro','Matsui','Sasaki','Kuroda']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

## output: {'Matsui': 1, 'Ichiro': 1, 'Kuroda': 1, 'Sasaki': 1}


##### The get method for dictionary

if name in counts:
    print(counts[name])
else:
    print(0)

## output: 1

print(counts.get(name,0)) # here, 0 is a default value if key dose not exist (and no Traceback). Very valuable!

## output: 1

##### Counting words

counts = dict()
print('Enter a line of text:')
line = input('')

## out: Enter a line of text: Python String split() Method - Learning Python in simple and easy steps : A beginner's tutorial containing complete knowledge of Python Syntax Object Oriented Language, Methods, Tuples, Tools/Utilities, Exceptions Handling, Sockets

words = line.split()
print('Words:', words)

## out: Words: ['Python', 'String', 'split()', 'Method', '-', 'Learning', 'Python', 'in', 'simple', 'and', 'easy', 'steps', ':', 'A', "beginner's", 'tutorial', 'containing', 'complete', 'knowledge', 'of', 'Python', 'Syntax', 'Object', 'Oriented', 'Language,', 'Methods,', 'Tuples,', 'Tools/Utilities,', 'Exceptions', 'Handling,', 'Sockets']
In [23]:

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts',counts)

## out: Counting...
Counts {'A': 1, 'of': 1, 'complete': 1, 'Syntax': 1, 'Handling,': 1, 'in': 1, 'Sockets': 1, "beginner's": 1, 'Oriented': 1, 'Methods,': 1, 'steps': 1, 'knowledge': 1, 'simple': 1, 'Tuples,': 1, 'easy': 1, 'and': 1, 'split()': 1, 'String': 1, 'Python': 3, ':': 1, 'Learning': 1, 'Language,': 1, 'Object': 1, 'Exceptions': 1, 'tutorial': 1, 'Method': 1, 'containing': 1, 'Tools/Utilities,': 1, '-': 1}
