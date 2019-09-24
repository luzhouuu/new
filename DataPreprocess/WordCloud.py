import pandas as pd
import data
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_excel('../Files/SFDC Projects Case Requirements Analysis - V2.xlsx',
                       sheet_name='User Stories')
#
# def ToTxt(df):
#     file = open('../Files/row_data.txt', 'w')
#     tag = pd.read_csv('../Files/' + Tag + 'TagID.csv').to_dict()[Tag]
#     tag = {b:a for a,b in tag.items()}
#
#     def addlable(row):
#         return '__label__' + str(tag[row])
#
#     l = df[Tag].apply(lambda row: '__label__' + str(tag[row]))
#     L =list(l + '\t' + df['User Story'] + '\n')
#
#     file.writelines(L)
#     file.close()



text = open('/Users/zlu024/Documents/project/USTag/Files/training_Epic.txt').read()
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()