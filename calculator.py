
# add function    
def add(n1,n2):
        result=n1+n2
        print(str(n1) + " + " + str(n2) + " = " + str(result))
# subtract function
def subtract(n1,n2):
        result=n1-n2
        print(str(n1) + "-" +  str(n2) + " = " + str(result))
# multiply function
def multiply(n1,n2):
        result=n1*n2
        print(str(n1) + "*" + str(n2) + " = " + str(result))
# divide function
def divide(n1,n2):
        # for denomrator zero 
        if n2 ==0:
            while 1:
                # error checking
                print("\nERROR : denomrator can't be zero \n")
                n2=int(input("Enter Second Number: "))
                if n2 !=0:
                    break

        result=n1/n2
        print(str(n1) + "/" + str(n2) + " = " + str(result))
# modulus function
def modulus(n1,n2):
        result=n1%n2
        print(str(n1) + "%" + str(n2) + " = " + str(result))
# power function
def power(n1,n2):
        result=n1**n2
        print(str(n1) + "**" + str(n2) + " = " + str(result))

def palindrome(num):
        l=len(num)
        left=0
        right=l-1
        while left<right:
                if num[left] != num[right]:
                        break
                left=left+1
                right=right-1
        if left<right:
                print(num + " is NOT palindrome ")
        else:
                print(num + " is  palindrome ")

# infinite loop untill user quit                                 
while 1:
        print("Select operataion. ")
        print("To add two numbers type in 'add' or '+' ")
        print("To subtract two numbers type in 'subtract' or '-' ")
        print("To multiply two numbers type in 'multiply' or '*' ")
        print("To divide two numbers type in 'divide' or '/' ")
        print("To calculate the  modulus of two numbers type in 'modulus' or '%' ")
        print("To use the power function type in 'power' or '^' ")
        print("To use the palindrome function type in 'palindrome' or '@'")
# taking user choice 
        choice=input("\nEnter your choice :  ")
# taking user inputs        
        if choice == "palindrome" or choice == "@":
                num=str(input("Enter the Number: "))
        else:        
                n1=int(input("Enter First Number: "))
                n2=int(input("Enter Second Number: "))
#  checking for which operation
        if choice == "add" or choice == "+":
            add(n1,n2)
        if choice == "subtract" or choice == "-":
            subtract(n1,n2)    
        if choice == "multiply" or choice == "*":
            multiply(n1,n2)
        if choice == "divide" or choice == "/":
            divide(n1,n2)
        if choice == "modulus" or choice == "%":
            modulus(n1,n2)
        if choice == "power" or choice == "^":
            power(n1,n2)
        if choice == "palindrome" or choice == "@":
            palindrome(num)     

# asking for continue or stop            
        check=input("Do you want to continue : ")
        if check != "YES" and check != "Y" and check != "yes" and check != "y":
            break
        print("\n")
         
