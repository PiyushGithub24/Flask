from flask import (
    Flask , 
    render_template ,
    redirect ,
    url_for ,
    flash
)

from forms import SignupForm , LoginForm

app=Flask(__name__)
app.config["SECRET_KEY"]="this_is_a_secret_key"

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title="Home")

@app.route('/login', methods=["GET","POST"])
def login():
    form=LoginForm()
    email=form.email.data
    pw=form.password.data
    if form.validate_on_submit():
        if (email=="abc@gmail.com" and pw=="12345"):
            flash(f"Successfully Logged in !!")
            return redirect(url_for("home"))
        
        else:
            flash(f"Incorrect Username or Password !!")
    return render_template("login.html",title="Login",form=form)

@app.route('/signup', methods=["GET","POST"])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        flash(f"Successfully Registered {form.username.data}!!")
        return redirect(url_for("home"))
    return render_template("signup.html",title="Signup",form=form)

if __name__=="__main__":
    app.run(debug=True)