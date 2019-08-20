example_chara = 'I am an NLPer'
example_word = example_chara.split()


def create_ngram(target, n):
    len_sent = len(target)
    assert 0 < n <= len_sent, 'Invalid "n"'
    result = []
    
    for i in range(len_sent-n+1):
        result.append(target[i:i+n])
    return result


result_chara_ngram = create_ngram(example_chara, 2)
print(result_chara_ngram)

result_word_ngram = create_ngram(example_word, 2)
print(result_word_ngram)
