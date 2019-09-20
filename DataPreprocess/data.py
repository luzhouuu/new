import pandas as pd

def labeltxt(Tag):
    if not isinstance(Tag, str):
        return 'Input type should be string'
    file = open('../Files/training_' + Tag + '.txt', 'w')

    df = pd.read_excel('../Files/SFDC Projects Case Requirements Analysis - V2.xlsx',
                       sheet_name='User Stories')

    df = df[df['User Story'].isnull() != True]
    df = df[df['Capability'].isnull() != True]

    def clean_n(line):
        return line.replace('\n', '')

    def clean_nn(line):
        return line.strip(' ').replace('\n', '').replace('\n', '')

    df['User Story'] = df['User Story'].apply(clean_n)
    df['User Story'] = df['User Story'].apply(clean_nn)

    tag = pd.read_csv('../Files/' + Tag + 'TagID.csv').to_dict()[Tag]
    tag = {b:a for a,b in tag.items()}
    print('pass 2')


    def addlable(row):
        return '__label__' + str(tag[row])

    l = df[Tag].apply(addlable)
    L =list(l + '\t' + df['User Story'] + '\n')

    file.writelines(L)
    file.close()


labeltxt('Epic')