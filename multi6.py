from flask import Flask, render_template
multi6=Flask(__name__)
@multi6.route("/",methods=["POST", "GET"])
def multiplication4():
    result=""
    input1=int(input("enter 1st no.:"))
    input2=int(input("enter 2nd no.:"))
    file1=open("7.txt","w")
    file2=open("8.txt","w")
    file3=open("9.txt","w")
    file4=open("10.txt","w")
    for i in range(input1,input2+1):
        print("multiplication table",(i))
        for j in range(1,11):
            info1=str(i)+"*"+str(j)+"="+str(i*j)
            print(info1)
            result=result+info1+"\n"
        result=result+"\n"
    print(result)
    file1.write(result)
    file2.write(result)
    file3.write(result)
    file4.write(result)
    file1.write("\n")
    file2.write("\n")
    file3.write("\n")
    file4.write("\n")     
    file1.write("\n")
    file2.write("\n")
    file3.write("\n")
    file4.write("\n")
    file1.close()
    file2.close()
    file3.close()
    file4.close()
    return render_template("multiplication.html",message1=result)

if __name__ == "__main__":
     multi6.run(debug=True)

