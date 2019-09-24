import pandas as pd
import nltk

def DataClean(df):
    temp = df['User Story']
    for x in range(len(temp)):
        tokens = nltk.word_tokenize(
            str(temp[x]).replace('\\', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' '))
        for n in range(len(tokens)):
            if tokens[n] == "'s":
                tokens[n] = 'is'
            if tokens[n] == "'t":
                tokens[n] = 'not'
            if tokens[n] == "'re":
                tokens[n] = 'are'
        if tokens[0] != 'nan':
            tagged = nltk.pos_tag(tokens)
            n = 0
            result = ''
            for i in range(0, len(tagged)):
                if tagged[i - n][1][0] != 'N' and tagged[i - n][1][0] != 'V':
                    del tagged[i - n]
                    n = n + 1
            for n in range(0, len(tagged)):
                result = result + tagged[n][0] + ' '
            temp[x] = result
    df = df[temp.isnull() != True]
    df = df[df['Capability'].isnull() != True]
    return df

def labeltxt(Tag, df):
    file = open('../Files/training_' + Tag + '.txt', 'w')
    tag = pd.read_csv('../Files/' + Tag + 'TagID.csv').to_dict()[Tag]
    tag = {b:a for a,b in tag.items()}

    def addlable(row):
        return '__label__' + str(tag[row])

    l = df[Tag].apply(lambda row: '__label__' + str(tag[row]))
    L =list(l + '\t' + df['User Story'] + '\n')

    file.writelines(L)
    file.close()

if __name__ == "__main__":
    df = pd.read_excel('../Files/SFDC Projects Case Requirements Analysis - V2.xlsx',
                       sheet_name='User Stories')
    df = DataClean(df)
    labeltxt('Sub-Capability', df)