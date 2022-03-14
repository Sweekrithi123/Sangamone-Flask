from flask import Flask,render_template,request
calculator1=Flask(__name__)
@calculator1.route("/",methods=["GET","POST"])
def calculator():
    result=""
    if request.method=="POST":
        print("1.Addition(+)")
        print("2.Subtraction(-)")
        print("3.Multiplication(*)")
        print("4.Division(/)")
        print("enter your choice:")
        choice=int(request.form.get("choice"))

        if choice == 1 :
            num1=int(request.form.get("input1"))
            num2=int(request.form.get("input2"))
            sum1=str(num1+num2)
            print(sum1)
            result=result+sum1+"\n"
            result=result+"\n"

        elif choice == 2:
            num1=int(request.form.get("input1"))
            num2=int(request.form.get("input2"))
            dif1=str(num1-num2)
            print(dif1)
            result=result+dif1+"\n"
            result=result+"\n"

        elif choice == 3:
            num1=int(request.form.get("input1"))
            num2=int(request.form.get("input2"))
            mul1=str(num1*num2)
            print(mul1)
            result=result+mul1+"\n"
            result=result+"\n"

        elif choice == 4:
            num1=int(request.form.get("input1"))
            num2=int(request.form.get("input2"))
            div1=str(num1/num2)
            print(div1)
            result=result+div1+"\n"
            result=result+"\n"

        else:
            print("invalid")
            result="invalid"
    return render_template("calculator.html",message1=result)
if __name__=="__main__":
    calculator1.run(debug=True)
