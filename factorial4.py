from flask import Flask, render_template,request
factorial1=Flask(__name__)

@factorial1.route("/",methods=["POST", "GET"])
def factorial2():
    fact1=1
    if request.method=="POST":
        num1=int(request.form.get("input1"))
        for i in range(1,num1+1):
            fact1=fact1*i
    return render_template("factorial.html",message1=fact1)



if __name__ == "__main__":
     factorial1.run(debug=True)
