import fasttext
import pandas as pd
import os

CURR_PATH = os.path.dirname(__file__)
TAG_PATH = os.path.dirname(CURR_PATH) #获得d所在的目录,即d的父级目录



def get_tagsystem():
    print(TAG_PATH)
    df_tagsystem = pd.read_csv(TAG_PATH+ "/Files/tag_system.csv")
    df_tagsystem['Tag'] = df_tagsystem.applymap(lambda x: '__label__' + str(x))['TagID']
    return df_tagsystem


def training_model():
    training_file = TAG_PATH+ "/Files/training_data.txt"

    model = fasttext.train_supervised(input=training_file, lr=0.5, epoch=25,
                                      wordNgrams=2, bucket=200000, dim=50, loss='ova')
    model.save_model(TAG_PATH+"/Model/model_userstory.bin")
    #result = model.test("C:/Users/lbao009/Documents/testing_data.txt")

def predict(userstory):
    model_file = TAG_PATH +  '/Model/model_userstory.bin'
    if not os.path.exists(model_file):
        training_model()
    df_tags = get_tagsystem()
    classifier = fasttext.load_model(model_file)

    label = classifier.predict(userstory)
    Label_Id = int(label[0][0][9:])
    df_result = df_tags[df_tags['TagID'] == Label_Id]
    return (df_result['Capability'].iloc[0],df_result['Sub-Capability'].iloc[0],df_result['Epic'].iloc[0])

def predict_tag(userstory):
    model_file = TAG_PATH +  '/Model/model_userstory.bin'
    if not os.path.exists(model_file):
        training_model()
    classifier = fasttext.load_model(model_file)

    label = classifier.predict(userstory)
    Label_Id = int(label[0][0][9:])

    return Label_Id




def recommend_stories(userstory):
    model_file = TAG_PATH +  '/Model/model_userstory.bin'
    userstory_file = TAG_PATH + '/Files/training_data.csv'
    df_userstories = pd.read_csv(TAG_PATH + "/Files/userstories.csv")
    if not os.path.exists(model_file):
        training_model()
    df_tags = get_tagsystem()
    classifier = fasttext.load_model(model_file)

    label = classifier.predict(userstory)
    Label_Id = label[0][0]
    stories = df_userstories[df_userstories['Label'] == Label_Id]['Story'].tolist()
    return stories

def tag_batchjob():
    model_file = TAG_PATH + '/Model/model_userstory.bin'
    if not os.path.exists(model_file):
        training_model()
    df_tags = get_tagsystem()

    df_predict = pd.read_csv(TAG_PATH+"/Files/testing_data.csv")
    texts = df_predict["Story"].str.strip().str.replace('\n', '').tolist()

    classifier = fasttext.load_model(model_file)

    labels = classifier.predict(texts)
    df_predict['Tag'] = pd.Series(labels[0]).apply(lambda x: x[0])

    df_result = pd.merge(df_predict, df_tags, on='Tag', how='left')
    df_result.to_csv(TAG_PATH+'/Files/result.csv', columns=['Tag', 'Story'], index=False)

if __name__ == "__main__":
    print(predict_tag('HR stories, as an HR, I would like'))




