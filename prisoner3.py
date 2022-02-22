from flask import Flask, render_template
prisoner3=Flask(__name__)
@prisoner3.route("/",methods=["POST", "GET"])
def prisoner():
    count=100
    doors=[False]*(count)
    for j in range(0,count,1):
        for i in range(j,count,j+1):
            doors[i]=not doors[i]

    free=[i+1 for i in range(0,count) if doors[i]==True]
    print("lucky prisoners are:",free)
    return render_template("prisoner.html",message1=free)

if __name__ == "__main__":
     prisoner3.run(debug=True)


