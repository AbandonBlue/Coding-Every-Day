def stem(word):
    """
    Find stem like (a little different)

    ex: 
        pattern = r"^.*(?:ing|ly|ed|iout|ies|ive|es|s|ment)$"
        re.findall(pattern, 'processing')
    """
    word = word.lower()    # lower first 
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'ed', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    # others
    return word


def segment(text, segs):
    """
    Use '1' to segment sentences

    ex: 
        text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
        seg1 = "0000000000000001000000000010000000000000000100000000000"
        segment(text, seg1) ---> ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
    """
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:])
    return words


def evaluate(text, segs):
    """
    To evaluate the score of seg.
    less score means better seg.
    ref: (Brent & Cart-wright, 1995)
    """
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    return text_size + lexicon_size


# 模擬退火算法的非確定性搜尋
from random import randint

def flip(segs, pos):
    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]


def flip_n(segs, n):
    for i in range(n):
        segs = flip(segs, randint(0,len(segs)-1))
    return segs


def anneal(text, segs, iterations, cooling_rate):
    temperature = float(len(segs))
    while temperature > 0.5:
        best_segs, best = segs, evaluate(text, segs)
        for i in range(iterations):
            guess = flip_n(segs, int(round(temperature)))
            score = evaluate(text, guess)
            if score < best:
                best, best_segs = score, guess
        score, segs = best, best_segs
        temperature = temperature / cooling_rate
        print(evaluate(text, segs), segment(text, segs))
    print()
    return segs





if __name__ == "__main__":
    pass