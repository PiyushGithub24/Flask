from flask import Flask

app=Flask(__name__)

@app.route("/")         
def home():
    return "<h1>Welcome to the Home Page !!!"

# @app.route("/welcome/steve")        #this creates static url
# def wel_steve():
#     return "<h1>Hi steve,Welcome to the Webpage Page !!!"

# @app.route("/welcome/john")        #this creates static url
# def wel_john():
#     return "<h1>Hi john,Welcome to the Webpage Page !!!"

@app.route("/welcome/<name>")        #this creates dynamic  url
def wel_name(name):
    return f"<h1>Hi {name} ,Welcome to the Webpage Page !!!"


if __name__=="__main__":
    app.run(debug=True)