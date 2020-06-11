def stem(word):
    """
    Find stem like (a little different)
    ex: 
        pattern = r"^.*(?:ing|ly|ed|iout|ies|ive|es|s|ment)$"
        re.findall(pattern, 'processing')
    """
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'ed', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    # others
    return word



if __name__ == "__main__":
    pass