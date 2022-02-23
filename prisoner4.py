from flask import Flask, render_template
prisoner4=Flask(__name__)
@prisoner4.route("/",methods=["POST", "GET"])
def prisoner1():
    result=""
    doors = [False] * 11
    for i in range(1, 11):
        for j in range(i, 11,i):
            doors[j] = not doors[j]
    print("Open doors are:")
    for i in range(1, 11):
        
        if doors[i] is True:
            lucky=str(i)
            result=result+lucky
        result=result+"\n"
    print(result)
            
    return render_template("prisoner.html",message1=result)

if __name__ == "__main__":
     prisoner4.run(debug=True)

