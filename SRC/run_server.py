#!/usr/bin/env python3

import fasttext
import pandas as pd
import FastText
import gotest

import numpy as np
from flask import Flask, render_template, request



app = Flask(__name__)



@app.route('/', methods=('GET', 'POST'))
def predict():
    prompt = ""
    texts = []
    texts2 = []

    if request.method == 'POST':
        prompt = request.form['prompt'].strip()


        if prompt:
            (capability, sub_capability, epic) = FastText.predict(prompt)
            result = capability+'/'+sub_capability+'/'+epic
            sss = gotest.gotest(prompt)

        else:
            result = ""
        texts.append(result)
        texts2.append(sss)


    return render_template("page.html", prompt=prompt, texts=texts, sample=texts2)



if __name__ == "__main__":
    print(("* Loading model and Flask starting server..."
           "please wait until server has fully started"))
    # Run app
    app.run(host="localhost", port=5000)