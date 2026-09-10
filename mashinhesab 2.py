def mashinhesab (num1 , num2 , amaliat):
    

    if amaliat == "+":
       result=num1+num2
    elif amaliat== "_":
        result=num1-num2
    elif amaliat=="*":
       result=num1*num2
    elif amaliat== "/":
        result=num1/num2

    return result 

num1:float(input("عدد اول را وارد کنید"))
num2:float(input("عدد دوم را وارد کنید"))
amaliat:input("+ , - , * , / ")
result= mashinhesab(num1 , num2 , amaliat)
print(result)