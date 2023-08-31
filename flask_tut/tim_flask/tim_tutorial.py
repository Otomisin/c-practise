from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "Hello World!. I am building a web with <b>Flask</b>"

if __name__ == "__main__":
    app.run()
