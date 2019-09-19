import pandas as pd

file = open('/Users/zlu024/Documents/project/USTag/Files/training_Capability.txt', 'w')

df = pd.read_excel('/Users/zlu024/Documents/project/USTag/Files/SFDC Projects Case Requirements Analysis - V2.xlsx',
                   sheet_name='User Stories')

df = df[df['User Story'].isnull() != True]
df = df[df['Capability'].isnull() != True]

def clean_n(line):
    return line.replace('\n', '')

def clean_nn(line):
    return line.strip(' ').replace('\n', '').replace('\n', '')

df['User Story'] = df['User Story'].apply(clean_n)
df['User Story'] = df['User Story'].apply(clean_nn)




tag = pd.read_csv('/Users/zlu024/Documents/project/USTag/Files/CapabilityTagID.csv').to_dict()['Capability']
tag = {b:a for a,b in tag.items()}
print('pass 2')


def addlable(row):
    return '__label__' + str(tag[row])

l = df['Capability'].apply(addlable)
L =list(l + '\t' + df['User Story'] + '\n')

file.writelines(L)
file.close()