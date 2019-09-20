import fasttext
import pandas as pd
# select tag you want to type
tag = 'Epic'

print(tag)
def training_model(tag):
    training_file = "../Files/training_" + tag + ".txt"

    model = fasttext.train_supervised(input=training_file, lr=0.5, epoch=25,
                                      wordNgrams=2, bucket=200000, dim=50, loss='ova')
    model.save_model("../Model/model_" + tag + ".bin")

def Tagid():
    df_tag = pd.read_csv('../Files/' + tag + 'TagID.csv')
    return(df_tag.to_dict()[tag])


def predict(userstory):
    model_file = '../Model/model_'+ tag + '.bin'

    classifier = fasttext.load_model(model_file)       # laod model
    label = classifier.predict(userstory)
    label = int(label[0][0].replace('__label__', ''))
    dic = Tagid()
    return(dic[label])

a = predict("As a CSR, Sales Rep, Plant Rep, RQM or Transportation Rep I would like to be able to Search for a customer contact---so that I can Track the customer involved in the complaint so I know who to contact with questions or")
print(a)