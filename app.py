from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "suma":
            result = num1 + num2
        elif operation == "resta":
            result = num1 - num2
        elif operation == "multiplicacion":
            result = num1 * num2
        elif operation == "division":
            result = num1 / num2

        return render_template("index.html", result=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
