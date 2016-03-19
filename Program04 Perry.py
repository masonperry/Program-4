print("Welcome to Calculator")

#Addition Function
def sum(num1, num2):
    #find operator
    add_pos = expr.find("+")
    if add_pos != -1:
        print(inValid)
    #recognize "+" expression
    expr[add_pos] = "+"
    isdigit(expr[ :add_pos])                    #Find number before plus sign
    isdigit(expr[add_pos+1: ])                  #Find number after plus sign
    #addition operator
    add = num1 + num2
    #Find out last stored value
    value = input("You can also type 'last' to see recently stored value: ")
    if value == "last":
    #Adding last sum to list
        a_store = [add]
        for i in store:
            print(i)
    return add

#Subtraction Function
def diff(num1, num2):
    #find operator
    sub_pos = expr.find("-")
    if sub_pos != -1:
        print(inValid)
    #recognize "-" expression
    expr[sub_pos] = "-"
    isdigit(expr[ :sub_pos])                    #Find number before minus sign
    isdigit(expr[sub_pos+1: ])                  #Find number after minus sign
    #Subtraction operator
    subtract = num1 - num2
    #Find out last stored value
    value = input("You can also type 'last' to see recently stored value: ")
    if value == "last":
    #Adding last subtraction to list
        s_store = [subtract]
        for i in store:
            print(i)
    return subtract

#Multiplication function
def product(num1, num2):
    mult_pos = expr.find("*")
    if mult_pos != -1:
        print(inValid)
    #recognize "*" expression
    expr[mult_pos] = "*"
    isdigit(expr[ :mult_pos])       #Find number before multiplication sign                          
    isdigit(expr[mult_pos+1: ])     #Find number after multiplication sign
    #multiplication operator
    multiply = num1 * num2
    #Find out last stored value
    value = input("You can also type 'last' to see recently stored value: ")
    if value == "last":
    #Adding last multiplication to list
        m_store = [multiply]
        for i in store:
            print(i)
    return multiply

#Division Function
def quotient(num1, num2):
    #find operator
    div_pos = expr.find("/")
    if div_pos != -1:
        print(inValid)
    #recognize "/" expression
    expr[div_pos] = "/"
    isdigit(expr[ :div_pos])                #Find number before division sign
    isdigit(expr[div_pos+1: ])              #Find number after division sign
    #division operator
    divide = num1 / num2
    #Find out last stored value
    value = input("You can also type 'last' to see recently stored value: ")
    if value == "last":
    #Adding last division to list
        d_store = [divide]
        for i in store:
            print(i) 
    return divide

inValid ="In Valid"
