def fact():
    fact1=1
    num1=int(input("enter a number:"))

    for i in range(1,num1+1):
        fact1=fact1*i
    print("the factorial is:",fact1)
fact()
