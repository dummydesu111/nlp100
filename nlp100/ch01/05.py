example = 'I am an NLPer'


def create_ngram(sentence, n):
    len_sent = len(sentence)
    assert 0 < n <= len_sent, 'Invalid "n"'
    result = []
    
    for i in range(len_sent-n+1):
        result.append(sentence[i:i+n])
    return result


result = create_ngram(example, 2)
print(result)
