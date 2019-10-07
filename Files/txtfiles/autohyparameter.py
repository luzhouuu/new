import fasttext

model = fasttext.train_supervised(input='df.train', autotuneValidationFile='df.test')
model.tset('df.test')

