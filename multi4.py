from flask import Flask, render_template
multi4=Flask(__name__)
@multi4.route("/",methods=["POST", "GET"])
def multiplication2():
    result=""
    file1=open("in2.txt","r")
    start=int(file1.readline())
    end=int(file1.readline())

    for i in range(start,end+1):
        print("multiplication table",(i))
        for j in range(1,11):
            output=(str(i)+"*"+str(j)+"="+str(i*j))
            result=result+output+"\n"
        result=result+"\n"
    print(result)
    return render_template("multiplication.html",message1=result)

if __name__ == "__main__":
     multi4.run(debug=True)

