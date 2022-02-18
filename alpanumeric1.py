from flask import Flask, render_template
alpanumeric1=Flask(__name__)
@alpanumeric1.route("/",methods=["POST", "GET"])
def alpa():
    import re
    input = "How are you ? Oh my God, you are bleeding! Let us go to the doctor quickly."
    output = re.sub('[^a-zA-Z\d\s]', '', input)
    print(output)
    return render_template("3.html",message1=output)

if __name__ == "__main__":
     alpanumeric1.run(debug=True)


