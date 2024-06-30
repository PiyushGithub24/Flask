from flask import Flask ,redirect ,url_for
import time

app=Flask(__name__)

@app.route("/")         
def home():
    return "<h1>Welcome to the Home Page !!!"

@app.route("/passed/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1>Congrats {sname.title()}!! You Have Passed with {marks} marks.."

@app.route("/failed/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1>Sorry {sname.title()} !! You Have Failed with {marks} marks.."


@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<30:
        time.sleep(1)
        #redirect to page "Fail"
        return redirect(url_for("failed",sname=name,marks=num))

    else:
        time.sleep(1)
        #redirect to page "pass"
        return redirect(url_for("passed",sname=name,marks=num))


if __name__=="__main__":
    app.run(debug=True)