from flask import Flask,render_template,request
longitude_latitude2=Flask(__name__)
@longitude_latitude2.route("/",methods=["GET","POST"])
def lat_lon():
    distance=1
    from math import sqrt
    if request.method=="POST":
        x1=int(request.form.get("input1"))
        y1=int(request.form.get("input2"))
        x2=int(request.form.get("input3"))
        y2=int(request.form.get("input4"))
        distance= sqrt((y2-y1)*(y2-y1)*  + (x2-x1)*(x2-x1))
        print("Distance is:",distance)
    return render_template("distance1.html",message1=distance)
if __name__=="__main__":
    longitude_latitude2.run(debug=True)

