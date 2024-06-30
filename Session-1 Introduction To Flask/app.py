from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to the Home Page...</h1>"

@app.route('/about')
def about():
    return "<h1>Welcome to the About Page...</h1>"

@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1> Hi {name.title()} !!\n You are Welcome to this Home page..."


@app.route('/addition/<int:num>')
def addition(num):
    return f"<h1>Input is {num} and addition with 10 is {num+10}<h1>"

@app.route('/addition_two/<int:num1>/<int:num2>')
def addition_two(num1,num2):
    return f"<h1>Input is {num1} and {num2}..The addition  is {num1+num2} <h1>"

if __name__=="__main__":
    app.run(debug=True)

