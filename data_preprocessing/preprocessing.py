import nltk
from collections import defaultdict

def get_missing_ratio(df, percent):
    """
    Args:
        df: DataFrame
        percent: Number
    Return:
        columns: List, the columns over "percent"
    """
    max_length = max(list(map(lambda x: len(x), df.columns)))
    columns = []

    for column in df.columns:
        missing_rate = df[column].isna().sum() / df.shape[0] *100
        if missing_rate >= percent:
            columns.append(column)
        print(f'{column}: %{max_length}d' % missing_rate, '%')
    return columns


def get_reverse_dict(d, is_one_to_one=False):
    """
    Args: 
        d: Dict
        is_one_to_one: Bool
    Return:
        reversed_d: Dict, DefaultDict
    """
    if is_one_to_one:
        reversed_d = dict()
        for k, v in d.items():
            reversed_d[v] = k
    else:
        reversed_d = defaultdict(list)
        for k, v in d.items():
            reversed_d[v].append(k)
    
    return reversed_d