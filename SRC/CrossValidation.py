import fasttext
import matplotlib.pyplot as plt

res = []
for i in range(1,100,1):
    model = fasttext.train_supervised(input='df.train', epoch= i, lr = 0.5, wordNgrams=2, loss = 'ova')
    res.append(model.test('df.test')[1])
print(res)
plt.plot(res)
plt.show()