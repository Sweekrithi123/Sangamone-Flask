from flask import Flask, render_template
multi5=Flask(__name__)
@multi5.route("/",methods=["POST", "GET"])
def multiplication3():
    result=""
    file1=open("in3.txt","r")
    file2=open("out3.txt","w")
    info1=file1.readline()
    list1=info1.split(",")
    start=int(list1[0])
    end=int(list1[1].replace("\n",""))
    for i in range(start,end+1):
        print("multiplication table",(i))
        for j in range(1,11):
            info2=str(i)+"*"+str(j)+"="+str(i*j)
            print(info2)
            result=result+info2+"\n"
        result=result+"\n"
    print(result)
    file2.write(result)
    file2.write("\n")
    file2.write("\n")
    file2.close()
    return render_template("multiplication.html",message1=result)

if __name__ == "__main__":
     multi5.run(debug=True)

