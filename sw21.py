from flask import Flask,render_template
sw21=Flask(__name__)
@sw21.route("/",methods=["GET","POST"])
def showmovies1():
    list1=[]
    list2=[]
    f1=open("GoodMovies_2022_0216.csv","r")
    for i in range(0,127,1):
        temp=f1.readline().replace('"','').replace("\n","").split(",")
        list1.append(temp[0])
        list2.append(temp[1])
    print(list1)
    print()
    print(list2)
    result=list2
    return render_template("movies2.html",message1=result)
if __name__=="__main__":
    sw21.run(debug=True)
