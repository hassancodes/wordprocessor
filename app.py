from flask import Flask, redirect, url_for
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    # return "<h1>Hi this is Home Page</h1>"
    # return "Hello"
    return render_template('index.html')



# main processing function
@app.route("/process", methods=["POST"])
def process():
    if request.method=='POST':
        sentence = request.form.get("sentence")
        
        mydict = {
            "total" : len(sentence),
            "up" : sentence.upper(),
            "low" : sentence.lower(),
            "listofsentence" : sentence.split(),
            "totalWords" : len(sentence)
            }
        print(mydict)
        
        return render_template("result.html", mydict=mydict)
        # return "Hello"
    
    

app.run(debug=True)