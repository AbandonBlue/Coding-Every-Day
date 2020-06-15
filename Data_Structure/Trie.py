import nltk

# Recursion 's power

trie = nltk.defaultdict(dict)

def insert(trie, key, value):
    # base case
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first], rest, value)
    else:
        trie['value'] = value




insert(trie, 'chat', 'cat')
insert(trie, 'chien', 'dog')
insert(trie, 'chair', 'flesh')
insert(trie, 'chic', 'stylish')

trie = dict(trie)   # for nicer printing
print(trie)