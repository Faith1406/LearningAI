from flask import Flask, render_template, request, session
import Rae as r

app = Flask(__name__)

app.secret_key = "hello"

@app.before_request
def clear():
    if not session.get("initialized"):
        session.clear()
        session["initialized"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if "history" not in session:
        session["history"] =[]
    history = session["history"]
    show_popup = False
    response = ""

    if request.method == "POST":
        input = request.form.get("user_input", "").strip()
        correct_input = request.form.get("correct_response", "").strip()
        if input:
            response, show_popup = r.chatbot(input,"")
            if response:
                history.append({"user": input, "rae": response})
            else:
                show_popup = True
                response, show_popup = r.chatbot(input,correction_input=correct_input)
                if correct_input:
                    history.append({"user": input, "rae": correct_input})
                else:
                    history.append({"user": input, "rae": "No answer provided yet."})
                
        session["history"] = history

    return render_template("index.html", history=history, response=response, show_popup=show_popup)

@app.route("/clear")
def clear():
    session.clear()
    return render_template("index.html")

if __name__ == "__main__":
    
    app.run(debug=True)
