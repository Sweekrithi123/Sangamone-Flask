from flask import Flask,render_template,request
coversion5=Flask(__name__)
@coversion5.route("/",methods=["GET","POST"])
def currency():
    inr=1
    if request.method=="POST":
        usd1=int(request.form.get("input1"))
        inr=usd1*74.75
        print("Currency in INR is:",round(inr))
    return render_template("currency.html",message1=inr)

if __name__ == "__main__":
     coversion5.run(debug=True)



            
