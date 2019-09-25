import fasttext
import pandas as pd

tags = ['Capability','Sub-Capability','Epic']
tag = tags[1]

print(tag)
def training_model(tag, e = 20, prefix = None):
    if prefix != None:
        training_file = "../Files/txtfiles/" + str(prefix) + tag + ".txt"
        model = fasttext.train_supervised(input=training_file, lr=0.5, epoch=e, loss='ova')
        model.save_model("../Model/model_" + str(prefix) + tag + ".bin")
    else:
        training_file = "../Files/txtfiles/" + tag + ".txt"
        model = fasttext.train_supervised(input=training_file, lr=0.5, epoch=e, loss='ova')
        model.save_model("../Model/model_" + tag + ".bin")

def Tagid(tag):
    df_tag = pd.read_csv('../Files/' + tag + 'TagID.csv')
    return(df_tag.to_dict()[tag])

# def int_to_tag(Tag):
#     tag = pd.read_csv('../Files/' + Tag + 'TagID.csv').to_dict()[Tag]
#     return tag # type dict

def predict(userstory, tag, prefix = None):
    if prefix != None:
        model_file = '../Model/model_'+ str(prefix) + tag + '.bin'
    else:
        model_file = '../Model/model_'+ tag + '.bin'
    classifier = fasttext.load_model(model_file)       # load model
    label = classifier.predict(userstory)
    label = int(label[0][0].replace('__label__', ''))
    dic = Tagid(tag)
    return(dic[label])

def get_tagId(taglabel, tag):
    tag_file = pd.read_csv('../Files/' + tag + 'TagID.csv')
    return int(tag_file[tag_file[tag] == taglabel]['TagID'])

if __name__ == "__main__":
    training_model(tags[0])
    training_model(tags[1], prefix=0)
    training_model(tags[1], prefix=1)