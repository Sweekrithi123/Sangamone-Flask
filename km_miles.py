from flask import Flask, render_template
km_miles=Flask(__name__)
@km_miles.route("/",methods=["POST", "GET"])
def conversion():
    result=""
    file1=open("input1.txt","r")
    for line in file1:
        list1=line.split(" ")
        print(list1)
        lhs_value=int(list1[0])
        lhs_units=list1[1]
        equals=list1[2]
        rhs_value=int(list1[3])
        rhs_units=list1[4].replace("\n","")
        km=str("1"+lhs_units+equals+str(rhs_value/lhs_value)+rhs_units)
        result=result+km+"\n"
        meter=str("1"+rhs_units+equals+str(lhs_value/rhs_value)+lhs_units)
        result=result+meter+"\n"
        result=result+"\n"
    print(result)
    return render_template("km_meter.html",message1=result)

if __name__ == "__main__":
     km_miles.run(debug=True)


    



