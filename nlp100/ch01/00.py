example = list('stressed')

len_example = len(example)
for i in range(len_example//2):
    example[i], example[-1-i] = example[-1-i], example[i]

print(''.join(example))

"""Answer2
print(''.join(reversed(example)))
"""

