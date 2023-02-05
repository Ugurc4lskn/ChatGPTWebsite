from flask import request, render_template, Flask
import openai
from chatApi import chatBot


app = Flask(__name__, static_folder="static")


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        __userInput = request.form.get("UserInput")
        response = chatBot(msg=__userInput)
        
        return render_template("index.html", inputValue = __userInput, response = response)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    
