# set FLASK_ENV=development
# i should have a folder called template have all html and css files

from flask import Flask

from flask import render_template

import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "<h2> Hello people ..!</h2>"


@app.route("/dd")
def sam():
    return render_template("var1.html")

# take input from url
@app.route("/n<yrName>")
def hereWeGo(yrName):
    return "<h1>hello, {}</h1>".format(yrName)

@app.route("/55")
def dev():
    myHeaderLine = "my name is Samir, thank you"
    return render_template("var.html", headline=myHeaderLine)

# link a css or html file
@app.route("/bye")
def deve():
    myHeaderLine = "Thank you goodbye"
    return render_template("var.html", headline=myHeaderLine)

# condition
@app.route("/newyear")
def ny():
    now = datetime.datetime.now()
    newyear = now.month == 1 and now.day == 1

    return render_template("ny.html", newyear = newyear)
#looping on a list
@app.route("/gf")
def met1():
    GFnames = ['simona','elisa','athina','cosmina','mila']
    return render_template("ind.html", names=GFnames)

# link page to another page
@app.route("/1")
def givemeMore():
    return render_template("moree.html")
@app.route("/2")
def givemeLess():
    return render_template("less.html")

@app.route("/3")
def giveMe():
    return render_template("b1.html")

# ezay a create end point and post and get
from flask import request

@app.route("/4")
def fo():
    return render_template("req1.html")

@app.route("/shofyrName", methods=['POST'])
def hey():
    myname = request.form.get("yrname")
    myPW = request.form.get("yrPassword")
    return render_template("hello.html", name=myname, pw=myPW)


@app.route("/5")
def fooo():
    return render_template("req2.html")

@app.route("/shofdehkman", methods=['POST','GET'])
def heyYou():
    if request.method == "GET":
        return "Please submit the form ... "
    else:

        myname = request.form.get("yrname")
        myPW = request.form.get("yrPassword")
        return render_template("hello.html", name=myname, pw=myPW)


# mohema awi l session deh

from flask import session
from flask_session import Session

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/shofffff", methods=['POST','GET'])
def funnn():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
# look at week 3 which is lec 2 min 1:41 for local session and global var till 1:44
    return render_template("out.html", notes=notes)




if __name__ == '__main__':
    app.run()