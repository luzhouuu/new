#!/usr/bin/env python3

import fasttext
import pandas as pd
import SRC.main as Main
import SRC.RequestGoTag as RequestGoTag

import numpy as np
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def open_server():
    prompt = ""
    title = ''
    result=()
    texts = []
    texts2 = []

    if request.method == 'POST':
        prompt = request.form['prompt'].strip()

        # if '"' in title:
        #     title = title.replace('"', '')
        # if '"' in prompt:
        #     prompt = prompt.replace('"', '')

        if prompt:
            taglable = Main.predict(prompt, 'Sub-Capability')
            tagid = Main.get_tagId(taglable, 'Sub-Capability')
            result = RequestGoTag.requestGoTag(prompt, tagid)
            # (capability, sub_capability, epic) = FastText.predict(prompt)
            # capability = str(capability)
            # sub_capability = str(sub_capability)
            # epic = str(epic)
            # result = capability+'/'+sub_capability+'/'+epic
            #prompt = str(prompt)
            #print(prompt)
            # texts2 = gotest.gotest(title, prompt)
            # texts = gotest.gotest(title, prompt, tagid)
        #else:
         #   texts = ""
        # texts.append(result)
        #texts2.append(sss)

    return render_template("page.html", prompt=prompt, texts=result)


if __name__ == "__main__":
    print(("* Loading model and Flask starting server..."
           "please wait until server has fully started"))
    # Run app
    app.run(host="localhost", port=5000)
