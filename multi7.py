from flask import Flask, render_template
multi7=Flask(__name__)
@multi7.route("/",methods=["POST", "GET"])
def multiplication6():
    result=""
    import  datetime as dt
    import os
    input1=int(input("enter 1st no.:"))
    input2=int(input("enter 2nd no.:"))
    path="E:\Interview\epitas\Tabels"
    name="output.txt"
    directory=os.path.join(path,name)
    print(directory)
    file1=open("directory","w")
    for i in range(input1,input2+1):
        print("multiplication table",(i))
        for j in range(1,11):
            info1=str(i)+"*"+str(j)+"="+str(i*j)
            print(info1)
            result=result+info1+"\n"
        result=result+"\n"
    print(result)
    file1.write(result)
    file1.write("\n")     
    file1.close()

    today = dt.datetime.now()
    print("date and time is:",today)
    return render_template("multiplication1.html",message1=result,message2=today)

if __name__ == "__main__":
     multi7.run(debug=True)

