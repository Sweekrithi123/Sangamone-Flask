from flask import Flask,render_template
flive=Flask(__name__)
@flive.route("/helloworld",methods=["GET","POST"])
def helloworld():
    info1="Hello world"
    print(info1)
    return render_template("helloworld.html",message1=info1)
@flive.route("/goodmorning",methods=["GET","POST"])
def goodmorning():
    info2="Good Morning"
    print(info2)
    return render_template("goodmorning.html",message2=info2)
@flive.route("/",methods=["GET","POST"])
def home():
    return render_template("index.html")



if __name__=="__main__":
    flive.run(debug=True)
