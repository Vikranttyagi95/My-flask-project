from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/blog")
def my_blog():
    return "This is my blog!"

if __name__ == '__main__':
    app.run()
