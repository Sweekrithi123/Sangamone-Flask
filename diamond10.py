from flask import Flask,render_template,request
diamond9=Flask(__name__)
@diamond9.route("/",methods=["POST","GET"])
def diamond2():
    output1=""
    if request.method=="POST":
        s1=request.form.get("input1")
      
        len1=len(s1)
        for i in range(1,len1+1,1):
            output1=output1+s1[0:i]+"\n"
            
        for i in range(1,len1,1):
            output1=output1+s1[0:len1-i]+"\n"
    return render_template("diamond8.html",message1=output1)
if __name__=="__main__":
    diamond9.run(debug=True)
