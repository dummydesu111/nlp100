example = 'Now I need a drink, alcoholic of course, ' + \
    'after the heavy lectures involving quantum mechanics.'
example.replace(',', '').replace('.', '')
words = example.split()

anser = [len(w) for w in words]
print(anser)
