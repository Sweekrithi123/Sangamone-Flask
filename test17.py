from flask import Flask,render_template,request
test17=Flask(__name__)
@test17.route("/",methods=["POST","GET"])
def diamondfull():
    output1=""
    if request.method=="POST":
        s1=request.form.get("input1")
        len1=len(s1)
        s2=" "
        for j in range(0,len1-5,1):   
            for i in range(0,len1-j,1):
                output1=output1+s2
            output1=output1+s1[0:(1+(2*j))]
            output1+="\n"


        for j in range(len1-7,-1,-1):   
            for i in range(0,len1-j,1):
                output1=output1+s2
            output1=output1+s1[0:(1+(2*j))]
            output1+="\n"
    return render_template("diamond8.html",message1=output1)
if __name__=="__main__":
    test17.run(debug=True)


