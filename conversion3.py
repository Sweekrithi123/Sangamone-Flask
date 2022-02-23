from flask import Flask,render_template
coversion3=Flask(__name__)
@coversion3.route("/",methods=["GET","POST"])
def currency():
    usd=int(input("enter usd:"))
    inr=usd*74.75
    print("Currency in INR is:",round(inr))
    return render_template("currency1.html",message1=inr)

if __name__ == "__main__":
     coversion3.run(debug=True)



            
