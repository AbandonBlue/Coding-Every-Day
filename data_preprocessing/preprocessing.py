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