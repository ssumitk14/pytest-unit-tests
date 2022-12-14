from app.employee import Employee
from app.employee import  add, multiply


if __name__=="__main__":
    num1 = 10
    num2 = 20

    res = add(num1,num2)
    print(multiply(res, num2))