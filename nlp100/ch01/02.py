example1 = 'パトカー'
example2 = 'タクシー'

result = ''
for ex1_val, ex2_val in zip(example1, example2):
    result += f'{ex1_val}{ex2_val}'

print(result)