import SRC.main as Main
import SRC.RequestGoTag as RequestGoTag
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def open_server():
    prompt = ""
    result=()
    texts2 = []

    if request.method == 'POST':
        prompt = request.form['prompt'].strip()

        # if '"' in prompt:
        #     prompt = prompt.replace('"', '')

        if prompt:
            taglable = Main.predict(prompt, 'Sub-Capability')
            tagid = Main.get_tagId(taglable, 'Sub-Capability')
            result_json = RequestGoTag.requestGoTag(prompt, tagid)
            result = RequestGoTag.GetResult(result_json)
            # (capability, sub_capability, epic) = FastText.predict(prompt)
            # capability = str(capability)
            # sub_capability = str(sub_capability)
            # epic = str(epic)
            # result = capability+'/'+sub_capability+'/'+epic
            #prompt = str(prompt)
            # texts2 = gotest.gotest(title, prompt)
            # texts = gotest.gotest(title, prompt, tagid)
            texts2 = []
            text_second = RequestGoTag.requestGoTag(prompt)
            for i in range(3):
                texts2.append([text_second[i]['body'], str(round(text_second[i]['Score']*100,2)) + '%'])


        #else:
         #   texts = ""
        # texts.append(result)
        #texts2.append(sss)

    return render_template("page.html", prompt = prompt, texts = result, texts2 = texts2)


if __name__ == "__main__":
    print(("* Loading model and Flask starting server..."
           "please wait until server has fully started"))
    # Run app
    app.run(host="localhost", port=5000)
