from flask import Flask , render_template ,url_for
from employees import employees_data

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    #return "<h1>Welcome to the Home Page...</h1>"
    return render_template("home.html",title="Home")

@app.route('/about')
def about():
    #return "<h1>Welcome to the About Page...</h1>"
    return render_template("about.html",title="About")

@app.route('/evaluate/<int:num>')
def evaluate(num):
    #return "<h1>Welcome to the About Page...</h1>"
    return render_template("evaluate.html",
                           title="Evaluate",
                           number=num)

@app.route('/employees')
def employees():
    #return "<h1>Welcome to the About Page...</h1>"
    return render_template("employees.html",
                           title="Employees",
                           employees=employees_data)

@app.route('/employees/managers')
def managers():
    #return "<h1>Welcome to the About Page...</h1>"
    return render_template("managers.html",
                           title="Managers",
                           employees=employees_data)

if __name__=="__main__":
    app.run(debug=True)