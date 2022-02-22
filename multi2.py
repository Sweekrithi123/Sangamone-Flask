from flask import Flask, render_template
multi2=Flask(__name__)
@multi2.route("/",methods=["POST", "GET"])
def multiplication():
    result=""
    for i in range(3,21):
        print("multiplication table for",(i))
        for j in range(1,11):
            output=(str(i)+"*"+str(j)+"="+str(i*j))
            result=result+output+"\n"
        result=result+"\n"
    print(result)
    return render_template("multiplication.html",message1=result)

if __name__ == "__main__":
     multi2.run(debug=True)

