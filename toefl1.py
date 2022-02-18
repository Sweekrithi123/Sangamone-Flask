from flask import Flask, render_template
toefl1=Flask(__name__)
@toefl1.route("/",methods=["POST", "GET"])
def toefl():
    import re
    text="Another day, and more cases reported from across the country. The number of COVID-19 cases tested positive in India is 156 and there are 139 active cases. According to WHO, as of March 17, there were 184,976 confirmed COVID-19 cases and 7,529 deaths in 159 countries.Chennai reported its second positive case today, West Bengal reported its first case yesterday, and the government of Goa made a *faux pas*.The State's health minister said a Norwegian national had tested positive but shortly afterwards retracted his remark."
    print(text)
    res = re.findall("\*([^\*]*)\*", text)
    print(res)
    return render_template("toefl.html",message1=text,message2=res)

if __name__ == "__main__":
     toefl1.run(debug=True)

