from flask import Flask, render_template
angle5=Flask(__name__)
@angle5.route("/",methods=["POST", "GET"])
def clock():
    result=""
    for j in range(0,12,1):
        for i in range(0,12,1):
            time1=(str(9+j)+":"+str(i*5).zfill(2))
            angle=((90-j*30)+i*30-i*2.5)
            output=(str(time1)+"-"+str(angle%360))
            result=result+output+"\n"
        result=result+"\n"
    print(result)
    return render_template("4.html",message1=result)

if __name__ == "__main__":
     angle5.run(debug=True)

