from flask import Flask,render_template
test16=Flask(__name__)
@test16.route("/",methods=["POST","GET"])
def diamondfull():
    s1="Sweekrithi"
    len1=len(s1)
    s2=" "
    output1=""
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
    return render_template("diamond7.html",message1=output1)
if __name__=="__main__":
    test16.run(debug=True)


