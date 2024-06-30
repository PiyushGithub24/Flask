from flask import Flask ,redirect ,url_for
import time

app=Flask(__name__)

@app.route("/")         
def home():
    return "<h1>Welcome to the Home Page !!!"

@app.route("/passed")
def passed():
    return "<h1>Congrats !! You Have Passed.."

@app.route("/failed")
def failed():
    return "<h1>Sorry !! You Have Failed.."

@app.route("/score/<name>/<int:marks>")
def score(name,num):
    if num<30:
        time.sleep(1)
        #redirect to page "Fail "
        return redirect(url_for("failed"))

    else:
        time.sleep(1)
        #redirect to page "pass"
        return redirect(url_for("passed"))


if __name__=="__main__":
    app.run(debug=True)