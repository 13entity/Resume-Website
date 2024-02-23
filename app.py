from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
