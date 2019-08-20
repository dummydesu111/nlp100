example = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. ' + \
    'New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
example = example.replace(',', '').replace('.', '')
words = example.split()

one_char = {1, 5, 6, 7, 8, 9, 15, 16, 19}

answer = {}
for i, word in enumerate(words):
    key = ''
    if i+1 in one_char:
        key += word[0]
    else:
        key += word[:2]
    answer[key] = i + 1

print(answer)