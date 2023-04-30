from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/about')
def about_page():
   return "About page"

@app.route('/login')
def login():
  return "Login Here"

@app.route('/greet/<user>')
def greet(user):
   return f"Hello {user}"

@app.route('/greet/<string:user>/<int:age>')
def greet_user(user, age):
   return f"This is {user} and you are {age}"   

@app.route('/contact')
def contact():
   return "You can contact me on **2931131111**"

if __name__ == "__main__":
  app.run(debug=True)
  app.run(host='0.0.0.0', port=5000)