from flask import Flask,render_template
test18=Flask(__name__)
@test18.route("/",methods=["POST","GET"])
def diamondfull():
    s1="Sweekrithi"
    len1=len(s1)
    s2=" "
    output1=""
    
    for i in range(1,len1+1,1):
        output1=output1+s1[0:i]+"\n"
        
    for i in range(1,len1,1):
        output1=output1+s1[0:len1-i]+"\n"

    for j in range(1,len1+1,1):   
        for i in range(0,len1-j,1):
            output1=output1+s2
            
        output1=output1+s1[0:j]
        output1+="\n"

    for j in range(1,len1,1):   
        for i in range(0,j,1):
            output1=output1+s2
        output1=output1+s1[0:len1-j]
        output1+="\n"
        


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
    test18.run(debug=True)


