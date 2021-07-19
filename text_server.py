from os import remove
from flask import Flask,request
from pyhtml import html,title,body,p,form,head,label,input_,a
import string
app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def text_analy():
    code = html(
        head(
        title("analysis")
        ),    
        body(
            p("Welcome to text analysis"),
            form(action = "result")
            (   
                label("Please type in text you want analysis"),
                input_(type="text",name="user_text"),
                input_(type="submit",value="submit")
            )
        )
    )
    return str(code)

@app.route('/result',methods=["POST"])
def text_result():
    text = request.form["user_text"]
    punctuation_num = 0
    newtext = ""
    for i in text:
        if i in string.punctuation:
            punctuation_num+=1
            newtext+=" "
        else:
            newtext+=i
    print(newtext)
    print(newtext.split(" "))
    newtextlist = list(newtext.split(" "))
    while "" in newtextlist:
        newtextlist.remove("")
    number = len(newtextlist) if text != '' else 0
    code = html(
        head(
        title("result")
        ),
        body(
            p(f"the number of characters (including spaces and punctuation):{len(text)}"),
            p(f"the number of characters (excluding punctuation):{len(text)-punctuation_num}"),
            p(f"the number of words:{number}"),
            form(action = "/")(
                input_(type="submit",value="Back")
            )
        )
    )
    return str(code)

if __name__ == "__main__":
    app.run(debug = True)