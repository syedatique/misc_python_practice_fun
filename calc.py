#calculator program

#this variable tells the loop whether it should loop or not.
# 1 means loop. anything else means don't loop.



def menu():
    #print what options you have
    print "Welcome to calculator.py "

    print "your options are:"
    print " "
    print "1) Addition"
    print "2) Subtraction"

    print "3) Multiplication"

    print "4) Division"
    print "5) Quit calculator.py"
    print " "
    return (input("enter your choice: "))

def add(a,b):
	return a+b
def subtract(a,b):
	return a-b
def division(a,b):
	return a/float(b)
def multiply(a,b):
	return a*b


loop = 1

#this variable holds the user's choice in the menu:

choice = 0

while loop == 1:

	choice = menu()
	if choice == 1:
	    add1 = input("Add this: ")
	    add2 = input("to this: ")
	    print add1, "+", add2, "=", add(add1,add2)
	    raw_input("PRESS ENTER TO CONTINUE -- ")
	elif choice == 2:
	    sub2 = input("Subtract this: ")
	    sub1 = input("from this: ")
	    print sub1, "-", sub2, "=", subtract(sub1,sub2)
	    raw_input("PRESS ENTER TO CONTINUE -- ")
	elif choice == 3:
	    mul1 = input("Multiply this: ")
	    mul2 = input("with this: ")
	    print mul1, "*", mul2, "=", multiply(mul1,mul2)
	    raw_input("PRESS ENTER TO CONTINUE -- ")
	elif choice == 4:
	    div1 = input("Divide this: ")
	    div2 = input("by this: ")
	    print div1, "/", div2, "=", division(div1,div2)
	    raw_input("PRESS ENTER TO CONTINUE -- ")
	elif choice == 5:
	    loop = 0
		
print "Thankyou for using calculator.py!"