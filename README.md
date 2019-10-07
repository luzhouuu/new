# UserStoriesTag 

Golang User Story Recommendation/Query Engine

Related repos:
> https://github.com/bao1018/gpt-2-master
>
> https://github.com/luzhouuu/serifer

## Overall Tech Arch Diagram

![Image of Arch Design](https://i.imgur.com/I1Y3GiG.png)

# Installation

Git clone this repository, and `cd` into directory for remaining commands

```
git clone https://github.com/luzhouuu/UserstoreisTag
```

# train_supervised parameters

```
input             # training file path (required)
    lr                # learning rate [0.1]
    dim               # size of word vectors [100]
    ws                # size of the context window [5]
    epoch             # number of epochs [5]
    minCount          # minimal number of word occurences [1]
    minCountLabel     # minimal number of label occurences [1]
    minn              # min length of char ngram [0]
    maxn              # max length of char ngram [0]
    neg               # number of negatives sampled [5]
    wordNgrams        # max length of word ngram [1]
    loss              # loss function {ns, hs, softmax, ova} [softmax]
    bucket            # number of buckets [2000000]
    thread            # number of threads [number of cpus]
    lrUpdateRate      # change the rate of updates for the learning rate [100]
    t                 # sampling threshold [0.0001]
    label             # label prefix ['__label__']
    verbose           # verbose [2]
    pretrainedVectors # pretrained word vectors (.vec file) for supervised learning []
```


### Requirement

```
pybind11==2.3.0
fasttext==0.9.1
pandas==0.25.1
flask==1.1.1
```
Insteall all packages:

```
pip3 install -r requirements.txt
brew install postgresql
pip3 install psycopg2
pip3 install config
```

make sure you have open other repos, then run:

```json
sudo python run_server.py
```