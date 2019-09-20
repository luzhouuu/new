import fasttext
import pandas as pd
# select tag you want to type
tags = ['Capability','Sub-Capability','Epic']

def training_model(tag):
    training_file = "../Files/training_" + tag + ".txt"

    model = fasttext.train_supervised(input=training_file, lr=0.5, epoch=250000,
                                      wordNgrams=2,loss='ova')
    #lr: learning rate
    #wordNgrams:  important for classification problems where word order is important, such as sentiment analysis.
    #'ova': handle multiple labels is to use independent binary classifiers for each label
    model.save_model("../Model/model_" + tag + ".bin")

def Tagid(tag):
    df_tag = pd.read_csv('../Files/' + tag + 'TagID.csv')
    return(df_tag.to_dict()[tag])


def predict(userstory, tag):
    model_file = '../Model/model_'+ tag + '.bin'

    classifier = fasttext.load_model(model_file)       # laod model
    label = classifier.predict(userstory)
    label = int(label[0][0].replace('__label__', ''))
    dic = Tagid(tag)
    return(dic[label])

print(predict("sdfa", 'Epic'))
#
# for tag in tags:
#     training_model(tag)