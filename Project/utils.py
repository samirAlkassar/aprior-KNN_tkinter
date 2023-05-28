def make_pattern(row:str):
    x = [i for i in row.split(',')]
    x = [i.replace(" ",'') for i in x]
    return x
def make_dic(df):
    dic = {}
    for id in range(len(df)):
        items = df['items'][id]
        dic[id] = make_pattern(items)

    return dic 