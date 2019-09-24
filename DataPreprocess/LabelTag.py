import pandas as pd

df = pd.read_excel('/Users/zlu024/Documents/project/USTag/Files/SFDC Projects Case Requirements Analysis - V2.xlsx')

TagName = ['Capability', 'Sub-Capability', 'Epic']

for tag in TagName:
    res = []
    for i in df[tag]:
        if isinstance(i, str):
            if i not in res:
                res.append(i)
    # dataframe = pd.DataFrame(list(zip(range(len(res)),res)),
    #                          columns = ['TagID', 'Capability'])
    dataframe = pd.DataFrame(res, columns = [tag])
    dataframe.index.name = 'TagID'
    dataframe.to_csv('/Users/zlu024/Documents/project/USTag/Files/' + tag +'TagID.csv')
