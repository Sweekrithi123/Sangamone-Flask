from flask import Flask, render_template
multi3=Flask(__name__)
@multi3.route("/",methods=["POST", "GET"])
def multiplication1():
    result=""
    start=int(input("enter 1st no."))
    end=int(input("enter 2nd no."))
    for i in range(start,end+1):
        print("multiplication table",(i))
        for j in range(1,11):
            output=(str(i)+"*"+str(j)+"="+str(i*j))
            result=result+output+"\n"
        result=result+"\n"
    print(result)
    return render_template("multiplication.html",message1=result)

if __name__ == "__main__":
     multi3.run(debug=True)

