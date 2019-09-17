#!/usr/bin/env python3

import fasttext
import pandas as pd
import SRC.FastText as FastText
import SRC.gotest as gotest

import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def predict():
    prompt = ""
    title = ""
    texts = []
    texts2 = []

    if request.method == 'POST':
        title = request.form['title'].strip()
        prompt = request.form['prompt'].strip()

        if '"' in title:
            title = title.replace('"', '')
        if '"' in prompt:
            prompt = prompt.replace('"', '')

        if prompt:
            tagid = FastText.predict_tag(title + prompt)
            # (capability, sub_capability, epic) = FastText.predict(prompt)
            # capability = str(capability)
            # sub_capability = str(sub_capability)
            # epic = str(epic)
            # result = capability+'/'+sub_capability+'/'+epic
            prompt = str(prompt)
            print(prompt)
            texts2 = gotest.gotest(title, prompt)
            texts = gotest.gotest(title, prompt, tagid)
        else:
            texts = ""
        # texts.append(result)
        #texts2.append(sss)

    return render_template("page.html", title=title, prompt=prompt, texts=texts, name1= texts2)


if __name__ == "__main__":
    print(("* Loading model and Flask starting server..."
           "please wait until server has fully started"))
    # Run app
    app.run(host="localhost", port=5000)
